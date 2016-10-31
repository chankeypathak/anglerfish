#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.ChainableFuture."""


from anglerfish import ChainableFuture


def test_ChainableFuture():
    future1 = ChainableFuture()
    future2 = future1.then(lambda arg: arg + "b")
    future1.set_result("a")
    assert future1.result() == "a"
    assert future2.result() == "ab"
