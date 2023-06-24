# Задача 1
# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

print("Задача #1")

file_path = "D:\Python_hw\File_name.txt"

def file_params(file_path):
    path, file_name = os.path.split(file_path)
    name, file_extension = os.path.splitext(file_name)
    return path, name, file_extension

print ("Вывод кортежа:", file_params(file_path))

# Задача 2
# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с указанием процентов вида «10.25%». 
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

print ("\nЗадача #2")

names, rates, percents = ["Иван", "Семен", "Анна"], [1000, 1500, 2000], ["10.25%", "5.35%", "20.05%"]

def gen_dict_str(list1, list2, list3):
    return dict(zip(list1, [key*float(val.split('%')[0]) for key, val in dict(zip(list2, list3)).items()]))
    
print ("Вывод словаря:", gen_dict_str(names,rates,percents))


# Задача 3
# Создайте функцию генератор чисел Фибоначчи

print ("\nЗадача #3")

num = int(input('Введите число для генерации чисел Фибоначчи: '))

def fibonnachi(n):
    n1, n2 = 0, 1
    for i in range(n):
        yield n1
        n1, n2 = n2, n1 + n2

print ("Вывод чисел Фибоначчи: ", list(fibonnachi(num)))