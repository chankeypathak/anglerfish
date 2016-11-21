#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.string2stealth()."""


from anglerfish import string2stealth


def test_string2stealth():
    word = "cat"
    stealthed = string2stealth(word)
    assert isinstance(stealthed, str)
    assert len(stealthed)
    assert u"\u200B" in stealthed
    assert u"\uFEFF" in stealthed
