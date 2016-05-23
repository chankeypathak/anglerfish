#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Add ENV environtment variables to python globals dict."""


def env2globals(pattern="PY_"):
    """Add ENV environtment variables to python globals dict."""
    try:
        for var in [_ for _ in os.environ.items() if _[0].startswith(pattern)]:
            globals().update({var[0]: var[1]}) # tuple to dict
    except Exception as e:
        log.warning(e)
        return False
    else:
        return True
