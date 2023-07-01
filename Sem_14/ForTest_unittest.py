import unittest
from ForTestMain import get_hexadecimal_string, get_triangle_info

#тесты для задачи 1 с семинара 2
class TestGetHexadecimalString(unittest.TestCase):
    
    def test_is_hexadecimal_string(self):
        self.assertEqual(get_hexadecimal_string(2), "Ваше число в шестнадцатеричном строковом представлении: 0x2 (проверка: 0x2)", msg="Test failed")
    
    def test_value(self):
        with self.assertRaises(ValueError):
            get_hexadecimal_string('два')

#тесты для задачи 1 с семинара 1
class TestGetTriangleInfo(unittest.TestCase):
    
    def test_no_triangle(self):
        self.assertEqual(get_triangle_info(50, 7, 9), 'Треугольника с такими сторонами не существует', msg="Test failed")

    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_info(5, 5, 5), 'Треугольник существует и он равносторонний!', msg="Test failed")
    
    def test_type(self):
        with self.assertRaises(TypeError):
            get_triangle_info('один', 2, 3)


if __name__ == '__main__':
    unittest.main()