#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Perform full walk of where, gather full path of all files."""


def walkdir2filelist(where, target, omit):
    """Perform full walk of where, gather full path of all files."""
    log.debug("Scan {},searching {},ignoring {}".format(where, target, omit))
    return tuple([os.path.join(r, f)
                  for r, d, fs in os.walk(where, followlinks=True)
                  for f in fs if not f.startswith('.') and
                  not f.endswith(omit) and
                  f.endswith(target)])  # only target files,no hidden files
