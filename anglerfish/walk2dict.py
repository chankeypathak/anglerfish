#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Convert bytes to kilobytes, megabytes, gigabytes, etc."""


import os


def get_directory_structure(rootdir, strip=False):
    """Return Nested Dictionary represents folder/file structure of rootdir."""
    ret = []
    for path, dirs, files in os.walk(rootdir):
        a = {}
        if strip:
            p = path.strip(rootdir + os.sep)

        else:
            p = path

        if len(p.split(os.sep)) == 1:
            parent = ''

        if len(p.split(os.sep)) > 1:
            parent = os.sep.join(p.split(os.sep)[:-1])

        if path == rootdir:
            parent = 'root'

        a['path'] = p
        a['fullpath'] = path
        a['parent'] = parent
        a['dirs'] = dirs
        a['files'] = []

        for fyle in files:
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

        ret.append(a)

    return(ret)
