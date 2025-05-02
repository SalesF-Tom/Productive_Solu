# transformer.py

import pandas as pd

def clean_generic(df):
    return df if not df.empty else pd.DataFrame()

def clean_people(df):
    if df.empty:
        return df
    df = df[df["person_id"].notnull()]
    df["person"] = df["first_name"].fillna("") + " " + df["last_name"].fillna("")
    return df

def clean_projects(df):
    if df.empty:
        return df
    df = df[df["project_id"].notnull()]
    return df

def clean_services(df):
    if df.empty:
        return df
    df = df[df["service_id"].notnull()]
    return df

def clean_time_entries(df):
    if df.empty:
        return df
    df = df[df["time_entry_id"].notnull()]
    df["note"] = df["note"].fillna("")
    return df

def clean_time_reports(df):
    if df.empty:
        return df
    df = df[df["time_report_id"].notnull()]
    return df

def clean_deals(df):
    if df.empty:
        return df
    df = df[df["deal_id"].notnull()]
    return df

def clean_bookings(df):
    if df.empty:
        return df
    df = df[df["booking_id"].notnull()]
    return df

def clean_events(df):
    if df.empty:
        return df
    df = df[df["event_id"].notnull()]
    return df

def clean_salaries(df):
    if df.empty:
        return df
    df = df[df["salary_id"].notnull()]
    return df

def clean_holiday_calendars(df):
    if df.empty:
        return df
    df = df[df["holiday_calendar_id"].notnull()]
    return df

def clean_holidays(df):
    if df.empty:
        return df
    df = df[df["holiday_id"].notnull()]
    return df
