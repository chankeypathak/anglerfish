#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.seconds2human()."""


import unittest

from anglerfish import seconds2human


class TestName(unittest.TestCase):

    def test_seconds2human(self):
        self.assertEqual(seconds2human(0), "00 Seconds")  # a == b
        self.assertEqual(seconds2human(42), "42 Seconds")  # a == b
        self.assertEqual(seconds2human(-666), "11 Minutes 06 Seconds")
        self.assertEqual(seconds2human(83490890),
                         "2 Years 236 Days 07 Hours 54 Minutes 50 Seconds")


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
