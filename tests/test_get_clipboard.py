#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.set_terminal_title()."""


from anglerfish import set_terminal_title


def test_set_terminal_title():
    clipboard_copy, clipboard_paste = get_clipboard()
    clipboard_copy("42")
    assert clipboard_paste() == "42"
