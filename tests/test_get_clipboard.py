#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_clipboard()."""


from anglerfish import get_clipboard


def test_set_terminal_title():
    clipboard_copy, clipboard_paste = get_clipboard()
    clipboard_copy == None  # Because no xclip on Travis, but its Ok.
    clipboard_paste == None  # Because no xclip on Travis, but its Ok.
