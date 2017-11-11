#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Convert bytes to kilobytes, megabytes, gigabytes, etc."""


from collections import deque, namedtuple
from types import MappingProxyType as frozendict

try:
    from ujson import dumps
except ImportError:
    from json import dumps


def bytes2human(integer_bytes: int) -> namedtuple:
    """Calculate Bytes, with precision from Bytes to Yottabytes."""
    # Calculate all Byte units from integer_bytes positive integer.
    kilo, bites = divmod(int(abs(integer_bytes)), 1_024)
    mega, kilo = divmod(kilo, 1_024)
    giga, mega = divmod(mega, 1_024)
    tera, giga = divmod(giga, 1_024)
    peta, tera = divmod(tera, 1_024)
    exa, peta = divmod(peta, 1_024)
    zetta, exa = divmod(exa, 1_024)
    yotta, zetta = divmod(zetta, 1_024)

    # Build a namedtuple with all named bytes units and all its integer values.
    bytes_units = namedtuple(
        "AllHumanFriendlyFrequentByteUnits",
        "byte kilo mega giga tera peta exa zetta yotta")(
        bites, kilo, mega, giga, tera, peta, exa, zetta, yotta)

    # Build a human friendly bytes string with frequent bytes units.
    bytes_parts, human_bytes_auto = deque(), None  # []
    if yotta:
        this_byte_unit = f"{yotta} Yottabyte{'s' if yotta > 1 else ''}"
        if not human_bytes_auto:
            human_bytes_auto, bytes_short = this_byte_unit, f"{yotta}Yb"
        bytes_parts.append(this_byte_unit)
    if zetta:
        this_byte_unit = f"{zetta} Zettabyte{'s' if zetta > 1 else ''}"
        if not human_bytes_auto:
            human_bytes_auto, bytes_short = this_byte_unit, f"{zetta}Zb"
        bytes_parts.append(this_byte_unit)
    if exa:
        this_byte_unit = f"{exa} Exabyte{'s' if exa > 1 else ''}"
        if not human_bytes_auto:
            human_bytes_auto, bytes_short = this_byte_unit, f"{exa}Eb"
        bytes_parts.append(this_byte_unit)
    if peta:
        this_byte_unit = f"{peta} Petabyte{'s' if peta > 1 else ''}"
        if not human_bytes_auto:
            human_bytes_auto, bytes_short = this_byte_unit, f"{peta}Pb"
        bytes_parts.append(this_byte_unit)
    if tera:
        this_byte_unit = f"{tera} Terabyte{'s' if tera > 1 else ''}"
        if not human_bytes_auto:
            human_bytes_auto, bytes_short = this_byte_unit, f"{tera}Tb"
        bytes_parts.append(this_byte_unit)
    if giga:
        this_byte_unit = f"{giga} Gigabyte{'s' if giga > 1 else ''}"
        if not human_bytes_auto:
            human_bytes_auto, bytes_short = this_byte_unit, f"{giga}Gb"
        bytes_parts.append(this_byte_unit)
    if mega:
        this_byte_unit = f"{mega} Megabyte{'s' if mega > 1 else ''}"
        if not human_bytes_auto:
            human_bytes_auto, bytes_short = this_byte_unit, f"{mega}Mb"
        bytes_parts.append(this_byte_unit)
    if kilo:
        this_byte_unit = f"{kilo} Kilobyte{'s' if kilo > 1 else ''}"
        if not human_bytes_auto:
            human_bytes_auto, bytes_short = this_byte_unit, f"{kilo}Kb"
        bytes_parts.append(this_byte_unit)
    if not human_bytes_auto:
        human_bytes_auto = f"{bites} Byte{'s' if bites > 1 else ''}"
        bytes_short = f"{bites}b"
    bytes_parts.append(f"{bites} Byte{'s' if bites > 1 else ''}")

    bytes_dict = {
        "byte": bites, "kilo": kilo, "mega": mega, "giga": giga,
        "tera": tera, "peta": peta, "exa": exa, "zetta": zetta, "yotta": yotta,
    }

    return namedtuple(
        "HumanBytes",
        "human units auto short dict json inmmutable")(
        " ".join(bytes_parts), bytes_units, human_bytes_auto, bytes_short,
        bytes_dict, dumps(bytes_dict), frozendict(bytes_dict))
