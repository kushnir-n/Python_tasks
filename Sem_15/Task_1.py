# Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

#Задача 1 с семинара 1
#Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
#Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
#Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. 
#Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

from Exceptions import UserTriangleError
import logging
import argparse

FORMAT = '{levelname} - {asctime} - {funcName} - {lineno}: {msg}'
logging.basicConfig(filename='UserTriangleError.log', filemode='w', encoding='utf-8', level=logging.ERROR, format=FORMAT, style="{")
logger = logging.getLogger(__name__)

def get_triangle_info(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        logger.error(f'Был введен треугольник, в котором одна сторона больше суммы двух других. Треугольника с такими сторонами не существует')
        raise UserTriangleError(value=False)
        
    else: 
        if a != b and b != c and a != c:
            return("Треугольник существует и он разносторонний!")
        elif a == b and a !=c and b != c:
            return("Треугольник существует и он равнобедренный!")
        elif a == b and b == c and a == c:
            return("Треугольник существует и он равносторонний!")
 

if __name__ == '__main__':
    #get_triangle_info(50, 5, 7)
    parser = argparse.ArgumentParser(description='Получаем аргументы из строки')
    parser.add_argument('param', metavar='a b c', type=int, nargs=3)
    args = parser.parse_args()
    print(get_triangle_info(*args.param)) # python Task_1.py 3 числа - для запуска
    