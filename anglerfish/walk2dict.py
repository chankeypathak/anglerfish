#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Convert bytes to kilobytes, megabytes, gigabytes, etc."""


import os
from collections import OrderedDict, namedtuple
from pathlib import Path
from types import MappingProxyType as frozendict


try:
    from ujson import dumps
except ImportError:
    from json import dumps


def walk2dict(folder: Path, topdown: bool=True,
              onerror: object=None, followlinks: bool=False,
              showhidden: bool=False, strip: bool=False) -> namedtuple:
    """Perform full walk, gather full path of all files,
    based on os.walk with multiple output types & extras.

    Returns a namedtuple 'walk2dict' with multiple output types:
    - Nested common dictionary represents folder/file structure of folder.
    - JSON dumps string of the dictionary, uses uJSON if installed.
    - collections.OrderedDict() of the dictionary.
    - types.MappingProxyType() inmmutable of the dictionary."""
    ret = []
    for path, dirs, files in os.walk(folder, topdown=topdown,
                                     onerror=onerror, followlinks=followlinks):
        if not showhidden:
            dirs = [_ for _ in dirs if not _.startswith(".")]
            files = [_ for _ in files if not _.startswith(".")]
        a = {}
        if strip:
            p = path.strip(str(folder) + os.sep)
        else:
            p = path
        if len(p.split(os.sep)) == 1:
            parent = ''
        if len(p.split(os.sep)) > 1:
            parent = os.sep.join(p.split(os.sep)[:-1])
        if path == str(folder):
            parent = 'root'
        a['path'] = p
        a['fullpath'] = os.path.abspath(path)
        a['parent'] = parent
        a['dirs'] = dirs
        a['files'] = []

        for fyle in files:
            try:  # sometimes os.stat(ff) just fails,breaking all the loop.
                f = {}
                ff = path + os.sep + fyle
                (mode, ino, dev, nlink, uid, gid, size,
                 atime, mtime, ctime) = os.stat(ff)
                f['name'] = fyle
                f['mode'] = mode
                f['ino'] = ino
                f['dev'] = dev
                f['nlink'] = nlink
                f['uid'] = uid
                f['gid'] = gid
                f['size'] = size
                f['atime'] = atime
                f['mtime'] = mtime
                f['ctime'] = ctime
                a['files'].append(f)
            except Exception:
                pass
        ret.append(a)
    dict_f = ret[0]

    return namedtuple("walk2dict", "dict json OrderedDict frozendict")(
        dict_f, dumps(dict_f), OrderedDict(dict_f), frozendict(dict_f))
