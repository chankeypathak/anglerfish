#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_public_ip()."""


from anglerfish import make_json_flat


def test_make_json_flat():
    sample = {"key_external": {"key_nested": ["abc", "def"]}, "another": 42}
    correct_output = {'key_external__key_nested': ['abc', 'def'], 'another': 42}
    assert make_json_flat(sample) == correct_output
