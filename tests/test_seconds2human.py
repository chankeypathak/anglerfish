#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.seconds2human()."""


from anglerfish import seconds2human


def test_seconds2human():
    assert seconds2human(0) == "00 Seconds"
    assert seconds2human(42) == "42 Seconds"
    assert seconds2human(-666) == "11 Minutes 06 Seconds"
    assert seconds2human(83490890) == "2 Years 236 Days 07 Hours 54 Minutes 50 Seconds"
