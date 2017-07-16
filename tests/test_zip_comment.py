#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_zip_comment()."""


import unittest

from zipfile import ZipFile

from anglerfish import set_zip_comment, get_zip_comment


class TestName(unittest.TestCase):

    def test_zip_comment(self):
        ZipFile("test.zip", 'w').close()
        self.assertTrue(set_zip_comment("test.zip", "test"))  # bool(x) is True
        self.assertEqual(get_zip_comment("test.zip"), "test")  # a == b
