#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test for anglerfish.set_single_instance()."""


import socket

from anglerfish import set_single_instance


def get_set_single_instance():
    lock = set_single_instance("test")
    assert isinstance(lock, socket.socket)
    assert lock.getsockname().decode("utf-8") == r'\x00_test__lock'
