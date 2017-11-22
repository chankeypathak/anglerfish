#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.stealth2string()."""


import unittest

from anglerfish import stealth2string, string2stealth


class TestName(unittest.TestCase):

    maxDiff, __slots__ = None, ()

    def test_stealth2string(self):
        word = string2stealth("cat")
        stringy = stealth2string(word)
        self.assertTrue(isinstance(stringy, str))  # bool(x) is True
        self.assertEqual(len(stringy), 3)  # a == b
        self.assertTrue(u"\u200B" not in stringy)
        self.assertTrue(u"\uFEFF" not in stringy)
        self.assertEqual(stringy, "cat")  # a == b


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
