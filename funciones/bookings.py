import requests
import pandas as pd
import os
from dotenv import load_dotenv
from funciones.endpoints import dic_endpoints
# from endpoints import dic_endpoints
import time
load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
organization_id = os.getenv("X_ORGANIZATION_ID")

headers = {
    "Content-Type": "application/vnd.api+json; charset=utf-8",
    "X-Auth-Token": access_token,
    "X-Organization-Id": organization_id
}


url_bookings = dic_endpoints['url_bookings']   

def get_bookings(start_date=None,end_date=None):
    bookings_data=[]
    page_number = 1  

    date_filter = ""
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  
    if end_date:
        date_filter += f"&filter[updated_at][lt_eq]={end_date}"
    include_param = "&include=person,service,event" 

    while True:
        response = requests.get(f"{url_bookings}?page[number]={page_number}{date_filter}{include_param}", headers=headers, timeout=None)
        retries = 0 

        if response.status_code != 200:
            print(f"Error en la solicitud: {response.status_code}")
            break

        if response.status_code == 429:  
                retries += 1
                wait_time = 2 ** retries  
                print(f"Error 429: esperando {wait_time} segundos antes de reintentar...")
                time.sleep(wait_time)
                if retries > 5:
                    print(f"No se pudo completar la solicitud.")
                    break
                continue  
        retries = 0 

        data = response.json().get('data',[])
        if not data:
            break

        for row in data:
            attributes = row.get('attributes',{})
            person = None
            service = None
            event= None

            if 'person' in row.get('relationships', {}):
                person = row['relationships']['person']['data']
            if 'service' in row.get('relationships', {}):
                service = row['relationships']['service']['data']
            if 'event' in row.get('relationships', {}):
                event = row['relationships']['event']['data']

            bookings_data.append({
                'booking_id':row['id'],
                'started_on': attributes.get('started_on'),
                'note': attributes.get('note'),
                'ended_on': attributes.get('ended_on'),
                'total_working_days': attributes.get('total_working_days'),
                'total_time': attributes.get('total_time'),
                'percentage': attributes.get('percentage'),
                'person_id': person.get('id') if person else None,
                'service_id': service.get('id') if service else "Time_Off",
                'event_id': event.get('id') if event else None
                # booking_id,started_on,note,ended_on,total_working_days,total_time,person_id,service_id,event_id, percentage
            })

        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break

    df = pd.DataFrame(bookings_data)

    datetime_columns = ['started_on', 'ended_on']
    for col in datetime_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce',utc=True)
    
    return df

