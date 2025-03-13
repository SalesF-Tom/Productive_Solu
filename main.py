import os
from dotenv import load_dotenv
from datetime import datetime
import pytz
# import schedule
# import time
from schema.schemas import Esquema
from funciones.fecha import obtener_fecha_ayer,obtener_lunes_semana_pasada, obtener_primer_dia_mes_pasado
from funciones.time_reports import get_time_report
from funciones.people import get_people
from funciones.projects import get_projects
from funciones.services import get_services
from funciones.time_entries import get_time_entries
from funciones.deals import get_deals
from funciones.bookings import get_bookings
from funciones.events import get_events
from funciones.salaries import get_salaries
from funciones.holiday_calendars import get_holiday_calendars
from funciones.holidays import get_holidays
from bigquery.bigquery_func import Get_BQ_service, Insertar_Datos_BQ
from bigquery.querys import Merge_Data_Time_Reports_BQ, Merge_Data_People_BQ, Merge_Data_Projects_BQ, Merge_Data_Deals_BQ, Merge_Data_Services_BQ, Merge_Data_Time_Entries_BQ, Merge_Data_Bookings_BQ, Merge_Data_Events_BQ, Merge_Data_Holiday_Calendars_BQ, Merge_Data_Holidays_BQ, Merge_Data_Salaries_BQ

load_dotenv()
client = Get_BQ_service()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_FINAL = os.getenv("DATASET_FINAL")
DATASET_TEMP = os.getenv("DATASET_TEMP")

TIMEZONE = pytz.timezone('America/Argentina/Buenos_Aires')

def main(tipo='diario'):
        if tipo == 'diario':
                fecha = obtener_fecha_ayer()
                print(f"\033[36m Ejecución Diaria \033[0m")
        elif tipo == 'semanal':
                fecha = obtener_lunes_semana_pasada()
                print(f"\033[36m Ejecución Semanal \033[0m")
        elif tipo == 'mensual': 
                fecha = obtener_primer_dia_mes_pasado()
                print(f"\033[36m Ejecución Mensual \033[0m")

        # fecha = "2024-12-01"
        
        print(f"\033[33m Time Report: \033[0m")
        time_report = get_time_report(fecha)
        # print(time_report.head())
        if not time_report.empty:
                Insertar_Datos_BQ(client, Esquema.schema_time_report, 'tbl_productive_time_reports', time_report, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Time_Reports_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_time_reports',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_time_reports_temp'
                )

        print(f"\033[33m People: \033[0m")
        people = get_people()
        # print(people.head())
        if not people.empty:
                Insertar_Datos_BQ(client, Esquema.schema_people, 'tbl_productive_people', people, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_People_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_people',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_people_temp'
                        )


        print(f"\033[33m Projects: \033[0m")
        projects = get_projects()
        # print(projects.head())
        if not projects.empty:
                Insertar_Datos_BQ(client, Esquema.schema_projects, 'tbl_productive_projects', projects, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Projects_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_projects',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_projects_temp'
                        )
        
        print(f"\033[33m Services: \033[0m")
        services = get_services()
        # print(services.head())
        if not services.empty:
                Insertar_Datos_BQ(client, Esquema.schema_services, 'tbl_productive_services', services, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Services_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_services',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_services_temp'
                        )
        print(f"\033[33m Time Entries: \033[0m")
        time_entries=get_time_entries(fecha)
        # print(time_entries.head())
        if not time_entries.empty:
                Insertar_Datos_BQ(client, Esquema.schema_time_entries, 'tbl_productive_time_entries', time_entries, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Time_Entries_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_time_entries',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_time_entries_temp'
                        )
                
        print(f"\033[33m Deals: \033[0m")
        deals = get_deals()
        # print(deals.head())
        if not deals.empty:
                Insertar_Datos_BQ(client, Esquema.schema_deals, 'tbl_productive_deals', deals, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Deals_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_deals',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_deals_temp'
                        )
        
        print(f"\033[33m Bookings: \033[0m")
        bookings = get_bookings(start_date=fecha)
        # print(bookings.head())
        if not bookings.empty:
                Insertar_Datos_BQ(client, Esquema.schema_bookings, 'tbl_productive_bookings', bookings, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Bookings_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_bookings',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_bookings_temp'
                        )
        
        print(f"\033[33m Events: \033[0m")
        events = get_events()
        # print(events.head())
        if not events.empty:
                Insertar_Datos_BQ(client, Esquema.schema_events, 'tbl_productive_events', events, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Events_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_events',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_events_temp'
                        )
        
        print(f"\033[33m Salaries: \033[0m")
        salaries = get_salaries()
        # print(events.head())
        if not salaries.empty:
                Insertar_Datos_BQ(client, Esquema.schema_salaries, 'tbl_productive_salaries', salaries, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Salaries_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_salaries',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_salaries_temp'
                        )
        
        print(f"\033[33m Holiday Calendars: \033[0m")
        holiday_calendars = get_holiday_calendars()
        # print(events.head())
        if not holiday_calendars.empty:
                Insertar_Datos_BQ(client, Esquema.schema_holiday_calendars, 'tbl_productive_holiday_calendars', holiday_calendars, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Holiday_Calendars_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_holiday_calendars',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_holiday_calendars_temp'
                        )
        
        
        print(f"\033[33m Holidays: \033[0m")
        holidays = get_holidays()
        # print(events.head())
        if not holidays.empty:
                Insertar_Datos_BQ(client, Esquema.schema_holidays, 'tbl_productive_holidays', holidays, 'temp', 'WRITE_TRUNCATE')
                Merge_Data_Holidays_BQ(
                        client,
                        'data-warehouse-311917.Productive.tbl_productive_holidays',
                        'data-warehouse-311917.zt_productive_temp.tbl_productive_holidays_temp'
                        )

def ejecutar_tareas():
        hoy = datetime.now(TIMEZONE)
        empieza = hoy
        print(f"Inicio de ejecución: {empieza}")

        if hoy.day == 1:
                main('mensual')
        else:
                main('semanal')

        termina = datetime.now(TIMEZONE)
        print(f"Tiempo de ejecución: {termina-empieza}.\nTerminó:   {termina.strftime('%Y-%m-%d %H:%M:%S')}")
        print("Esperando la hora programada...")



if __name__ == "__main__":
        ejecutar_tareas()
        # main("mensual")
#     try:
#         schedule.every().day.at("03:00").do(ejecutar_tareas)
#         print("Esperando la hora programada...")

#         while True:
#             schedule.run_pending()
#             time.sleep(60)

#     except KeyboardInterrupt:
#         print("Scheduler detenido manualmente.")
        
