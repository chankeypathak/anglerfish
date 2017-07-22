#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Debug and Log Encodings and Check for root/administrator,return Bool."""


import logging as log
import os
import sys
from getpass import getuser
from platform import platform, python_version


_MSG = f"""
Python { python_version() } on { platform() }.
Default Encoding: { sys.getdefaultencoding()               }.
STDIN   Encoding: { getattr(sys.stdin, "encoding", "???")  }.
STDERR  Encoding: { getattr(sys.stderr, "encoding", "???") }.
STDOUT  Encoding: { getattr(sys.stdout, "encoding", "???") }.
I/O File Systems Encoding: { sys.getfilesystemencoding()   }.
PYTHONIOENCODING Encoding: { os.environ.get("PYTHONIOENCODING", "???")}.
Default File Systems Encoding Errors:     { sys.getfilesystemencodeerrors() }.
PYTHONLEGACYWINDOWSFSENCODING Encoding: {
    os.environ.get("PYTHONLEGACYWINDOWSFSENCODING", "???") }.
PYTHONLEGACYWINDOWSSTDIO Encoding:      {
    os.environ.get("PYTHONLEGACYWINDOWSSTDIO", "???") }."""


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
