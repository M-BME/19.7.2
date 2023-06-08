import pytest
from app.calculator import Calculator


class TestCalc:
   def setup(self):
       self.calc = Calkulator

   def test_multiply_calculate_correctly(self):
       assert self.calc.multiply(self, 2, 2) == 4

   def test_multiply_failed(self):
       assert self.calc.multiply(self, 2, 2) == 5

   def test_zero_divizion(self):
       with pytest.raises(ZeroDivisionError):
           self.calc.division(self, 1, 0)

   def teardown(self):
       print('Выполненеие метода Teardown')