# calculates how many days are left until the first Monday of the next month

from datetime import datetime, timedelta

def get_days_until_next_salary():
    current_date = datetime.now()

    if current_date.month == 12:
        next_month = 1
        year = current_date.year + 1
    else:
        next_month = current_date.month + 1
        year = current_date.year

    # 2025-02-01 00:00:00
    first_day_of_next_month = datetime(year, next_month, 1)


    # returns (0=Monday, 6=Sunday)
    first_day_weekday = first_day_of_next_month.weekday()

    # Calculate how many days to the next Monday
    if first_day_weekday == 0:
        first_monday = first_day_of_next_month
    else:
        days_to_next_monday = (7 - first_day_weekday) % 7
        first_monday = first_day_of_next_month + timedelta(days=days_to_next_monday + 1)

    # Calculate the number of days left until the first Monday
    days_left = (first_monday - current_date).days

    return days_left


days_until_salary = get_days_until_next_salary()
print(f"days until next salary: {days_until_salary}")
