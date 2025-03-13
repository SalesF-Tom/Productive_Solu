import requests
import pandas as pd
import os
from dotenv import load_dotenv
from funciones.endpoints import dic_endpoints
# from endpoints import dic_endpoints
load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
organization_id = os.getenv("X_ORGANIZATION_ID")

headers = {
    "Content-Type": "application/vnd.api+json; charset=utf-8",
    "X-Auth-Token": access_token,
    "X-Organization-Id": organization_id
}

url_salaries = dic_endpoints['url_salaries']



def get_salaries(start_date=None):
    salaries_data = []
    page_number = 1
    date_filter = ""
    include_param = f'&include=holiday_calendar, person'
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  

    while True:
        response = requests.get(f"{url_salaries}?page[number]={page_number}{date_filter}{include_param}", headers=headers)
        
        if response.status_code != 200:
            print(f"Error en la solicitud: {response.status_code}, Detalles: {response.text}")
            break

        data = response.json().get('data', [])
        if not data:
            break

        for row in data:
            attributes = row.get('attributes', {})
            holiday_calendar = None
            project = None

            if 'person' in row.get('relationships', {}):
                person = row['relationships']['person']['data']

            if 'holiday_calendar' in row.get('relationships', {}):
                holiday_calendar = row['relationships']['holiday_calendar']['data']


            salaries_data.append({
                'salary_id': row['id'],
                'exchange_date': attributes.get('exchange_date', ''),
                'exchange_rate': float(attributes.get('exchange_rate', '')),
                'hours': float(attributes.get('hours', None)),
                'started_on': attributes.get('started_on', ''),
                'currency': attributes.get('currency', ''),
                'cost': attributes.get('cost', ''),
                'holiday_calendar_id': holiday_calendar.get('id'),
                'person_id': person.get('id')
            })


        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break
    df = pd.DataFrame(salaries_data)

    datetime_columns = ['exchange_date', 'started_on']
    for col in datetime_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce',utc=True)

    return df