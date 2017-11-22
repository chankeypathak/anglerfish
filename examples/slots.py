#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Basic simple miminum possible examples of Angler AutoSlots."""


from anglerfish import AutoSlots_meta


class TestinClass(metaclass=AutoSlots_meta):
    def __init__(self):
        self.a = 1
        self.b = 2


testin = TestinClass()
print(testin.a, testin.b)
testin.a, testin.b = 666, 42
print(testin.a, testin.b)
print(testin.__doc__)
print(testin.__slots__)
# This must raise:  AttributeError: 'TestinClass' object has no attribute 'c'.
testin.c = "This should not be possible, because its protected by Angler!.  ;P"
