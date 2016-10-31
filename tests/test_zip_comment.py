#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.get_zip_comment()."""


from zipfile import ZipFile

from anglerfish import set_zip_comment, get_zip_comment



def test_zip_comment():
    ZipFile("test.zip", 'w').close()
    assert set_zip_comment("test.zip", "test") == True
    assert get_zip_comment("test.zip") == "test"
