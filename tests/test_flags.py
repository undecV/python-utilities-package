# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


import unittest
from utilities.flags import Flags


class TestFlags(unittest.TestCase):
    def setUp(self):
        self.flags = Flags("T", "P", "F")

    def test_initialization(self):
        self.assertEqual(str(self.flags), "   ")
        self.assertFalse(self.flags.any_set())
        self.assertFalse(self.flags.all_set())

    def test_set(self):
        self.flags.set("T")
        self.assertEqual(str(self.flags), "T  ")
        self.assertTrue(self.flags.is_set("T"))

    def test_clear(self):
        self.flags.set("T")
        self.flags.set("P")
        self.flags.set("F")
        self.flags.clear()
        self.assertEqual(str(self.flags), "   ")
        self.assertFalse(self.flags.is_set("T"))
        self.assertFalse(self.flags.is_set("P"))
        self.assertFalse(self.flags.is_set("F"))

    def test_toggle(self):
        self.flags.set("T")
        self.flags.toggle("T")
        self.assertFalse(self.flags.is_set("T"))
        self.assertEqual(str(self.flags), "   ")
        self.flags.toggle("P")
        self.assertTrue(self.flags.is_set("P"))
        self.assertEqual(str(self.flags), " P ")

    def test_is_set(self):
        self.flags.set("F")
        self.assertTrue(self.flags.is_set("F"))
        self.assertFalse(self.flags.is_set("T"))

    def test_any_set(self):
        self.flags.set("P")
        self.assertTrue(self.flags.any_set())
        self.flags.clear()
        self.assertFalse(self.flags.any_set())

    def test_all_set(self):
        self.flags.set("T")
        self.flags.set("P")
        self.flags.set("F")
        self.assertTrue(self.flags.all_set())
        self.flags.clear()
        self.assertFalse(self.flags.all_set())

    def test_unset(self):
        self.flags.set("T")
        self.flags.set("F")
        self.flags.unset("T")
        self.assertFalse(self.flags.is_set("T"))
        self.assertTrue(self.flags.is_set("F"))
        self.assertEqual(str(self.flags), "  F")

    def test_str_representation(self):
        self.flags.set("T")
        self.flags.set("F")
        self.assertEqual(str(self.flags), "T F")

    def test_repr_representation(self):
        self.assertEqual(repr(self.flags), "<Flags {'T': False, 'P': False, 'F': False}>")
        self.flags.set("T")
        self.assertEqual(repr(self.flags), "<Flags {'T': True, 'P': False, 'F': False}>")


if __name__ == "__main__":
    unittest.main()
