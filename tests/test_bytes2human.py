#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.bytes2human()."""


import unittest

from anglerfish import bytes2human


class TestName(unittest.TestCase):

    def test_bytes2human(self):
        self.assertMultiLineEqual(bytes2human(3284902384), '3 Gigabytes')
        self.assertMultiLineEqual(bytes2human(0), '0 bytes')
        self.assertMultiLineEqual(bytes2human(6666), '6 Kilobytes')
        self.assertMultiLineEqual(bytes2human(-6666), '6 Kilobytes')
        self.assertMultiLineEqual(bytes2human(1024), '1 Kilobytes')


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
