#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_free_port()."""


import unittest

from anglerfish import get_free_port


class TestName(unittest.TestCase):

    def test_get_free_port(self):
        self.assertEqual(get_free_port((8000, 8005)), 8000)  # a == b


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
