# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv


class Names:
    """Дескриптор для ФИО: проверка ФИО на первую заглавную букву и наличие только букв."""

    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value:str):
        if value.istitle() == False:
            raise ValueError(f'Значение {value} должно начинаться с заглавной буквы.')
        if value.isalpha() == False:
            raise ValueError(f'Значение {value} должно содержать только буквы.')


class Subjects:
    """Дескриптор для предметов: названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы."""

    def __init__(self, param):
        self.param = param

    def __set_name__(self, owner, name):
        self.param_name = '_' + name
    
    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value:str):
        data = []
        with open('subjects.csv', 'r', newline='', encoding='utf-8') as f:
            csv_file = csv.reader(f)
            for line in csv_file:
                data.append(''.join(line)) 
                    
            if value not in data: 
                raise ValueError(f'Значения {value} нет в утвержденном списке предметов.')
            

class Grades:
    """Дескриптор для оценок: для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100)."""

    def __init__(self, min_value: int=None, max_value: int=None):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.param_name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)
    
    def validate(self, value:int):
        if not isinstance(value, int):
            raise TypeError(f'Значение {value} должно быть целым числом.')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'Значение {value} должно быть больше или равно {self.min_value}. Допустимый диапазон оценок: от 2 до 5.')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'Значение {value} должно быть меньше {self.max_value}. Допустимый диапазон результатов теста: от 0 до 100.')

        
class Student:
    first_name = Names(str)
    patronymic_name = Names(str)
    last_name = Names(str)
    grade = Grades(2, 5)
    test_res = Grades(0, 100)
    subject = Subjects(str)

    def __init__(self, first_name, last_name, patronymic_name, subject, grade, test_res):
        self.first_name = first_name
        self.patronymic_name = patronymic_name
        self.last_name = last_name
        self.subject = subject
        self.grade = grade
        self.test_res = test_res
        
    def __str__(self) -> str:
        return f'Экземпляр класса Student {self.first_name} {self.last_name} {self.patronymic_name}: предмет {self.subject}, оценка {self.grade}, результат теста {self.test_res}.'

if __name__ == '__main__':
    #для теста необходимо сохранить файл subjects.csv
    student_test = Student('Наталья', 'Андреевна', 'Кушнир', 'Русский', 5, 100)
    print(student_test)