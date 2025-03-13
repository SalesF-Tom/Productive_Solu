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

url_services = dic_endpoints['url_services']

def get_services(start_date=None,end_date=None):
    service_data=[]
    page_number = 1  

    date_filter = ""
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  
    if end_date:
        date_filter += f"&filter[updated_at][lt_eq]={end_date}"


    include_param = "&include=deal" 

    while True:
        response = requests.get(f"{url_services}?page[number]={page_number}{include_param}{date_filter}", headers=headers)
    
        if response.status_code != 200:
            print(f"Error en la solicitud: {response.status_code}")
            break

        data = response.json().get('data',[])
        if not data:
            break

        for row in data:
            attributes = row.get('attributes',{})
            deal = None
            if 'deal' in row.get('relationships', {}):
                deal = row['relationships']['deal']['data']
            service_data.append({
                'deal_id' : deal.get('id') if deal else None,
                'service_id': row['id'],
                'service':  attributes.get('name',''),
                'worked_time': attributes.get('worked_time'),
                'unapproved_time': attributes.get('worked_time'),
                'billable_time': attributes.get('billable_time'),
                'budgeted_time':attributes.get('budgeted_time'),
                'budget_total':attributes.get('budget_total'),
                'budget_used':attributes.get('budget_used'), 
                'profit':attributes.get('profit'), #
                'work_cost_normalized':attributes.get('work_cost_normalized'), 
                'price':attributes.get('price'), 
                'revenue':attributes.get('revenue'), 
                'discount_amount':attributes.get('discount_amount'), 
                'markup_amomunt':attributes.get('markup_amount')


            })

        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break
    df = pd.DataFrame(service_data)
    return df