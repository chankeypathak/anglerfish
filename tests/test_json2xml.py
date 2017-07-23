#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.json2xml()."""


import unittest

from anglerfish import json2xml


class TestName(unittest.TestCase):

    def test_json2xml(self):
        self.assertEqual(json2xml({}), "")  # a == b


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
