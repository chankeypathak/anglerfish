#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.set_single_instance()."""


import socket
import unittest

from anglerfish import set_single_instance


class TestName(unittest.TestCase):

    def get_set_single_instance(self):
        lock = set_single_instance("test")
        self.assertTrue(isinstance(lock, socket.socket))  # bool(x) is True
        self.assertEqual(lock.getsockname().decode("utf8"), r'\x00_test__lock')


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
