import unittest

from utils import utils


class TestReversed(unittest.TestCase):
    def test_reversed_with_integers(self):
        self.assertEqual(utils.reversed(123), 321)
        self.assertEqual(utils.reversed(120), 21)      # trailing zero disappears
        self.assertEqual(utils.reversed(-123), -321)   # sign is preserved
        self.assertEqual(utils.reversed(0), 0)
        self.assertIsInstance(utils.reversed(123), int)

    def test_reversed_with_floats(self):
        with self.assertRaises(TypeError):
            utils.reversed(12.3)
        with self.assertRaises(TypeError):
            utils.reversed(-0.5)

    def test_reversed_with_strings(self):
        with self.assertRaises(TypeError):
            utils.reversed("123")
        with self.assertRaises(TypeError):
            utils.reversed("abc")


class TestFormatter(unittest.TestCase):
    def test_formatter_with_integers(self):
        self.assertEqual(utils.formatter(10), ("0b1010", "0o12"))
        self.assertEqual(utils.formatter(0), ("0b0", "0o0"))
        self.assertEqual(utils.formatter(255), ("0b11111111", "0o377"))
        self.assertEqual(utils.formatter(-8), ("-0b1000", "-0o10"))

    def test_formatter_with_floats(self):
        with self.assertRaises(TypeError):
            utils.formatter(10.0)
        with self.assertRaises(TypeError):
            utils.formatter(3.14)

    def test_formatter_with_strings(self):
        with self.assertRaises(TypeError):
            utils.formatter("10")
        with self.assertRaises(TypeError):
            utils.formatter("ten")


if __name__ == "__main__":
    unittest.main()
