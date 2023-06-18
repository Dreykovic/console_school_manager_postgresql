#!/bin/python3
import datetime

def validate_text(text):
    if text.isalpha():
        return 1
    else:
        return 0


def validate_phone_number(phone_number):
    phone_number = str(phone_number)
    if len(phone_number) == 8:
        if phone_number.isdigit():
            if phone_number[0] in ("9", "7") and phone_number[1] in ("0", "1", "2", "3", "6", "7", "8", "9"):
                return 1
    else:
        return 0


def validate_number(number):
    number = str(number)
    if number.isdigit():
        return 1
    else:
        return 0
def validate_date(my_date):
    date_format = "%Y-%m-%d"
  
    try:
        datetime.datetime.strptime(my_date, date_format)
    except ValueError:
        return 0
    return 1

 





# print(validate_text("dzz"))
# print(validate_number("5"))
print(validate_date("2020-12-20"))
