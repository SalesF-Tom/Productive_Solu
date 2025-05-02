from productive.funciones.people import get_people
from productive.funciones.projects import get_projects
from productive.funciones.services import get_services
from productive.funciones.time_entries import get_time_entries
from productive.funciones.time_reports import get_time_report
from productive.funciones.deals import get_deals
from productive.funciones.bookings import get_bookings
from productive.funciones.events import get_events
from productive.funciones.salaries import get_salaries
from productive.funciones.holiday_calendars import get_holiday_calendars
from productive.funciones.holidays import get_holidays

def extract_people(**kwargs):
    return get_people(**kwargs)

def extract_projects(**kwargs):
    return get_projects(**kwargs)

def extract_services(**kwargs):
    return get_services(**kwargs)

def extract_time_entries(**kwargs):
    return get_time_entries(**kwargs)

def extract_time_reports(**kwargs):
    return get_time_report(**kwargs)

def extract_deals(**kwargs):
    return get_deals(**kwargs)

def extract_bookings(**kwargs):
    return get_bookings(**kwargs)

def extract_events(**kwargs):
    return get_events(**kwargs)

def extract_salaries(**kwargs):
    return get_salaries(**kwargs)

def extract_holiday_calendars(**kwargs):
    return get_holiday_calendars(**kwargs)

def extract_holidays(**kwargs):
    return get_holidays(**kwargs)
