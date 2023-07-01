import pytest
from ForTestMain import get_hexadecimal_string, get_triangle_info

#тесты для задачи 1 с семинара 2
def test_get_hexadecimal_string():
    assert get_hexadecimal_string(2) == 'Ваше число в шестнадцатеричном строковом представлении: 0x2 (проверка: 0x2)', 'Test failed'

def test_value():
    with pytest.raises(ValueError):
        get_hexadecimal_string('два')

#тесты для задачи 1 с семинара 1
def test_no_triangle():
    assert (get_triangle_info(50, 7, 9) == 'Треугольника с такими сторонами не существует', "Test failed")

def test_isosceles_triangle():
    assert (get_triangle_info(5, 5, 5) == 'Треугольник существует и он равнобедренный!', "Test failed")
    
def test_type():
    with pytest.raises(TypeError):
        get_triangle_info('три', 5, 3)


if __name__ == '__main__':
    pytest.main()