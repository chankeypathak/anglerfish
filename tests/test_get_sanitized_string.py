#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_sanitized_string()."""


from anglerfish import get_sanitized_string


def test_get_sanitized_string():
    assert get_sanitized_string("\m/_(>_<)_\m/") == "\m/_(>_<)_\m/"
    assert get_sanitized_string("abcd1234") == "abcd1234"
    assert get_sanitized_string("") == ""
