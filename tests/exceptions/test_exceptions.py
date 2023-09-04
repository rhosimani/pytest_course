import pytest

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b

def test_exception():
    a = 0
    b = 10
    with pytest.raises(ZeroDivisionError):
        c = b / a

def test_divide():
    with pytest.raises(ValueError) as exception_info:
        divide(10,0)
    assert str(exception_info.value) == 'Cannot divide by zero'

def test_recursion_depth():
    with pytest.raises(RuntimeError) as exception_info:
        def f():
            f()
        f()
    assert "maximum recursion" in str(exception_info.value)