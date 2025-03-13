import requests
import pandas as pd
import os
from dotenv import load_dotenv
# from endpoints import dic_endpoints
from funciones.endpoints import dic_endpoints
load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
organization_id = os.getenv("X_ORGANIZATION_ID")

headers = {
    "Content-Type": "application/vnd.api+json; charset=utf-8",
    "X-Auth-Token": access_token,
    "X-Organization-Id": organization_id
}

url_events = dic_endpoints['url_events']

def get_events(start_date=None, end_date=None):
    events_data = []
    page_number = 1    
    date_filter = ""
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  
    if end_date:
        date_filter += f"&filter[updated_at][lt_eq]={end_date}"

    while True:
        response = requests.get(f"{url_events}?page[number]={page_number}{date_filter}", headers=headers)
        
        if response.status_code != 200:
            print(f"Error en la solicitud: {response.status_code}")
            break

        data = response.json().get('data', [])
        if not data:
            break

        for row in data:
            attributes = row.get('attributes', {})
                
            events_data.append({
                'event_id': row['id'],
                'event_name': attributes.get('name', '')
            })

        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break
    df = pd.DataFrame(events_data)
    return df