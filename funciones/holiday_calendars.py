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

url_holiday_calendars = dic_endpoints['url_holiday_calendars']



def get_holiday_calendars(start_date=None):
    holiday_calendar_data = []
    page_number = 1
    date_filter = ""
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  

    while True:
        response = requests.get(f"{url_holiday_calendars}?page[number]={page_number}{date_filter}", headers=headers)
        
        if response.status_code != 200:
            print(f"Error en la solicitud: {response.status_code}, Detalles: {response.text}")
            break

        data = response.json().get('data', [])
        if not data:
            break

        for row in data:
            attributes = row.get('attributes', {})

            holiday_calendar_data.append({
                'holiday_calendar_id': row['id'],
                'pais': attributes.get('name', ''),
                'country': attributes.get('country', '')
            })

        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break
    df = pd.DataFrame(holiday_calendar_data)
    
    return df