#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Debug and Log Encodings and Check for root/administrator,return Bool."""


import logging as log
import os
import sys

from getpass import getuser
from platform import platform, python_version


_MSG = """Python {ver} on {so}.\nChecking All System Encodings...
Default Encoding: {d}.\nSTDIN   Encoding: {i}.
STDERR  Encoding: {e}.\nSTDOUT  Encoding: {o}.
I/O File Systems Encoding: {f}.\nPYTHONIOENCODING Encoding: {io}.
PYTHONLEGACYWINDOWSFSENCODING Encoding: {leg}.
PYTHONLEGACYWINDOWSSTDIO      Encoding: {wio}.
Default File Systems Encode Errors:     {er}.""".format(
    ver=python_version(), so=platform(), d=sys.getdefaultencoding(),
    f=sys.getfilesystemencoding(), i=getattr(sys.stdin, "encoding", "???"),
    e=getattr(sys.stderr, "encoding", "???"),
    o=getattr(sys.stdout, "encoding", "???"),
    io=os.environ.get("PYTHONIOENCODING", "???"),
    leg=os.environ.get("PYTHONLEGACYWINDOWSFSENCODING", "???"),
    wio=os.environ.get("PYTHONLEGACYWINDOWSSTDIO", "???"),
    er=sys.getfilesystemencodeerrors() if hasattr(
        sys, "getfilesystemencodeerrors") else "???")


def check_encoding(check_root=True):
    """Debug and Log Encodings and Check for root/administrator,return Bool."""
    log.debug(_MSG)
    os.environ["PYTHONIOENCODING"] = "utf-8"
    if sys.platform.startswith(("linux", "darwin")) and check_root:  # root
        if not os.geteuid():
            log.warning("Runing as root is not Recommended !.")
            return False
    elif sys.platform.startswith("win") and check_root:  # administrator
        if getuser().lower().startswith("admin"):
            log.warning("Runing as Administrator is not Recommended !.")
            return False
    return True
