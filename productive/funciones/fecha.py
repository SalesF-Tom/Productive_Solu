from datetime import datetime, timedelta
import pytz

TIMEZONE = pytz.timezone('America/Argentina/Buenos_Aires')
fecha_actual = datetime.now(TIMEZONE)


def obtener_fecha_ayer():
    ayer = fecha_actual - timedelta(days=1)
    return ayer.strftime('%Y-%m-%d')

# print(obtener_fecha_ayer())  

def obtener_lunes_semana_pasada():
    hoy = fecha_actual
    dia_semana = hoy.weekday()  # Lunes=0, ..., Domingo=6
    # Retroceder hasta el lunes de la semana pasada
    dias_hasta_lunes = dia_semana + 7
    lunes_semana_pasada = hoy - timedelta(days=dias_hasta_lunes)
    return lunes_semana_pasada.strftime('%Y-%m-%d')

# print(obtener_lunes_semana_pasada())  # Salida: '2024-11-18' si hoy es '2024-11-29'

def obtener_primer_dia_mes_pasado():
    hoy = fecha_actual
    # Calcular el mes pasado
    primer_dia_mes_actual = hoy.replace(day=1)  # Ir al primer día del mes actual
    mes_pasado = primer_dia_mes_actual - timedelta(days=1)  # Retroceder un día para llegar al mes pasado
    primer_dia_mes_pasado = mes_pasado.replace(day=1)  # Ir al primer día del mes pasado
    return primer_dia_mes_pasado.strftime('%Y-%m-%d')