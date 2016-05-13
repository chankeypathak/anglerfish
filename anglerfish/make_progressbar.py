#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Simple plain text progress bar."""


import sys

from datetime import datetime


def progressbar(i, title=None, logger=None, started=None):
    """Simple plain text progress bar."""
    i = i + 1
    p = "[{0}]".format("#" * (50 * i // 100) + "." * (50 - 50 * i // 100))
    p += " ~{0},{1}% ".format(100 * i // 100, random.randint(0, 9))[:80]
    p += " -> " + title.title()[:20] if title else ""
    p += " | Now={0}, Elapsed={1} ".format(
        datetime.datetime.now().time().isoformat()[:-7],
        str(datetime.datetime.now() - started)[:-7]) if started else ""
    p += "\n" if i >= 100 else "\r"
    logger.info(p) if logger else sys.stdout.write(p)
