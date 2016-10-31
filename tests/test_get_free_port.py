#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_free_port()."""


from anglerfish import get_free_port


def get_free_port():
    assert get_free_port((8000, 8005)) == 8000
