dic_endpoints = {
    'url_people' : 'https://api.productive.io/api/v2/people',
    'url_time_reports' : 'https://api.productive.io/api/v2/reports/time_reports',
    'url_projects' : 'https://api.productive.io/api/v2/projects',
    'url_services' : 'https://api.productive.io/api/v2/services',
    'url_time_entries' : 'https://api.productive.io/api/v2/time_entries',
    'url_deals' : 'https://api.productive.io/api/v2/deals',
    'url_bookings': 'https://api.productive.io/api/v2/bookings',
    'url_events': 'https://api.productive.io/api/v2/events',
    'url_salaries': 'https://api.productive.io/api/v2/salaries',
    'url_holiday_calendars': 'https://api.productive.io/api/v2/holiday_calendars',
    'url_holidays': 'https://api.productive.io/api/v2/holidays',
}

columns = { 
    'services_columns':['deal_id','service_id','service','worked_time','unapproved_time','billable_time','budgeted_time','budget_total','budget_used'],
    'time_entries_columns':['time_entry_id','date_','worked_time','billable_time','person_id','service_id','note','approver_id'],
    'deals_columns':['deal_id','deal','date_','end_date','budgeted_time','worked_time','delivered_on','budget_total','budget_used','project_id','responsible_id']
}

