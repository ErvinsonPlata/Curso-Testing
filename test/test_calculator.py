import unittest

from src.calculator import sum, subtract, mutiply, divide


class CalculatorTests(unittest.TestCase):  # clase de unittest

    def test_sum(self):
        assert sum(2, 3) == 5

    def test_subtract(self):
        assert subtract(10, 5) == 5

    def test_mutiply(self):
        assert mutiply(10, 5) == 50

    def divide(self):
        assert divide(10, 2) == 5

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(30, 0)


# Comando para correr las pruebas "python -m unittest"
# Comando para correr las pruebas cuadno no se esta en la misma carpeta que el archivo python -m unittest discover -v -s test, con -v se muestra ams clara los test que se estan haciendo
