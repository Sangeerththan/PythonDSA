from datetime import datetime
import calendar


def week_day_of_birthday(day, month, year):
    return calendar.day_name[datetime.strptime(f'{month}-{day}-{year}', "%m-%d-%Y").weekday()]


print(week_day_of_birthday(20, 6, 1995))
