from google.cloud import bigquery

def Merge_Data_People_BQ(client, tabla_final, tabla_temp):

    merge_query = f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON A.person_id=B.person_id
        
        WHEN MATCHED THEN
        UPDATE SET
            A.email = B.email,
            A.title = B.title,
            A.last_seen_at = B.last_seen_at,
            A.manager_id = B.manager_id,
            A.legajo = B.legajo
            

        WHEN NOT MATCHED THEN
            INSERT (
                person_id, person, first_name, last_name, email, last_seen_at, title, manager_id, legajo
                )
            VALUES (
                B.person_id, B.person, B.first_name, B.last_name, B.email, B.last_seen_at, B.title, B.manager_id, B.legajo
                )
        """

    # print("QUERY : " , merge_query)
    query_job = client.query(merge_query)
    resultados = list(query_job.result())   
    filas_actualizadas = query_job.num_dml_affected_rows
    
    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Time_Reports_BQ(client, tabla_final, tabla_temp):

    merge_query = f"""
                MERGE `{tabla_final}` as A
                    USING  (SELECT DISTINCT * FROM `{tabla_temp}`) as B
                    ON A.id_custom_field=B.id_custom_field
                    
                    WHEN MATCHED THEN
                    UPDATE SET
                    A.capacity_ = B.capacity_,
                    A.available = B.available,
                    A.scheduled = B.scheduled,
                    A.worked = B.worked,
                    A.billable = B.billable,
                    A.date_ = B.date_,
                    A.time_report_id = B.time_report_id

                    WHEN NOT MATCHED THEN
                        INSERT (
                            person_id, capacity_, available, scheduled, worked, billable, date_, time_report_id, id_custom_field

                            )
                        VALUES (
                            B.person_id, B.capacity_, B.available, B.scheduled, B.worked, B.billable, B.date_, B.time_report_id, B.id_custom_field
                            )
                    """
    
    query_job = client.query(merge_query)
    resultados = list(query_job.result()) 
    filas_actualizadas = query_job.num_dml_affected_rows
    
    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Projects_BQ(client, tabla_final, tabla_temp):
    merge_query = f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON A.project_id = B.project_id
        
        WHEN MATCHED THEN
        UPDATE SET
            A.project_ = B.project_,
            A.project_type = B.project_type,
            A.project_manager_id = B.project_manager_id,
            A.last_activity_at = B.last_activity_at,
            A.created_at = B.created_at, 
            A.project_number = B.project_number

        WHEN NOT MATCHED THEN
        INSERT (
            project_id, project_, project_type, project_manager_id, last_activity_at, created_at, project_number
        )
        VALUES (
            B.project_id, B.project_, B.project_type, B.project_manager_id, B.last_activity_at, B.created_at, B.project_number
        )
    """


    query_job = client.query(merge_query)
    resultados = list(query_job.result())
    filas_actualizadas = query_job.num_dml_affected_rows

    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Services_BQ(client, tabla_final, tabla_temp):
    merge_query = f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON 
            A.service_id = B.service_id

        WHEN MATCHED THEN
        UPDATE SET
            A.deal_id = B.deal_id,
            A.service = B.service,
            A.worked_time = B.worked_time,
            A.unapproved_time = B.unapproved_time,
            A.billable_time = B.billable_time,
            A.budgeted_time = B.budgeted_time,
            A.budget_total = B.budget_total,
            A.budget_used = B.budget_used,
            A.profit = B.profit,
            A.work_cost_normalized = B.work_cost_normalized,
            A.price = B.price,
            A.revenue = B.revenue,
            A.discount_amount = B.discount_amount,
            A.markup_amomunt = B.markup_amomunt

        WHEN NOT MATCHED THEN
        INSERT (
            deal_id, service_id, service, worked_time, unapproved_time, billable_time, budgeted_time, budget_total, budget_used, profit, work_cost_normalized, price, revenue, discount_amount, markup_amomunt
            )
        VALUES (
            B.deal_id,B.service_id,B.service,B.worked_time,B.unapproved_time,B.billable_time,B.budgeted_time,B.budget_total,B.budget_used,B.profit,B.work_cost_normalized,B.price,B.revenue,B.discount_amount,B.markup_amomunt
            ) 
    """
    
    query_job = client.query(merge_query)
    resultados = list(query_job.result())
    filas_actualizadas = query_job.num_dml_affected_rows

    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Time_Entries_BQ(client, tabla_final, tabla_temp):
    merge_query = f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON A.time_entry_id = B.time_entry_id

        WHEN MATCHED THEN
        UPDATE SET
            A.worked_time = B.worked_time,
            A.billable_time = B.billable_time,
            A.note = B.note,
            A.approved = B.approved, 
            A.approved_at = B.approved_at, 
            A.updated_at = B.updated_at, 
            A.jira_worklog_id = B.jira_worklog_id,
            A.jira_issue_id = B.jira_issue_id,
            A.jira_organization = B.jira_organization,
            A.jira_issue_status = B.jira_issue_status,
            A.jira_issue_summary = B.jira_issue_summary,
            A.cost = B.cost, 
            A.overhead_cost = B.overhead_cost,
            A.person_id = B.person_id,
            A.service_id = B.service_id,
            A.approver_id = B.approver_id

        WHEN NOT MATCHED THEN
        INSERT (
            time_entry_id, date_, worked_time, billable_time, note, approved, approved_at, updated_at,
            jira_worklog_id, jira_issue_id, jira_organization, jira_issue_status, jira_issue_summary,
            cost, overhead_cost, person_id, service_id, approver_id
        )
        VALUES (
            B.time_entry_id, B.date_, B.worked_time, B.billable_time, B.note, B.approved, B.approved_at, B.updated_at,
            B.jira_worklog_id, B.jira_issue_id, B.jira_organization, B.jira_issue_status, B.jira_issue_summary,
            B.cost, B.overhead_cost, B.person_id, B.service_id, B.approver_id
        ) 
    """

    print(merge_query)

    query_job = client.query(merge_query)
    resultados = list(query_job.result())
    filas_actualizadas = query_job.num_dml_affected_rows

    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Deals_BQ(client, tabla_final, tabla_temp):
    merge_query =f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON A.deal_id = B.deal_id

        WHEN MATCHED THEN
        UPDATE SET
            A.end_date = B.end_date,
            A.budgeted_time = B.budgeted_time,
            A.worked_time = B.worked_time,
            A.budget_total = B.budget_total,
            A.budget_used = B.budget_used,
            A.responsible_id = B.responsible_id,
            A.revenue = B.revenue,
            A.cost = B.cost,
            A.profit = B.profit

        WHEN NOT MATCHED THEN
        INSERT (
            deal_id, deal_name, date_, end_date, budgeted_time, worked_time, delivered_on, budget_total, budget_used, project_id, responsible_id, revenue, cost, profit
        )
        VALUES (
            B.deal_id, B.deal_name, B.date_, B.end_date, B.budgeted_time, B.worked_time, B.delivered_on, B.budget_total, B.budget_used, B.project_id, B.responsible_id, B.revenue, B.cost, B.profit
        ) 
    """

    query_job = client.query(merge_query)
    resultados = list(query_job.result())
    filas_actualizadas = query_job.num_dml_affected_rows

    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Bookings_BQ(client, tabla_final, tabla_temp):
    merge_query =f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON A.booking_id = B.booking_id

        WHEN MATCHED THEN
        UPDATE SET
            A.started_on = B.started_on,
            A.note = B.note,
            A.ended_on = B.ended_on,
            A.total_working_days = B.total_working_days,
            A.total_time = B.total_time,
            A.person_id = B.person_id,
            A.percentage = B.percentage,
            A.service_id = B.service_id,
            A.event_id = B.event_id

        WHEN NOT MATCHED THEN
        INSERT (
            booking_id,started_on,note,ended_on,total_working_days,total_time,person_id,service_id,event_id, percentage
        )
        VALUES (
            B.booking_id,B.started_on,B.note,B.ended_on,B.total_working_days,B.total_time,B.person_id,B.service_id,B.event_id, B.percentage
        ) 
    """

    query_job = client.query(merge_query)
    resultados = list(query_job.result())
    filas_actualizadas = query_job.num_dml_affected_rows

    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Events_BQ(client, tabla_final, tabla_temp):
    merge_query =f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON A.event_id = B.event_id

        WHEN MATCHED THEN
        UPDATE SET
            A.event_name = B.event_name

        WHEN NOT MATCHED THEN
        INSERT (
            event_id, event_name
        )
        VALUES (
            B.event_id, B.event_name
        ) 
    """

    query_job = client.query(merge_query)
    resultados = list(query_job.result())
    filas_actualizadas = query_job.num_dml_affected_rows

    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Salaries_BQ(client, tabla_final, tabla_temp):
    merge_query =f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON A.salary_id = B.salary_id

        WHEN MATCHED THEN
        UPDATE SET
            A.exchange_date = B.exchange_date,
            A.exchange_rate = B.exchange_rate,
            A.hours = B.hours,
            A.currency = B.currency,
            A.cost = B.cost,
            A.holiday_calendar_id = B.holiday_calendar_id,
            A.person_id = B.person_id


        WHEN NOT MATCHED THEN
        INSERT (
            salary_id, exchange_date, exchange_rate,hours, started_on, currency, cost, holiday_calendar_id, person_id
        )
        VALUES (
            B.salary_id, B.exchange_date, B.exchange_rate,B.hours, B.started_on, B.currency, B.cost, B.holiday_calendar_id, B.person_id
        ) 
    """

    query_job = client.query(merge_query)
    resultados = list(query_job.result())
    filas_actualizadas = query_job.num_dml_affected_rows

    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Holiday_Calendars_BQ(client, tabla_final, tabla_temp):
    merge_query =f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON A.holiday_calendar_id = B.holiday_calendar_id

        WHEN MATCHED THEN
        UPDATE SET
            A.pais = B.pais,
            A.country = B.country

        WHEN NOT MATCHED THEN
        INSERT (
            holiday_calendar_id, pais, country
        )
        VALUES (
            B.holiday_calendar_id, B.pais, B.country 
            ) 
    """

    query_job = client.query(merge_query)
    resultados = list(query_job.result())
    filas_actualizadas = query_job.num_dml_affected_rows

    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")


def Merge_Data_Holidays_BQ(client, tabla_final, tabla_temp):
    merge_query =f"""
        MERGE `{tabla_final}` A
        USING (SELECT DISTINCT * FROM `{tabla_temp}`) B
        ON A.holiday_id = B.holiday_id

        WHEN MATCHED THEN
        UPDATE SET
            A.holiday_name = B.holiday_name,
            A.holiday_date = B.holiday_date,
            A.holiday_calendar_id = B.holiday_calendar_id

        WHEN NOT MATCHED THEN
        INSERT (
            holiday_id,holiday_calendar_id, holiday_name, holiday_date
        )
        VALUES (
            B.holiday_id, B.holiday_calendar_id, B.holiday_name, B.holiday_date
            ) 
    """

    query_job = client.query(merge_query)
    resultados = list(query_job.result())
    filas_actualizadas = query_job.num_dml_affected_rows

    print(f"\033[35m Se actualizaron {filas_actualizadas} a la tabla {tabla_final}. \033[0m")