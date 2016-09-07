#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Simple dumb information helpers."""


import os
import logging as log

from webbrowser import open_new_tab


def about_self():
    """Open this App homepage."""
    if __url__ and isinstance(__url__, str):
        log.debug("Opening: {0}".format(__url__))
        return open_new_tab(__url__)


def view_code():
    """Open this App local Python source code."""
    if __file__ and os.path.isfile(__file__):
        log.debug("Opening file: {0}.".format(__file__))
        return open_new_tab(os.path.abspath(__file__))
