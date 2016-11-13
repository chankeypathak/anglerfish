#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_public_ip()."""


from anglerfish import get_public_ip


def test_get_public_ip():
    ip = get_public_ip()
    assert isinstance(ip, str)
    assert len(ip)
    assert "." in ip
