import calculator
import pytest

from calculator import *
from pytest import approx

# handles addition
def test_addition():
  assert add(2, 3) == 5

# handles subtraction
def test_subtraction():
  assert subtract(10, 1) == 9

# handles multiplication
def test_multiply():
  assert multiply(1, 10) == 10

# handles division
# DONE: handles zero division 
def test_divide():
  assert divide(1, 0) == "Cannot divide by 0"
  assert divide(10, 3) == 10/3
  assert divide(99,2) == 49.5

# Handles division by a negative number
def test_divide_negative():
  assert divide(10, -2) == -5
  assert divide(-10, -2) == 5
  assert divide(-10, 2) == -5

# Handles division by a positive number
def test_divide_positive():
  assert divide(10, 2) == 5

# Handles division by a floating-point number
def test_divide_float():
  assert divide(10, 3) == 10/3

# Handles division by zero with negative dividend
def test_divide_zero_negative():
  assert divide(-10, 0) == "Cannot divide by 0"

# Handles division by zero with positive dividend
def test_divide_zero_positive():
  assert divide(10, 0) == "Cannot divide by 0"

# Handles division by zero with zero dividend
def test_divide_zero_zero():
  assert divide(0, 0) == "Cannot divide by 0"
  
  
@pytest.mark.parametrize("num1,num2,expectedResult", [(2, 3, 5), (-2, -3, -5), (2, -3, -1)])
def test_param_add(num1, num2, expectedResult):
    result = calculator.add(num1, num2)
    assert result == expectedResult

# Testing Multiply Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(2, 3, 6), (-2, -3, 6), (2, -3, -6)])
def test_Multiply(num1, num2, expectedResult):
    result = calculator.multiply(num1, num2)
    assert result == expectedResult

# Testing Division Calculator Function
@pytest.mark.parametrize("num1,num2,expectedResult", [(21, 3, 7), (-21, -3, 7), (-21, 3, -7)])
def test_Divide(num1, num2, expectedResult):
    result = calculator.divide(num1, num2)
