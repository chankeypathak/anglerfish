#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.set_process_priority()."""


import os
import unittest

from anglerfish import set_process_priority


class TestName(unittest.TestCase):

    maxDiff, __slots__ = None, ()

    def test_set_process_priority(self):
        old_nice = os.getpriority(os.PRIO_PROCESS, 0)
        prio_set = set_process_priority(ionice=True)
        new_nice = os.getpriority(os.PRIO_PROCESS, 0)
        self.assertEqual(old_nice, 0)  # a == b
        self.assertTrue(isinstance(prio_set, bool))  # bool(x) is True
        self.assertTrue(prio_set)  # bool(x) is True
        self.assertEqual(new_nice, 19)  # a == b


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
