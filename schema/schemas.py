from google.cloud import bigquery

class Esquema(object):
    schema_people = [
        bigquery.SchemaField("person_id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("person", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("first_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("last_name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("manager_id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("email", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("last_seen_at", "DATETIME", mode="NULLABLE"), #Datetime
        bigquery.SchemaField("title", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("legajo", "STRING", mode="NULLABLE"),
    ]

    schema_time_report = [
        bigquery.SchemaField("person_id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("capacity_", "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField("available", "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField("scheduled", "INTEGER", mode="NULLABLE"),
         bigquery.SchemaField("worked", "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField("billable", "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField("date_", "DATETIME", mode="NULLABLE"), #Datetime
        bigquery.SchemaField("time_report_id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("id_custom_field", "STRING", mode="NULLABLE") 

    ]

    schema_projects = [
        bigquery.SchemaField("project_id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("project_", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("project_type", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("project_manager_id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("last_activity_at", "DATETIME", mode="NULLABLE"),
        bigquery.SchemaField("created_at", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("project_number", "STRING", mode="NULLABLE")
    ]

    schema_services = [
        bigquery.SchemaField('deal_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('service_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('service', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('worked_time', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('unapproved_time', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('billable_time', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('budgeted_time', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('budget_total', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('budget_used', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('profit', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('work_cost_normalized', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('price', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('revenue', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('discount_amount', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('markup_amomunt', "FLOAT", mode="NULLABLE")

    ]

    schema_time_entries = [
        bigquery.SchemaField('time_entry_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('date_', "DATETIME", mode="NULLABLE"), 
        bigquery.SchemaField('worked_time', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('billable_time', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('person_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('service_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('note', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('approver_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('approved', "BOOLEAN", mode="NULLABLE"),
        bigquery.SchemaField('jira_worklog_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('jira_issue_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('jira_organization', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('jira_issue_status', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('jira_issue_summary', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('cost', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('overhead_cost', "INTEGER", mode="NULLABLE")
    ]

    schema_deals = [
        bigquery.SchemaField('deal_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('deal_name', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('date_', "DATETIME", mode="NULLABLE"),
        bigquery.SchemaField('end_date', "DATETIME", mode="NULLABLE"),
        bigquery.SchemaField('budgeted_time', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('worked_time', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('delivered_on', "DATETIME", mode="NULLABLE"),
        bigquery.SchemaField('budget_total', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('budget_used', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('project_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('revenue', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('cost', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('profit', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('responsible_id', "STRING", mode="NULLABLE")
    ]
    
    schema_bookings = [
        bigquery.SchemaField('booking_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('started_on', "DATETIME", mode="NULLABLE"),
        bigquery.SchemaField('note', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('ended_on', "DATETIME", mode="NULLABLE"),
        bigquery.SchemaField('total_working_days', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('total_time', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('person_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('service_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('event_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('percentage', "INTEGER", mode="NULLABLE"),
    ]

    schema_events = [
        bigquery.SchemaField('event_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('event_name', "STRING", mode="NULLABLE")
    ]

    schema_salaries = [
        bigquery.SchemaField('salary_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('exchange_date', "DATE", mode="NULLABLE"),
        bigquery.SchemaField('exchange_rate', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('hours', "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField('started_on', "DATE", mode="NULLABLE"),
        bigquery.SchemaField('currency', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('cost', "INTEGER", mode="NULLABLE"),
        bigquery.SchemaField('holiday_calendar_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('person_id', "STRING", mode="NULLABLE")
    ]


    schema_holiday_calendars = [
        bigquery.SchemaField('holiday_calendar_id', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('pais', "STRING", mode="NULLABLE"),
        bigquery.SchemaField('country', "STRING", mode="NULLABLE")

    ]
    schema_holidays = [
                bigquery.SchemaField('holiday_id', "STRING", mode="NULLABLE"),
                bigquery.SchemaField('holiday_name', "STRING", mode="NULLABLE"),
                bigquery.SchemaField('holiday_date', "DATE", mode="NULLABLE"),
                bigquery.SchemaField('holiday_calendar_id', "STRING", mode="NULLABLE")
    ]