# Задача 2
# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

__all__ = ['get_coordinates', 'check_battle']

from chess_func import gen_ferz_coordinates

BOARD_LENGTH = 8
x = []
y = []

def get_coordinates(n: int):
    print("Введите координаты x и y через пробел", BOARD_LENGTH, "раз. После ввода пары, нажимай enter")
    for i in range(n):
        new_x, new_y = [int(n) for n in input().split()]
        x.append(new_x)
        y.append(new_y)

def check_battle(n: int, x: list, y: list):
    battle = True
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                battle = False
    return battle


if __name__ == "__main__":
    #проверка_1 для текущего модуля
    get_coordinates(BOARD_LENGTH)
    print(check_battle(BOARD_LENGTH, x, y))

    #проверка_2 для модуля с импортированной функцией
    # x = gen_ferz_coordinates()
    # y = gen_ferz_coordinates()
    # print(x, y)
    # print(check_battle(BOARD_LENGTH, x, y))
    # result = check_battle(BOARD_LENGTH, x, y)
    # while (not result):
    #     x = gen_ferz_coordinates()
    #     y = gen_ferz_coordinates()
    #     print(x, y)
    #     result = check_battle(BOARD_LENGTH, x, y)