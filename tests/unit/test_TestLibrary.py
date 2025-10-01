import unittest
from py_robot_template.TestLibrary import TestLibrary


class TestTestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.lib = TestLibrary()

    def test_add_two_positive_ints(self) -> None:
        result = self.lib.add_two_ints(2, 3)
        self.assertEqual(result, 5)

    def test_add_positive_and_negative_int(self) -> None:
        result = self.lib.add_two_ints(5, -2)
        self.assertEqual(result, 3)

    def test_add_two_negative_ints(self) -> None:
        result = self.lib.add_two_ints(-4, -6)
        self.assertEqual(result, -10)

    def test_add_zero(self) -> None:
        result = self.lib.add_two_ints(0, 0)
        self.assertEqual(result, 0)

    def test_add_non_int_a(self) -> None:
        with self.assertRaises(AssertionError):
            self.lib.add_two_ints("1", 2)

    def test_add_non_int_b(self) -> None:
        with self.assertRaises(AssertionError):
            self.lib.add_two_ints(1, "2")
