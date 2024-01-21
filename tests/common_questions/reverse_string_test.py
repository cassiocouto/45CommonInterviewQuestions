from unittest import TestCase
from src.common_questions.reverse_string import reverse_string


class ReverseStringTestCase(TestCase):
    def test_reverse_string(self):
        test_arg = "Hello, world!"
        expected_result = "!dlrow ,olleH"
        actual_result = reverse_string(test_arg)
        self.assertEqual(actual_result, expected_result)

    def test_reverse_string_none(self):
        self.assertIsNone(reverse_string(None))
