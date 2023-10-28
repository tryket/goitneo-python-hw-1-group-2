from datetime import datetime, timedelta
from enum import Enum


class UserParams(Enum):
    name = 1
    birthday = 2


users = [
    {UserParams.name: "Bill Gates", UserParams.birthday: datetime(1955, 10, 28)},
    {UserParams.name: "Steve Jobs", UserParams.birthday: datetime(1955, 2, 24)},
]


def get_birthdays_per_week(users):
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    birthday_dict = {day: [] for day in range(7)}
    for user in users:
        name = user[UserParams.name]
        birthday = user[UserParams.birthday]
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - monday).days
        day_of_week = (monday.weekday() + delta_days) % 7
        birthday_dict[day_of_week].append(name)
    for day, names in birthday_dict.items():
        day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][day]
        if names:
            print(f"{day_of_week}: {', '.join(names)}")


get_birthdays_per_week(users)
