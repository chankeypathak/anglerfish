#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.json_pretty()."""


import unittest

from anglerfish import json_pretty


class TestName(unittest.TestCase):

    def test_json_pretty(self):
        self.assertEqual(json_pretty({}), "{}")  # a == b
        self.assertEqual(
            json_pretty({"foo": True, "bar": 42, "links": ["https://github.com", "http://localhost"]}),
            '\n\n{\n    "bar":       42,\n\n    "foo":       true,\n\n    "links": [\n        "https://github.com",\n\n        "http://localhost"\n    ]\n}\n'
        )


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
