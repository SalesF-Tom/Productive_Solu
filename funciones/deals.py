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

url_deals = dic_endpoints['url_deals']

def get_deals(start_date=None, end_date=None):
    deal_data = []
    page_number = 1    
    include_param = '&include=project,responsible'
    date_filter = ""
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  
    if end_date:
        date_filter += f"&filter[updated_at][lt_eq]={end_date}"

    while True:
        response = requests.get(f"{url_deals}?page[number]={page_number}{include_param}{date_filter}", headers=headers)
        
        if response.status_code != 200:
            print(f"Error en la solicitud: {response.status_code}")
            break

        data = response.json().get('data', [])
        if not data:
            break

        for row in data:
            attributes = row.get('attributes', {})
            project=None
            responsible=None

            if 'project' in row.get('relationships', {}):
                project = row['relationships']['project']['data']
            if 'responsible' in row.get('relationships', {}):
                responsible = row['relationships']['responsible']['data']
                
            deal_data.append({
                'deal_id': row['id'],
                'deal_name': attributes.get('name', ''),
                'date_': attributes.get('date',''),
                'end_date': attributes.get('end_date',''),
                'budgeted_time': attributes.get('budgeted_time',''),
                'worked_time': attributes.get('worked_time',''),
                'delivered_on': attributes.get('delivered_on',''),
                'budget_total': attributes.get('budget_total',''),
                'budget_used': attributes.get('budget_used',''),
                'revenue': attributes.get('budget_used',''),
                'cost': attributes.get('budget_used',''),
                'profit': attributes.get('budget_used',''),
                'responsible_id': responsible.get('id') if responsible else None,
                'project_id': project.get('id') if project else None
            })

        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break
    df = pd.DataFrame(deal_data)

    datetime_columns = ['date_', 'end_date', 'delivered_on']
    for col in datetime_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce', utc=True)

    return df