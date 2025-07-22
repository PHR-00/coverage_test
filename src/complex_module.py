# src/complex_module.py

class MathOperations:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def factorial(self, n):
        if n < 0:
            raise ValueError("Negative number not allowed.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


class StringProcessor:
    def reverse(self, s):
        return s[::-1]

    def is_palindrome(self, s):
        return s == s[::-1]

    def analyze(self, s):
        result = {
            "length": len(s),
            "has_digit": any(char.isdigit() for char in s),
            "has_alpha": any(char.isalpha() for char in s),
            "is_upper": s.isupper(),
            "is_lower": s.islower(),
        }
        return result


def classify_number(n):
    if n < 0:
        return "negative"
    elif n == 0:
        return "zero"
    elif n < 10:
        return "small"
    elif n < 100:
        return "medium"
    else:
        return "large"


def complex_logic(x, y):
    if x > y:
        if x - y > 10:
            return "x is much greater"
        else:
            return "x is greater"
    elif x < y:
        if y - x > 5:
            return "y is much greater"
        else:
            return "y is greater"
    else:
        return "equal"