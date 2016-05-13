#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Simple information helpers."""


import logging as log

from webbrowser import open_new_tab


def about_python():
    """Open Python official homepage."""
    log.debug("Opening: https://python.org")
    return open_new_tab('https://python.org')


def about_self():
    """Open this App homepage."""
    log.debug("Opening: {0}".format(__url__))
    return open_new_tab(__url__)


def view_code():
    """Open this App local Python source code."""
    log.debug("Opening: {0}".format(__file__))
    return open_new_tab(__file__)


def report_bug():
    """Open this App Bug Tracker."""
    log.debug("Opening: {0}/issues/new".format(__url__))
    return open_new_tab(__url__ + "/issues/new")
