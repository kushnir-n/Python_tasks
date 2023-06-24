""" 
Задача 1
# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.
"""

__all__ = ['check_date']

import datetime
from sys import argv

def check_date(date: str):
    day,month,year = date.split(".")
    dateIsValid = True
    try: 
        datetime.datetime(int(year), int(month), int(day))
    except:
        dateIsValid = False
    return dateIsValid

def _check_leap(year: int):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print("Год високосный")
    else:
        print("Год не високосный")

if __name__ == '__main__':
    #проверка_1 при вводе только даты
    #date = input("Введите дату в формате DD.MM.YYYY: ")
    #if check_date(date):
        #print(check_date(date))
        #_check_leap(int(date.split(".")[2]))
    #else:
        #exit()

    #проверка даты при вводе python check_date.py дата
    print(check_date(argv[1]))
   
 