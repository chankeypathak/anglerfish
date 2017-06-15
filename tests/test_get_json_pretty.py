#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.json_pretty()."""


from anglerfish import json_pretty


def test_json_pretty():
    # assert json_pretty({}) == "{}"
    assert json_pretty({"foo": True, "bar": 42, "links": ["https://github.com", "http://localhost"]}) == '\n\n{\n    "bar":       42,\n\n    "foo":       true,\n\n    "links": [\n        "https://github.com",\n\n        "http://localhost"\n    ]\n}\n'
