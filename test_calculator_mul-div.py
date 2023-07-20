import pytest
import calculator

#TC0003- For Multiplication
@pytest.mark.parametrize("num1, num2, expected_result", [
    (-3,-2,6),
    (-1,0,0),
    (1,-2,-2),
    (3,4,12),
])

def test_multiply(num1, num2, expected_result):
    assert calculator.multiply(num1, num2) == expected_result

@pytest.mark.parametrize("num1, num2, expected_result", [
    (-3,-2,1.5),
    (-1,0,ZeroDivisionError),
    (1,2,0.5),
    (3,4,0.75),
])

def test_divide(num1, num2, expected_result):
    if expected_result == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            calculator.divide(num1, num2)
    else:
        assert calculator.divide(num1, num2) == expected_result
    
