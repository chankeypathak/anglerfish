#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Make a JSON from Nested to Flat with an arbitrary delimiter."""


from types import MappingProxyType


def make_json_flat(jsony: dict, delimiter: str="__",
                   inmmutable: bool=False) -> dict:
    """Make a JSON from Nested to Flat with an arbitrary delimiter."""
    values = {}
    for item in jsony.keys():
        if isinstance(jsony[item], dict):
            get = make_json_flat(jsony[item], delimiter)
            for something in get.keys():
                values[f"{item}{delimiter}{something}"] = get[something]
        else:
            values[item] = jsony[item]
    return MappingProxyType(values) if inmmutable else values
