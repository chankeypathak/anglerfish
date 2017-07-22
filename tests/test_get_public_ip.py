#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_public_ip()."""


import unittest

from anglerfish import get_public_ip


class TestName(unittest.TestCase):

    def test_get_public_ip(self):
        # Travis has an invalid certificate, and it fails because of that.
        ip = get_public_ip()  # this works ok locally.
        assert isinstance(ip, str)
        assert len(ip)
        assert "." in ip
