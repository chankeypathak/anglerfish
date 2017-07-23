#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.ChainableFuture."""


import unittest

from anglerfish import ChainableFuture


class TestName(unittest.TestCase):

    def test_ChainableFuture(self):
        future1 = ChainableFuture()
        future2 = future1.then(lambda arg: arg + "b")
        future1.set_result("a")
        self.assertEqual(future1.result(), "a")  # a == b
        self.assertEqual(future2.result(), "ab")  # a == b


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
