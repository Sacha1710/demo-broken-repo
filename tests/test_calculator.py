import pytest
from src.calculator import add, subtract, multiply, divide, average, is_prime


# --- Basic operations (these pass) ---

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12


# --- Failing tests (the agent must fix the source, not these tests) ---

def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

def test_divide_normal():
    assert divide(10, 2) == 5.0

def test_average_empty_list():
    assert average([]) == 0.0

def test_average_normal():
    assert average([1, 2, 3, 4, 5]) == 3.0

def test_is_prime_one_is_not_prime():
    assert is_prime(1) is False

def test_is_prime_known_primes():
    assert is_prime(2) is True
    assert is_prime(7) is True
    assert is_prime(13) is True

def test_is_prime_known_composites():
    assert is_prime(4) is False
    assert is_prime(9) is False
