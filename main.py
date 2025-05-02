import os
import time
import pytz
import schedule
import logging
from dotenv import load_dotenv
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from notificador import enviar_a_discord


# Cargar entorno
load_dotenv()
CREDENTIALS_PATH = "./credenciales/data-warehouse-311917-73a0792225c7.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = CREDENTIALS_PATH
os.environ["GOOGLE_CLOUD_DISABLE_GRPC"] = "True"

# Logger sin emojis
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("productive_etl.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

# Imports del proyecto
from bigquery.bigquery_func import Get_BQ_service
from productive.entidades import ENTIDADES
from productive.loader import cargar_entidad
from productive.funciones.fecha import (
    obtener_fecha_ayer,
    obtener_lunes_semana_pasada,
    obtener_primer_dia_mes_pasado
)

client = Get_BQ_service()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_FINAL = os.getenv("DATASET_FINAL")
DATASET_TEMP = os.getenv("DATASET_TEMP")
TIMEZONE = pytz.timezone("America/Argentina/Buenos_Aires")

resultados = {}

def ejecutar_entidad(nombre_entidad, fecha=None):
    try:
        config = ENTIDADES[nombre_entidad]
        logging.info(f"Procesando entidad: {nombre_entidad}")
        config["project_id"] = PROJECT_ID
        config["dataset_final"] = DATASET_FINAL
        config["dataset_temp"] = DATASET_TEMP

        kwargs = {}
        if config.get("usa_fecha") and fecha:
            kwargs["start_date"] = fecha

        df = config["getter"](**kwargs)
        df = config["transform"](df)

        if df.empty:
            logging.warning(f"{nombre_entidad}: DataFrame vacío. Se omite carga.")
            resultados[nombre_entidad] = "VACÍO"
            return

        cargar_entidad(client, config, df)
        resultados[nombre_entidad] = f"{len(df)} filas"

    except Exception as e:
        logging.error(f"Error en {nombre_entidad}: {str(e)}")
        resultados[nombre_entidad] = f"ERROR: {str(e)}"

def main(tipo="diario"):
    if tipo == "diario":
        fecha = obtener_fecha_ayer()
    elif tipo == "semanal":
        fecha = obtener_lunes_semana_pasada()
    elif tipo == "mensual":
        fecha = obtener_primer_dia_mes_pasado()
    elif tipo == "historico":
        fecha = "2024-06-01"
    else:
        raise ValueError("Tipo inválido")

    logging.info(f"Iniciando ejecución Productive: {tipo.upper()} - Fecha base: {fecha}")
    start = time.time()

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(ejecutar_entidad, nombre, fecha) for nombre in ENTIDADES]
        for future in futures:
            future.result()

    end = time.time()
    logging.info(f"Pipeline finalizado en {end - start:.2f} segundos.")

    resumen = f"\nResumen de ejecución Productive ({tipo.upper()})\nFecha de corte: {fecha}\nDuración: {end - start:.2f} segundos\n"
    for entidad, resultado in resultados.items():
        resumen += f"- {entidad}: {resultado}\n"

    logging.info(resumen)
    enviar_a_discord(resumen)

def ejecutar_tareas(historico=False):
    hoy = datetime.now(TIMEZONE)
    if historico:
        logging.info("Ejecución histórica")
        main("historico")
    elif hoy.day == 1:
        logging.info("Ejecución mensual")
        main("mensual")
    elif hoy.weekday() == 0:
        logging.info("Ejecución semanal")
        main("semanal")
    else:
        logging.info("Ejecución diaria")
        main("diario")

if __name__ == "__main__":
    try:
        ejecutar_tareas(historico=True)
        while True:
            schedule.run_pending()
            time.sleep(60)
    except KeyboardInterrupt:
        logging.warning("Scheduler detenido manualmente.")
