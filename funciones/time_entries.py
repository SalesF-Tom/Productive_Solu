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

url_time_entries = dic_endpoints['url_time_entries']

def get_time_entries(start_date=None,end_date=None):
    time_entries_data=[]
    page_number = 1  

    date_filter = ""
    if start_date:
        date_filter += f"&filter[updated_at][gt_eq]={start_date}"  
    if end_date:
        date_filter += f"&filter[updated_at][lt_eq]={end_date}"
    include_param = "&include=person,service,approver" 

    while True:
        response = requests.get(f"{url_time_entries}?page[number]={page_number}{date_filter}{include_param}", headers=headers, timeout=None)
        retries = 0 

        if response.status_code != 200:
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
            approver = None

            if 'person' in row.get('relationships', {}):
                person = row['relationships']['person']['data']
            if 'service' in row.get('relationships', {}):
                service = row['relationships']['service']['data']
            if 'approver' in row.get('relationships',{}):
                approver = row['relationships']['approver']["data"]

            time_entries_data.append({
                'time_entry_id':row['id'],
                'date_': attributes.get('date'),
                'worked_time': attributes.get('time'),
                'billable_time': attributes.get('billable_time'),
                'note': attributes.get('note'),
                'approved': attributes.get('approved'),
                'approved_at': attributes.get('approved_at'),
                'updated_at': attributes.get('updated_at'),
                'jira_worklog_id': attributes.get('jira_worklog_id'),
                'jira_issue_id': attributes.get('jira_issue_id'),
                'jira_organization': attributes.get('jira_organization'),
                'jira_issue_status': attributes.get('jira_issue_status'),
                'jira_issue_summary': attributes.get('jira_issue_summary'),
                'cost': attributes.get('cost'),
                'overhead_cost': attributes.get('overhead_cost'),
                'person_id': person.get('id') if person else None,
                'service_id': service.get('id') if service else None,
                'approver_id': approver.get('id') if approver else None
            })

        if response.json()["meta"]["current_page"] < response.json()["meta"]["total_pages"]:
            page_number += 1
        else:
            break
    df = pd.DataFrame(time_entries_data)

    datetime_columns = ['date_']
    for col in datetime_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce', utc=True)

    return df