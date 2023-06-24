# Задача 3
# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше. 
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from random import randint

__all__ = ['gen_ferz_coordinates']

def gen_ferz_coordinates(*args):
    board = []
    for i in range(8):
        board.append(randint(1, 8))
    return board


if __name__ == '__main__':
    print(gen_ferz_coordinates())


