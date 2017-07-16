#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_clipboard()."""


import unittest

from anglerfish import get_clipboard

class TestName(unittest.TestCase):

    def test_dummy(self):
        clipboard_copy, clipboard_paste = get_clipboard()
        self.assertEqual(clipboard_copy, None)  # No xclip on Travis,but its Ok
        self.assertEqual(clipboard_paste, None)


if __name__.__contains__("__main__"):
    unittest.main()
