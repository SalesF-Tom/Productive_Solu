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

url_people = dic_endpoints['url_people']



def get_people(start_date=None):
    people_data = []
    page_number = 1
    date_filter = ""
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  

    while True:
        response = requests.get(f"{url_people}?page[number]={page_number}{date_filter}", headers=headers)
        
        if response.status_code != 200:
            print(f"Error en la solicitud: {response.status_code}, Detalles: {response.text}")
            break

        data = response.json().get('data', [])
        if not data:
            break

        for row in data:
            attributes = row.get('attributes', {})
            custom_fields = attributes.get('custom_fields', None)
            people_data.append({
                'person_id': row['id'],
                'first_name': attributes.get('first_name', ''),
                'last_name': attributes.get('last_name', ''),
                'last_seen_at': attributes.get('last_seen_at', None),
                'manager_id': attributes.get('manager_id', ''),
                'email': attributes.get('email', ''),
                'title': attributes.get('title', ''),
                'legajo': (custom_fields or {}).get("82238", None)
            })

        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break
    df = pd.DataFrame(people_data)
    df['person'] = df['first_name'] + ' ' + df['last_name']

    datetime_columns = ['last_seen_at']
    for col in datetime_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce',utc=True)
    
    return df