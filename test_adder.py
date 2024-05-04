"""A test class for the add function."""
import unittest
from adder import add

class TestAdd(unittest.TestCase):
    """A test class for the add function."""

    def test_add(self):
        """Test the add function with positive numbers."""
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_negative_numbers(self):
        """Test the add function with negative numbers."""
        result = add(-5, -7)
        self.assertEqual(result, -12)

    def test_add_zero(self):
        """Test the add function with zero."""
        result = add(10, 0)
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()
