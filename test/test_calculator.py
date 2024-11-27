import unittest

from src.calculator import sum, subtract, multiply, divide


class CalculatorTests(unittest.TestCase):  # clase de inittest

    def test_sum(self):
        assert sum(2, 3) == 5

    def test_subtract(self):
        assert subtract(10, 5) == 5

    def test_multiply(self):
        assert multiply(3, 2) == 6

    def test_divide(self):
        result = divide(10, 2)
        expected = 5
        assert result == expected


# Comando para correr las pruebas "python -m unittest"
# Comando para correr las pruebas cuadno no se esta en la misma carpeta que el archivo python -m unittest discover -v -s test, con -v se muestra ams clara los test que se estan haciendo
