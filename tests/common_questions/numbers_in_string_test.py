from unittest import TestCase

from src.common_questions.numbers_in_string import calculate_numbers_in_str


class NumbersInStringTestCase(TestCase):
    def test_numbers_in_string(self):
        test_arg = "123456"
        expected_result = 123456
        self.assertEqual(calculate_numbers_in_str(test_arg), expected_result)

    def test_numbers_in_mixed_string(self):
        test_arg = "123 456 &&& 789 )()() 123"
        expected_result = 123456789123
        self.assertEqual(calculate_numbers_in_str(test_arg), expected_result)

    def test_numbers_in_no_number_string(self):
        test_arg = "Hello, world!"
        self.assertIsNone(calculate_numbers_in_str(test_arg))

    def test_numbers_in_none_string(self):
        self.assertIsNone(calculate_numbers_in_str(None))

    def test_numbers_in_zero_string(self):
        test_arg = "0"
        expected_result = 0
        self.assertEqual(calculate_numbers_in_str(test_arg), expected_result)

    def test_numbers_in_zeroes_string(self):
        test_arg = "000000000"
        expected_result = 0
        self.assertEqual(calculate_numbers_in_str(test_arg), expected_result)

    def test_numbers_in_zeroes_one_string(self):
        test_arg = "000000010"
        expected_result = 10
        self.assertEqual(calculate_numbers_in_str(test_arg), expected_result)
