import pytest

@pytest.mark.parametrize(
    "input_value, expected_value",
    [
        ("3 + 5", 8),
        ("9 - 5", 4),
        ("9 * 3", 27)
    ]
)
def test_eval(input_value, expected_value):
    assert eval(input_value) == expected_value

def fibonacci(n):
    # fibonacci(n) es la sumatoria de los dos valores fibonacci(n-2) + fibonacci(n - 1) y ademas por definición fibonacci(0) = 0
    # 0 -> 0, 1 -> 1, 2 -> 1, 3 -> 2, 4 -> 3, 5 -> 5, 6 -> 8 ...
    old, new = 0, 1
    for _ in range(n):
        old, new = new, old + new
    return old

@pytest.mark.parametrize(
    "n, result",
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8)
    ]
)
def test_fibonacci(n, result):
    assert fibonacci(n) == result
