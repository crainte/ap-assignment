from addtime import *

import unittest


class add_time_tests(unittest.TestCase):

    def provided_example_test(self):
        ret = add_time("9:13 AM", 200)
        self.assertEqual("12:33 PM", ret)

    def zero_padded_hour_test(self):
        ret = add_time("09:13 AM", 200)
        self.assertEqual("12:33 PM", ret)

    def zero_padded_minute_test(self):
        ret = add_time("9:03 AM", 200)
        self.assertEqual("12:23 PM", ret)

    def padded_string_test(self):
        with self.assertRaises(SyntaxError):
            add_time("9:13 AM ", 200)
        with self.assertRaises(SyntaxError):
            add_time(" 9:13 AM", 200)
        with self.assertRaises(SyntaxError):
            add_time(" 9:13 AM ", 200)
        with self.assertRaises(SyntaxError):
            add_time(" 9 : 13 AM ", 200)

    def half_day_test(self):
        ret = add_time("9:13 AM", 720)
        self.assertEqual("9:13 PM", ret)
        ret = add_time("9:13 AM", -720)
        self.assertEqual("9:13 PM", ret)

    def whole_day_test(self):
        ret = add_time("9:13 AM", 1440)
        self.assertEqual("9:13 AM", ret)
        ret = add_time("9:13 AM", -1440)
        self.assertEqual("9:13 AM", ret)

    def single_rollover_test(self):
        ret = add_time("9:13 AM", 260)
        self.assertEqual("1:33 PM", ret)
        ret = add_time("9:13 AM", -260)
        self.assertEqual("4:53 AM", ret)

    def double_rollover_test(self):
        ret = add_time("9:13 AM", 1640)
        self.assertEqual("12:33 PM", ret)
        ret = add_time("9:13 AM", -1640)
        self.assertEqual("5:53 AM", ret)

    def invalid_period_test(self):
        with self.assertRaises(SyntaxError):
            ret = add_time("9:13 CST", 200)
        with self.assertRaises(SyntaxError):
            ret = add_time("9:13 CM", 200)

    def invalid_minute_test(self):
        with self.assertRaises(SyntaxError):
            add_time("9:3 PM", 200)
        with self.assertRaises(SyntaxError):
            add_time("9:63 PM", 200)
        with self.assertRaises(SyntaxError):
            add_time("9:-3 PM", 200)

    def invalid_hour_test(self):
        with self.assertRaises(SyntaxError):
            add_time("-9:13 PM", 200)
        with self.assertRaises(ValueError):
            add_time("13:13 PM", 200)
        with self.assertRaises(ValueError):
            add_time("00:13 PM", 200)

    def large_int_test(self):
         ret = add_time("9:13 AM", 523516402)
         self.assertEqual("10:35 AM", ret)

    def pretty_print_test(self):
         ret = add_time("9:13 AM", 47)
         self.assertEqual("10:00 AM", ret)
