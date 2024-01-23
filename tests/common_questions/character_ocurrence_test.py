from unittest import TestCase
from src.common_questions.character_occurence import (
    count_single_character,
    count_many_characters,
)


class TestCharacterOccurence(TestCase):
    def test_count_single_character(self):
        test_str = "aaabbbcccaaabbbccc"
        test_char = "a"
        expected_count = 6
        self.assertEqual(count_single_character(test_str, test_char), expected_count)

    def test_count_single_character_inexistent_character(self):
        test_str = "aaabbbcccaaabbbccc"
        test_char = "d"
        expected_count = 0
        self.assertEqual(count_single_character(test_str, test_char), expected_count)

    def test_count_single_character_empty_string(self):
        test_str = ""
        test_char = "a"
        expected_count = 0
        self.assertEqual(count_single_character(test_str, test_char), expected_count)

    def test_count_many_characters(self):
        test_str = "aaabbbcccabbccc"
        test_char = ["a", "b", "c"]
        expected_result = {"a": 4, "b": 5, "c": 6}
        self.assertEqual(count_many_characters(test_str, test_char), expected_result)

    def test_count_many_characters_with_inexistent_characters(self):
        test_str = "aaabbbcccabbccc"
        test_char = ["a", "b", "c", "d"]
        expected_result = {"a": 4, "b": 5, "c": 6, "d": 0}
        self.assertEqual(count_many_characters(test_str, test_char), expected_result)

    def test_count_many_characters_with_empty_string(self):
        test_str = ""
        test_char = ["a", "b", "c", "d"]
        expected_result = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.assertEqual(count_many_characters(test_str, test_char), expected_result)
