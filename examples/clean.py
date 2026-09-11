"""Clean sample"""
def add(a: int, b: int) -> int:
    """Add two integers"""
    return a + b

def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("divisor cannot be zero")
    return a / b
"""Minimalist clean example."""
