#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Set or Reset CLI Window Titlebar Title."""

import os
import sys

def set_terminal_title(titlez=""):
    """Set or Reset CLI Window Titlebar Title."""
    if titlez and isinstance(titlez, str) and len(titlez.strip()):
        # Windows:
        if sys.platform.startswith('win'):
            os.system('title {0}'.format(titlez.strip()))
        # Linux and otherwise
        else:
            print(r"\x1B]0; {0} \x07".format(titlez.strip()))
        return titlez
    else:
        if sys.platform.startswith('win'):
            os.system('title')
        else:
            print(r"\x1B]0;\x07")
