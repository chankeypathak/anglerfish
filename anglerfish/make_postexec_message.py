#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Simple Post-Execution Message with information about RAM and Time."""


import logging as log
import os
import sys

from datetime import datetime

try:
    import resource
except ImportError:
    resource = None  # MS Window dont have resource


def make_post_execution_message(app=__doc__.splitlines()[0].strip()):
    """Simple Post-Execution Message with information about RAM and Time."""
    use, al = 0, 0
    if sys.platform.startswith("linux"):
        use = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss *
                  resource.getpagesize() / 1024 / 1024 if resource else 0)
        al = int(os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES') /
                 1024 / 1024 if hasattr(os, "sysconf") else 0)
    msg = "Total Maximum RAM Memory used: ~{0} of {1}MegaBytes".format(use, al)
    log.info(msg)
    if start_time and datetime:
        log.info("Total Working Time: {0}".format(datetime.now() - start_time))
    print("Thanks for using this App,share your experience! {0}".format("""
    Twitter: https://twitter.com/home?status=I%20Like%20{n}!:%20{u}
    Facebook: https://www.facebook.com/share.php?u={u}&t=I%20Like%20{n}
    G+: https://plus.google.com/share?url={u}""".format(u=__url__, n=app)))
    return msg  # see the message, but dont get on logs.
