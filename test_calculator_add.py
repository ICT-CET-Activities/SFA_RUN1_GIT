import pytest
import calculator

#TC0001- For Addition
@pytest.mark.parametrize("num1, num2, expected_result", [
    (-3,-2,-5),
    (-1,0,-1),
    (1,-2,-1),
    (3,4,7),
])

def test_add(num1, num2, expected_result):
    assert calculator.add(num1, num2) == expected_result

@pytest.mark.parametrize("num1, num2, expected_result", [
    (-3,-2,-1),
    (-1,0,-1),
    (1,2,-1),
    (3,4,-1),
])

def test_subtract(num1, num2, expected_result):
    assert calculator.subtract(num1, num2) == expected_result
    
