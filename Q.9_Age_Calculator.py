# Age calculator

import datetime


def find_age(year, month, day):
    today = datetime.date.today()
    dob = datetime.date(year, month, day)
    age = int((today - dob).days/365)
    return age


user_dob = input("Enter your D.O.B. in format of day-month-year: ")

dob = user_dob.split('-')
year, month, day = int(dob[0]), int(dob[1]), int(dob[2])
your_age = find_age(year, month, day)
print(f"you are {your_age} years old.")
