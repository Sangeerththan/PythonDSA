import calendar
from datetime import datetime


def get_calendar_year(year):
    return calendar.calendar(year)


def get_calendar_month(year, month):
    return calendar.month(year, month)


def get_calendar_week_day(year, month, day):
    return calendar.day_name[datetime.strptime(f'{month}-{day}-{year}', "%m-%d-%Y").weekday()]


print(get_calendar_week_day(2021, 9, 29))
