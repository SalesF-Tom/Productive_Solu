import requests
import pandas as pd
import os
from dotenv import load_dotenv
from funciones.endpoints import dic_endpoints
load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")
organization_id = os.getenv("X_ORGANIZATION_ID")

headers = {
    "Content-Type": "application/vnd.api+json; charset=utf-8",
    "X-Auth-Token": access_token,
    "X-Organization-Id": organization_id
}

url_projects = dic_endpoints['url_projects']


def get_projects(start_date=None,end_date=None):
    projects_data  = []
    page_number  = 1
    include_param = "&include=project_manager"
    date_filter = ""
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  
    if end_date:
        date_filter += f"&filter[updated_at][lt_eq]={end_date}"

    while True:
        response = requests.get(f"{url_projects}?page[number]={page_number}{include_param}{date_filter}", headers=headers)
        
        if response.status_code != 200:
            print(f"Error en la solicitud: {response.status_code}")
            break

        data = response.json().get('data',[])
        if not data:
            break
        
        tipo=None

        for row in data:
            attributes = row.get('attributes',{})
            project = None
            if 'project_manager' in row.get('relationships', {}):
                project = row['relationships']['project_manager']['data']

            if 'Mantenimiento' in attributes.get('name',''):
                tipo = 'Mantenimiento'
            else: 
                tipo = 'Implementación'
            projects_data.append({
                'project_id': row['id'],
                'project_': attributes.get('name',''),
                'last_activity_at': attributes.get('last_activity_at',''),
                'created_at': attributes.get('created_at',''),
                'project_number': attributes.get('number',''),
                'project_type': tipo,
                'project_manager_id': project.get('id') if project else None
            })

        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break
    df = pd.DataFrame(projects_data)

    datetime_columns = ['last_activity_at']
    for col in datetime_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce',utc=True)

    return df