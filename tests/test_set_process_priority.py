#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.set_process_priority()."""


import os

from anglerfish import set_process_priority


def test_set_process_priority():
    old_nice = os.getpriority(os.PRIO_PROCESS, 0)
    prio_set = set_process_priority(ionice=True)
    new_nice = os.getpriority(os.PRIO_PROCESS, 0)
    assert old_nice == 0
    assert isinstance(prio_set, bool)
    assert prio_set
    assert new_nice == 19
