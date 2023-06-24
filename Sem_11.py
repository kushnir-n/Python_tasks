#Задания с семинара + дз

# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

# Задание №1
# Создайте класс Моя Строка, где: будут доступны все возможности str, дополнительно хранятся имя автора строки и время создания (time.time)
# Задание №2
# Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару 
# списковархивов list-архивы также являются свойствами экземпляра
# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.
# Задание №4
# Доработаем класс Архив из задачи 2. Добавьте методы представления экземпляра для программиста и для пользователя.
# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания. При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину. При вычитании не допускайте отрицательных значений.
# Задание №6
# Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади Должны работать все шесть операций сравнения

import time


class MyString(str):
    """Класс, где доступны все возможности str и дополнительно хранятся имя автора строки и время создания (time.time)."""

    def __new__(cls, text: str, author: str):
        """Метод добавляет параметры: автора строки и время создания в класс str."""
        instance = super().__new__(cls, text) 
        instance.author = author
        instance.time = time.time()
        return instance
    
    def __str__(self) -> str:
        return f'Экземпляр класса MyString добавляет автора строки и время создания.'
    
    def __repr__(self) -> str:
        return f'MyString({self.author=})'
    
class Archive:
    """Класс хранит число и строку. При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков архивов list-архивы также являются свойствами экземпляра."""
    _archive = None

    def __init__(self, number: int, text: str):
        """Метод добавляет параметры: число и строку."""
        self.number = number
        self.text = text

    def __new__(cls, *args, **kwargs):
        """Метод добавляет число и строку в архив."""
        if cls._archive is None:
            cls._archive = super().__new__(cls)
            cls._archive.num = []
            cls._archive.val = []
        else:
            cls._archive.num.append(cls._archive.number)
            cls._archive.val.append(cls._archive.text)
        return cls._archive
    
    def __str__(self) -> str:
        return f'Экземпляр класса Archive с числом {self.number} и строкой {self.text}.'

    def __repr__(self) -> str:
        return f'Archive ({self.number=}, {self.text=})'

class Rectangle:
    """Класс вычисляет периметр и площадь прямоугольника; складывает и вычитает периметры."""
    def __init__(self, side_a, side_b = None):
        """Метод добавляет параметры side_a и side_b, если добавляется только одит параметр, считаем, что side_a и side_b равны."""
        self.a = side_a
        if side_b is None:
            self.b = side_a
        else:
            self.b = side_b

    def rectangle_long(self):
        """Метод вычисляет периметр прямоугольника."""
        long = (self.a + self.b) * 2
        return long
    
    def rectangle_square(self):
        """Метод вычисляет площадь прямоугольника."""
        square = self.a * self.b 
        return square
    
    def __add__(self, other):
        """Метод складывает периметры прямоугольников."""
        a = self.a + other.a
        b = self.b + other.b
        return Rectangle(a, b)

    def __sub__(self, other):
        """Метод вычитает периметры прямоугольников."""
        if self.rectangle_long() < other.rectangle_long():
            self, other = other, self
        a = self.a - other.a
        b = self.b - other.b
        return Rectangle(a, b)
    
    def __str__(self) -> str:
        return f'Экземпляр класса Rectangle со сторонами {self.a} и {self.b}'
    
    def __repr__(self) -> str:
        return f'Rectangle({self.a=},{self.b=})'

# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения

class Matrix: 

    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def show_matrix(self):
        mat = ""
        for i in range(len(self.matrix)):
            mat = mat + '\t'.join(map(str,self.matrix[i])) + "\n"
        return mat
    
    def comparison_matrix(self, other):
        result = ""
        if self.matrix < other.matrix: result = "Вторая матрица больше первой"
        elif self.matrix > other.matrix: result = "Первая матрица больше второй"
        else: result = "Матрицы равны"
        return result

    def __add__(self, other):
        result = []
        nums = []
        for i in range(len(self.matrix)): 
            for j in range(len(self.matrix[i])):
                summa = self.matrix[i][j] + other.matrix[i][j]
                nums.append(summa)
                if len(nums) == len(self.matrix[i]):
                    result.append(nums)
                    nums = []
        return result


if __name__ == "__main__":

#тестируем методы вывода строк документации на печать в классах MyString, Archive, Rectangle
    test1 = MyString("text example", "author example")
    print(test1)
    print(f'{test1 = }')
    help(MyString)

    test2 = Archive(2, "text example")
    print(test2)
    print(f'{test2 = }')
    help(Archive)

    test3 = Rectangle(10, 3)
    print(test3)
    print(f'{test3 = }')
    help(Rectangle)

#тестируем методы класса Matrix
    mat_1 = Matrix([[1, 2, 2], [3, 4, 4]])
    print(f'\nМатрица 1:\n{mat_1.show_matrix()}')
    mat_2 = Matrix([[5, 6, 6], [7, 8, 8]])
    print(f'Матрица 2:\n{mat_2.show_matrix()}')
    mat_sum = mat_1 + mat_2
    print(f'Сумма 1-й и 2-й матриц:\n{mat_sum}\n')
    mat_3 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    mat_4 = Matrix([[7, 8, 9], [1, 2, 3]])
    mat_compare = mat_4.comparison_matrix(mat_2)
    print(f'Сравнение матриц:\n{mat_compare}')