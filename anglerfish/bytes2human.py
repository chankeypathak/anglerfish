#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Convert bytes to kilobytes, megabytes, gigabytes, etc."""


from math import log2


def bytes2human(bites: int, to: str=None) -> str:
    """Convert bytes to kilobytes, megabytes, gigabytes, etc."""
    size = int(abs(bites))
    if to:  # Force a specific data unit from args.
        for i in range({'k': 1, 'm': 2, 'g': 3, 't': 4, 'p': 5, 'e': 6}[to]):
            size = size / 1_024
        unit, value = {'k': "Kilo", 'm': "Mega", 'g': "Giga",
                       't': "Tera", 'p': "Peta", 'e': "Exa"}[to], int(size)
    else:  # Auto-scale data unit.
        sfx = ('', 'Kilo', 'Mega', 'Giga', 'Tera',
               'Peta', 'Exa', 'Zetta', 'Yotta')
        order = int(log2(size) / 10) if size else 0
        value, unit = int(size / (1 << (order * 10))), sfx[order]
    return f"{ value } { unit }bytes"
