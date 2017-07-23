#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_public_ip()."""


import unittest

from anglerfish import make_json_flat


class TestName(unittest.TestCase):

    def test_make_json_flat(self):
        sample = {"key_external": {"key_nested": ["abc", "def"]}, "another": 42}
        correct_output = {'key_external__key_nested': ['abc', 'def'], 'another': 42}
        self.assertEqual(make_json_flat(sample), correct_output)  # a == b


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
