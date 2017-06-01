#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Simple Post-Execution Message with information about RAM and Time."""


import atexit
import logging as log
import os
import sys

from datetime import datetime

try:
    import resource
except ImportError:
    resource = None  # MS Window dont have resource

try:
    from anglerfish.bytes2human import bytes2human
    from anglerfish.seconds2human import timedelta2human
except ImportError:
    from anglerfish import bytes2human, timedelta2human


def make_post_exec_msg(start_time=None, comment=None):
    """Simple Post-Execution Message with information about RAM and Time."""
    use, al, msg = 0, 0, ""
    if sys.platform.startswith(("win", "darwin")):
        msg = "No information about RAM usage available on non-Linux systems\n"
    elif sys.platform.startswith("linux"):
        use = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss *
                  resource.getpagesize() if resource else 0)
        al = int(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
                 if hasattr(os, "sysconf") else 0)
        msg += "Max Memory Used: {0} ({1} bytes) of {2} ({3} bytes).\n".format(
            bytes2human(use, "m"), use, bytes2human(al, "m"), al)
        if start_time and datetime:
            _t = datetime.now() - start_time
            msg += "Working Time: {0} ({1}).\n".format(timedelta2human(_t), _t)
    if comment:
        msg += str(comment).strip()
    log.debug("Preparing Simple Post-Execution Messages.")
    atexit.register(log.info, msg)
    return msg


def app_is_ready(start_time):  # this goes at end of your apps __init__()
    """Simple Post-StartUp Message with Start-Up time."""
    _t = datetime.now() - start_time
    log.debug("Total Start-Up Time: {0} ({1})".format(timedelta2human(_t), _t))
