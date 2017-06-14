#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Set Monitor Display OFF, return Bool."""


import logging as log
import sys

from shutil import which
from subprocess import run


def set_display_off():
    """Set Monitor Display OFF, it should Auto-ON when needed, return Bool."""
    log.debug("Setting Monitor Display OFF.")
    _xset = which("xset")
    if sys.platform.startswith('linux') and _xset:
        return not bool(run(f"{_xset} dpms force off", shell=True).returncode)
    elif sys.platform.startswith('darwin'):
        return not bool(run(
            """echo 'tell application "Finder" to sleep' | osascript""",
            shell=True, timeout=3).returncode)
    elif sys.platform.startswith('win'):  # Complicated as hell,dont worth it.
        log.warning("Set Monitor Display OFF not supported on this OS.")
        return False
