from unittest import TestCase
from src.common_questions.non_matching_characters import non_matching_characters


class TestNonMatchingCharacters(TestCase):
    def test_non_matching_characters(self):
        test_string = "Hello, World!"
        expected_result = ["H", "e", ",", " ", "W", "r", "d", "!"]
        self.assertListEqual(non_matching_characters(test_string), expected_result)

    def test_non_matching_characters_all_matching(self):
        test_string = "Hello, World! Hello, World!"
        self.assertListEqual(non_matching_characters(test_string), [])

    def test_non_matching_characters_nothing_matching(self):
        test_string = "Python"
        expected_result = ["P", "y", "t", "h", "o", "n"]
        self.assertListEqual(non_matching_characters(test_string), expected_result)

    def test_non_matching_characters_empty_string(self):
        test_string = ""
        self.assertListEqual(non_matching_characters(test_string), [])
