#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.json2xml()."""


from anglerfish import json2xml


def test_json2xml():
    assert json2xml({"foo": True, "bar": 42, "baz": []}) == r'<baz>\n\n</baz>\n<foo>\n    True\n</foo>\n<bar>\n    42\n</bar>'
    assert json2xml({}) == ""
