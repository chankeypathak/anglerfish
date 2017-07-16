#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.log_exception()."""


import unittest

from anglerfish import log_exception


class TestName(unittest.TestCase):

    def test_log_exception(self):
        pass # FIXME: pytest.raises() dont like try:...except:... ?
        #  with pytest.raises(ZeroDivisionError):
        #     try:
        #         0 / 0
        #     except Exception:
        #         log_exception()
