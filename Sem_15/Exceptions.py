
class UserException(Exception):
    pass


class UserNumberError(UserException):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f'Нельзя ввести отрицательное число или число больше 100 тыс'
    

class UserTriangleError(UserException):
    
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f'Нельзя создать треугольник, в котором одна сторона больше суммы двух других. Треугольника с такими сторонами не существует'
    

