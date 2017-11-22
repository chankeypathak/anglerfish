#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Make a JSON from Nested to Flat with an arbitrary delimiter."""


from collections import OrderedDict, namedtuple
from types import MappingProxyType as frozendict


try:
    from ujson import dumps
except ImportError:
    from json import dumps


def make_json_flat(jsony: dict, delimiter: str="__") -> namedtuple:
    """Make a JSON from Nested to Flat with an arbitrary delimiter."""
    values = {}
    for item in jsony.keys():
        if isinstance(jsony[item], dict):
            get = make_json_flat(jsony[item], delimiter)
            for something in get.keys():
                values[f"{item}{delimiter}{something}"] = get[something]
        else:
            values[item] = jsony[item]

    return namedtuple("JSONFlat", "dict json OrderedDict frozendict")(
        values, dumps(values), OrderedDict(values), frozendict(values))
