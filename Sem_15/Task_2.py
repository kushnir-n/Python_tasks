#Задача 2 с семинара 1
#Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
#Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
#Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

from Exceptions import UserNumberError
import logging
import argparse

FORMAT = '{levelname} - {asctime} - {funcName} - {lineno}: {msg}'
logging.basicConfig(filename='UserNumberError.log', filemode='w', encoding='utf-8', level=logging.ERROR, format=FORMAT, style="{")
logger = logging.getLogger(__name__)

def check_number(n):
    max_limit = 100000
    count = 0
    if n < 0 or n > max_limit:
        logger.error(f'Было введено отрицательное число или число больше 100 тыс')
        raise UserNumberError(value=True)
    else:  
        for i in range(2, n // 2 + 1):  
            if n % i == 0:
                count += 1
        if count <= 0:
            print("Число является простым")
        else:
            print("Число является составным")


if __name__ == '__main__':
    #check_number(73)
    parser = argparse.ArgumentParser(description='Получаем аргументы из строки')
    parser.add_argument('param', metavar='num', type=int, nargs=1)
    args = parser.parse_args()
    print(check_number(*args.param)) # python Task_2.py число - для запуска
    

 