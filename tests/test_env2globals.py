#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.string2stealth()."""

import os

from anglerfish import env2globals


def test_env2globals():
    os.environ["PY_EXAMPLE"] = "cat"
    assert env2globals()
    # assert "PY_EXAMPLE" in globals().keys()  # FIXME check this
