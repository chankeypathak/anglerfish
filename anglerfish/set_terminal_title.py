#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Set or Reset CLI Window Titlebar Title."""


import sys

from shutil import which
from subprocess import run


def set_terminal_title(titlez: str="") -> str:
    """Set or Reset CLI Window Titlebar Title."""
    if titlez and isinstance(titlez, str) and len(titlez.strip()):
        if sys.platform.startswith('win') and which("title"):  # Windows
            run(f"{ which('title') } { titlez }", shell=True, timeout=9)
        else:  # Linux, Os X and otherwise
            print(f"\x1B]0; { titlez } \x07")
        return titlez
    else:
        if sys.platform.startswith('win') and which("title"):
            run(str(which("title")), shell=True, timeout=9)
        else:
            print(r"\x1B]0;\x07")
        return ""  # Title should be "" so we return ""
