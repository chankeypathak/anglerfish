#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.bytes2human()."""


from anglerfish import bytes2human


def test_bytes2human():
    assert bytes2human(3284902384, "g") == '3 Gigabytes'
    assert bytes2human(0, "m") == '0 Megabytes'
    assert bytes2human(6666, "k") == '6 Kilobytes'
    assert bytes2human(-6666, "k") == '6 Kilobytes'
    assert bytes2human(1024, "k") == '1 Kilobytes'
