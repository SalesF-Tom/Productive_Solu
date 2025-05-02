from productive.extractor import (
    extract_people,
    extract_projects,
    extract_services,
    extract_time_entries,
    extract_time_reports,
    extract_deals,
    extract_bookings,
    extract_events,
    extract_salaries,
    extract_holiday_calendars,
    extract_holidays
)

from productive.transformer import (
    clean_people,
    clean_projects,
    clean_services,
    clean_time_entries,
    clean_time_reports,
    clean_deals,
    clean_bookings,
    clean_events,
    clean_salaries,
    clean_holiday_calendars,
    clean_holidays,
)

from schema.schemas import Esquema
from bigquery.querys import (
    Merge_Data_People_BQ,
    Merge_Data_Projects_BQ,
    Merge_Data_Services_BQ,
    Merge_Data_Time_Entries_BQ,
    Merge_Data_Time_Reports_BQ,
    Merge_Data_Deals_BQ,
    Merge_Data_Bookings_BQ,
    Merge_Data_Events_BQ,
    Merge_Data_Salaries_BQ,
    Merge_Data_Holiday_Calendars_BQ,
    Merge_Data_Holidays_BQ
)

ENTIDADES = {
    'people': {
        'getter': extract_people,
        'transform': clean_people,
        'schema': Esquema.schema_people,
        'table': 'tbl_productive_people',
        'merge': Merge_Data_People_BQ,
        'usa_fecha': False
    },
    'projects': {
        'getter': extract_projects,
        'transform': clean_projects,
        'schema': Esquema.schema_projects,
        'table': 'tbl_productive_projects',
        'merge': Merge_Data_Projects_BQ,
        'usa_fecha': False
    },
    'services': {
        'getter': extract_services,
        'transform': clean_services,
        'schema': Esquema.schema_services,
        'table': 'tbl_productive_services',
        'merge': Merge_Data_Services_BQ,
        'usa_fecha': False
    },
    'time_entries': {
        'getter': extract_time_entries,
        'transform': clean_time_entries,
        'schema': Esquema.schema_time_entries,
        'table': 'tbl_productive_time_entries',
        'merge': Merge_Data_Time_Entries_BQ,
        'usa_fecha': True
    },
    'time_reports': {
        'getter': extract_time_reports,
        'transform': clean_time_reports,
        'schema': Esquema.schema_time_report,
        'table': 'tbl_productive_time_reports',
        'merge': Merge_Data_Time_Reports_BQ,
        'usa_fecha': True
    },
    'deals': {
        'getter': extract_deals,
        'transform': clean_deals,
        'schema': Esquema.schema_deals,
        'table': 'tbl_productive_deals',
        'merge': Merge_Data_Deals_BQ,
        'usa_fecha': False
    },
    'bookings': {
        'getter': extract_bookings,
        'transform': clean_bookings,
        'schema': Esquema.schema_bookings,
        'table': 'tbl_productive_bookings',
        'merge': Merge_Data_Bookings_BQ,
        'usa_fecha': True
    },
    'events': {
        'getter': extract_events,
        'transform': clean_events,
        'schema': Esquema.schema_events,
        'table': 'tbl_productive_events',
        'merge': Merge_Data_Events_BQ,
        'usa_fecha': False
    },
    'salaries': {
        'getter': extract_salaries,
        'transform': clean_salaries,
        'schema': Esquema.schema_salaries,
        'table': 'tbl_productive_salaries',
        'merge': Merge_Data_Salaries_BQ,
        'usa_fecha': True
    },
    'holiday_calendars': {
        'getter': extract_holiday_calendars,
        'transform': clean_holiday_calendars,
        'schema': Esquema.schema_holiday_calendars,
        'table': 'tbl_productive_holiday_calendars',
        'merge': Merge_Data_Holiday_Calendars_BQ,
        'usa_fecha': False
    },
    'holidays': {
        'getter': extract_holidays,
        'transform': clean_holidays,
        'schema': Esquema.schema_holidays,
        'table': 'tbl_productive_holidays',
        'merge': Merge_Data_Holidays_BQ,
        'usa_fecha': False
    }
}
