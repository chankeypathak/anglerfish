#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.set_terminal_title()."""


from anglerfish import set_terminal_title


def test_set_terminal_title():
    assert set_terminal_title("test") == "test"
    assert set_terminal_title("") == ""
