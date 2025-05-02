from bigquery.bigquery_func import Insertar_Datos_BQ

def cargar_entidad(client, entidad_config, df):
    if df.empty:
        print(f"⚠️  No hay datos para {entidad_config['table']}.")
        return

    nombre_tabla = entidad_config["table"]

    # Carga en tabla temporal
    Insertar_Datos_BQ(
        client,
        entidad_config["schema"],
        nombre_tabla,
        df,
        tipo="temp",
        metodo="WRITE_TRUNCATE"
    )

    # Ejecutar MERGE a tabla final
    entidad_config["merge"](
        client,
        f"{entidad_config['project_id']}.{entidad_config['dataset_final']}.{nombre_tabla}",
        f"{entidad_config['project_id']}.{entidad_config['dataset_temp']}.{nombre_tabla}_temp"
    )
