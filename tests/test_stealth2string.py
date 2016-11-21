#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.stealth2string()."""


from anglerfish import stealth2string, string2stealth


def test_stealth2string():
    word = string2stealth("cat")
    stringy = stealth2string(word)
    assert isinstance(stringy, str)
    assert len(stringy) == 3
    assert u"\u200B" not in stringy
    assert u"\uFEFF" not in stringy
    assert stringy == "cat"
