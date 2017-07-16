#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.set_terminal_title()."""


import unittest

from anglerfish import set_terminal_title


class TestName(unittest.TestCase):

    def test_set_terminal_title(self):
        self.assertEqual(set_terminal_title("test"), "test")  # a == b
        self.assertEqual(set_terminal_title(""), "")  # a == b
