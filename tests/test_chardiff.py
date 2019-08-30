import unittest

import colorama

from chardiff import chardiff, get_color


class TestCharDiff(unittest.TestCase):
    self.RESET = colorama.Style.RESET_ALL

    def test_diff(self):
        a = "a"
        b = "b"
        marker = colorama.Style.BRIGHT
        result = marker + a + self.RESET

        self.assertEqual(chardiff(a, b), result)

    def test_diff_set_marker(self):
        a = "a"
        b = "b"
        marker = colorama.Fore.RED
        result = marker + a + self.RESET

        self.assertEqual(chardiff(a, b, marker=marker), result)

    def test_diff_a_longer_b(self):
        a = "abc"
        b = "a"
        marker = colorama.Style.BRIGHT
        result = "a" + marker + "bc" + self.RESET

        self.assertEqual(chardiff(a, b), result)

    def test_diff_b_longer_a(self):
        a = "a"
        b = "abc"
        marker = colorama.Style.BRIGHT
        result = "a"

        self.assertEqual(chardiff(a, b), result)

    def test_middle_similar(self):
        a = "string"
        b = "strong"
        marker = colorama.Style.BRIGHT
        result = "str" + marker + "i" + self.RESET + "ng"

        self.assertEqual(chardiff(a, b), result)

class TestGetColor(unittest.TestCase):
    def test_lower_case_color_name(self):
        color = "red"
        self.assertEqual(get_color(color), colorama.Fore.RED)

    def test_color_not_exist(self):
        color = "doesn't exist"
        with self.assertRaises(RuntimeError):
            get_color(color)
