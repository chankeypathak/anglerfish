#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Perform full walk of where, gather full path of all files."""


import os
from collections import namedtuple

try:
    from ujson import dumps
except ImportError:
    from json import dumps


def walk2list(folder: str, target: tuple, omit: tuple=(),
              showhidden: bool=False, topdown: bool=True,
              onerror: object=None, followlinks: bool=False) -> namedtuple:
    """Perform full walk, gather full path of all files,
    based on os.walk with multiple output types & extras.

    Returns a namedtuple 'walk2list' with multiple output types:
    - List represents folder/file structure of folder.
    - JSON dumps string of the list, uses uJSON if installed.
    - tuple of the list.
    - set of the list.
    - frozenset of the list."""
    oswalk = os.walk(folder, topdown=topdown,
                     onerror=onerror, followlinks=followlinks)
    listy = [os.path.abspath(os.path.join(r, f))
             for r, d, fs in oswalk
             for f in fs if not f.startswith(() if showhidden else ".") and
             not f.endswith(omit) and
             f.endswith(target)]

    return namedtuple("walk2list", "list tuple json set frozenset")(
        list, tuple(listy), dumps(listy), set(listy), frozenset(listy))
