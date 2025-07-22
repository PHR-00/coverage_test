import pytest
from src.complex_module import (
    MathOperations,
    StringProcessor,
    classify_number,
    complex_logic,
)

# --- Test Class ---
class TestComplexModule:

    # --- MathOperations Tests ---
    
    def test_add(self): 
        print("\n>>> 正在执行测试: test_add <<<")
        m = MathOperations()
        
        assert m.add(5, 3) == 8
        
    def test_divide(self):
        m = MathOperations()
        assert m.divide(10, 2) == 5
        with pytest.raises(ValueError):
            m.divide(10, 0)

    def test_factorial(self):
        m = MathOperations()
        assert m.factorial(5) == 120
        assert m.factorial(0) == 1
        with pytest.raises(ValueError):
            m.factorial(-1)

    # --- StringProcessor Tests ---

    def test_reverse(self):
        s = StringProcessor()
        assert s.reverse("hello") == "olleh"

    def test_is_palindrome(self):
        s = StringProcessor()
        assert s.is_palindrome("madam") is True
        assert s.is_palindrome("hello") is False

    def test_analyze(self):
        s = StringProcessor()
        result = s.analyze("Abc123")
        assert result["length"] == 6
        assert result["has_digit"] is True
        assert result["has_alpha"] is True
        assert result["is_upper"] is False
        assert result["is_lower"] is False
        #assert result["is_lower"] is True

    # --- classify_number Tests ---

    @pytest.mark.parametrize("value,expected", [
        (-5, "negative"),
        # (0, "zero"),
        # (5, "small"),
        # (50, "medium"),
        # (150, "large")
    ])
    def test_classify_number(self, value, expected): 
        assert classify_number(value) == expected

    # --- complex_logic Tests ---

    @pytest.mark.parametrize("x,y,expected", [
        (15, 2, "x is much greater"),
        (10, 5, "x is greater"),
        (3, 10, "y is much greater"),
        (6, 8, "y is greater"),
        (7, 7, "equal")
    ])
    def test_complex_logic(self, x, y, expected): 
        assert complex_logic(x, y) == expected