from unittest import TestCase
from src.common_questions.palindrome import is_palindrome


class PalindromeTestCase(TestCase):
    def test_is_palindrome(self):
        test_arg = "aabbaa"
        self.assertTrue(is_palindrome(test_arg))

    def test_is_palindrome_not_palindrome(self):
        test_arg = "aabb"
        self.assertFalse(is_palindrome(test_arg))

    def test_is_palindrome_nome(self):
        self.assertFalse(is_palindrome(None))
