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

url_holidays = dic_endpoints['url_holidays']



def get_holidays(start_date=None):
    holidays_data = []
    page_number = 1
    date_filter = ""
    include_param = f'&include=holiday_calendar'
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  

    while True:
        response = requests.get(f"{url_holidays}?page[number]={page_number}{date_filter}{include_param}", headers=headers)
        
        if response.status_code != 200:
            print(f"Error en la solicitud: {response.status_code}, Detalles: {response.text}")
            break

        data = response.json().get('data', [])
        if not data:
            break

        for row in data:
            attributes = row.get('attributes', {})
            holiday_calendar = None

            if 'holiday_calendar' in row.get('relationships', {}):
                holiday_calendar = row['relationships']['holiday_calendar']['data']


            holidays_data.append({
                'holiday_id': row['id'],
                'holiday_name': attributes.get('name', ''),
                'holiday_date': attributes.get('date', ''),
                'holiday_calendar_id': holiday_calendar.get('id')
            })


        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break
    df = pd.DataFrame(holidays_data)

    datetime_columns = ['holiday_date']
    for col in datetime_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce',utc=True)

    return df