import unittest

import colorama

from chardiff import chardiff, get_color

class TestCharDiff(unittest.TestCase):
    def test_diff(self):
        a = "a"
        b = "b"
        marker = colorama.Style.BRIGHT
        result = marker + a + colorama.Style.RESET_ALL

        self.assertEqual(chardiff(a, b), result)

    def test_diff(self):
        a = "a"
        b = "b"
        marker = colorama.Fore.Red
        result = marker + a + colorama.Style.RESET_ALL

        self.assertEqual(chardiff(a, b), result)

class TestGetColor(unittest.TestCase):
    def test_lower_case_color_name(self):
        color = "red"
        self.assertEqual(get_color(color), colorama.Fore.Red)

    def test_lower_case_color_name(self):
        color = "doesn't exist"
        with self.assertRaises(RuntimeError):
            get_color(color)
