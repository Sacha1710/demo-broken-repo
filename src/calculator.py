"""
Simple calculator module — intentionally contains 3 bugs for the hackathon demo.
The agent must find and fix them without touching the tests.
"""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    """Return a / b. Should raise ValueError when b is 0."""
    # BUG 1: missing guard — raises ZeroDivisionError instead of ValueError
    return a / b


def average(numbers: list[float]) -> float:
    """Return the arithmetic mean. Should return 0.0 for an empty list."""
    # BUG 2: missing empty-list guard — raises ZeroDivisionError
    return sum(numbers) / len(numbers)


def is_prime(n: int) -> bool:
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        # BUG 3: should return False for n < 2, but returns True for n == 1
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
