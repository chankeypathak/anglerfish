#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.log_exception()."""


from anglerfish import log_exception


def test_log_exception():
    with pytest.raises(ZeroDivisionError):
        try:
            0 / 0
        except Exception:
            log_exception()
