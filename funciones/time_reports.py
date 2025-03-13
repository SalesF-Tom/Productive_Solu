import requests
import pandas as pd
import os
from dotenv import load_dotenv
# from endpoints import dic_endpoints
from funciones.endpoints import dic_endpoints
from datetime import datetime, timedelta
import pytz
import time
load_dotenv()
TIMEZONE = pytz.timezone('America/Argentina/Buenos_Aires')

access_token = os.getenv("ACCESS_TOKEN_TOMAS")
organization_id = os.getenv("X_ORGANIZATION_ID")

headers = {
    "Content-Type": "application/vnd.api+json; charset=utf-8",
    "X-Auth-Token": access_token,
    "X-Organization-Id": organization_id
}

url_time_reports = dic_endpoints['url_time_reports']


def get_time_report(start_date=None):
    time_report_data = []

    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    start_date = TIMEZONE.localize(start_date)
    end_date = datetime.now(TIMEZONE) - timedelta(days=1)

    current_date = start_date
    while current_date <= end_date:
        # print(f"Obteniendo datos para la fecha: {current_date.strftime('%Y-%m-%d')}")
        
        date_filter = f"&filter[date][eq]={current_date.strftime('%Y-%m-%d')}"  
        include_param = "&include=person"
        page_number = 1
        retries = 0  
        
        while True:
            response = requests.get(
                f"{url_time_reports}?page[number]={page_number}{date_filter}{include_param}",
                headers=headers
            )

            # if response.status_code == 429:  
            if response.status_code != 200:
                retries += 1
                wait_time = 2 ** retries  
                print(f"Error {response.status_code}: esperando {wait_time} segundos antes de reintentar...")
                time.sleep(wait_time)
                if retries > 5:
                    print(f"No se pudo completar la solicitud para {current_date.strftime('%Y-%m-%d')}. Pasando al siguiente día.")
                    break
                continue  

            retries = 0 
            data = response.json().get('data', [])

            if not data:
                break

            for row in data:
                attributes = row.get('attributes', {})
                person = None

                if 'person' in row.get('relationships', {}):
                    person = row['relationships']['person']['data']
                
                id_custom_field = str(person.get('id') if person else None) + "-" + str(current_date.strftime('%Y%m%d'))
                time_report_data.append({
                    'person_id': person.get('id') if person else None,  
                    'capacity_': attributes.get('capacity', ''),
                    'available': attributes.get('available_time', ''),
                    'scheduled': attributes.get('scheduled_time', ''),
                    'worked': attributes.get('worked_time', ''),
                    'billable': attributes.get('billable_time', ''),
                    'date_': current_date.strftime('%Y-%m-%d'),
                    'time_report_id': row.get('id'),
                    'id_custom_field':id_custom_field
                })

            if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
                page_number += 1
            else:
                break
        
        current_date += timedelta(days=1)

    df = pd.DataFrame(time_report_data)

    datetime_columns = ['date_']
    for col in datetime_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce',utc=True)

    return df
