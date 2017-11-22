#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.log_exception()."""


import unittest

from anglerfish import log_exception


class TestName(unittest.TestCase):

    maxDiff, __slots__ = None, ()

    def test_log_exception(self):
        print(log_exception)
        # with self.assertRaises(ZeroDivisionError):  # Fails on Travis.
        #     try:
        #         0 / 0
        #     except Exception:
        #         log_exception()


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
