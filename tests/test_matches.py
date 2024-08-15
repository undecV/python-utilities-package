# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

import unittest
import re
from utilities.matches import multiple_finditer


class TestMultipleFinditer(unittest.TestCase):

    def setUp(self) -> None:
        self.test_string = "The quick brown fox jumps over the lazy dog"

    def test_multiple_matches(self) -> None:
        patterns: list[re.Pattern] = [re.compile(r"fox"), re.compile(r"dog")]
        matches = list(multiple_finditer(patterns, self.test_string))
        self.assertEqual(len(matches), 2)
        self.assertEqual(matches[0].group(), "fox")
        self.assertEqual(matches[1].group(), "dog")

    def test_multiple_no_matches(self) -> None:
        patterns: list[re.Pattern] = []
        matches = list(multiple_finditer(patterns, self.test_string))
        self.assertEqual(len(matches), 0)

    def test_multiple_bad_matches(self) -> None:
        patterns: list[re.Pattern] = [re.compile(r"cat"), re.compile(r"dog")]
        matches = list(multiple_finditer(patterns, self.test_string))
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].group(), "dog")


if __name__ == "__main__":
    unittest.main()
