#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Convert bytes to kilobytes, megabytes, gigabytes, etc."""


from math import log2


def bytes2human(bites, *args):
    """Convert bytes to kilobytes, megabytes, gigabytes, etc."""
    size = int(abs(bites))
    sfx = ('', 'Kilo', 'Mega', 'Giga', 'Tera', 'Peta', 'Exa', 'Zetta', 'Yotta')
    order = int(log2(size) / 10) if size else 0
    value = int(size / (1 << (order * 10)))
    return f"{ value } { sfx[order] }bytes"
