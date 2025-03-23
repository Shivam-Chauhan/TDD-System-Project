import sys
import os

# Add project_folder to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tdd_main import StringCalculator
import unittest


class TestStringCalculator(unittest.TestCase):
    """
        Sample test file, currently using unittest, can also use pytest.
    """
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.add("1,2,3,4"), 10)

    def test_new_line_between_numbers(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)
    
    def test_custom_delimiter_long(self):
        self.assertEqual(self.calc.add("//[***]\n1***2***3"), 6)
    
    def test_multiple_custom_delimiters(self):
        self.assertEqual(self.calc.add("//[*][%]\n1*2%3"), 6)
    
    def test_ignore_large_numbers(self):
        self.assertEqual(self.calc.add("2,1001"), 2)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,-2,3,-4")
        self.assertIn("Negatives not allowed", str(context.exception))

if __name__ == "__main__":
    unittest.main()
