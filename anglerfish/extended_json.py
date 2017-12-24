#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""JSON encoder with support for datetime, date, timedelta, Decimal,
IntEnum, Enum, MappingProxyType, deque, Exception, set, frozenset.

Pretty-Printing JSON to String with a YAML-like syntax but still Valid JSON.
Uses a simple string replace to a unicode utf-8 character."""


from collections import deque
from datetime import date, datetime, timedelta
from decimal import Decimal
from enum import Enum, IntEnum
from functools import singledispatch
from json import dumps, loads  # ujson dont support "separators" argument.
from types import MappingProxyType


__all__ = ("extended_JSON_encoder", "loadz", "dumpz")


@singledispatch
def extended_JSON_encoder(object_to_serialize):
    """JSON encoder with support for datetime, date, timedelta, Decimal,
    IntEnum, Enum, MappingProxyType, deque, Exception, set, frozenset."""
    return str(object_to_serialize)


@extended_JSON_encoder.register(datetime)
def _serialize_datetime(object_to_serialize: datetime) -> str:
    return object_to_serialize.replace(microsecond=0).astimezone().isoformat()


@extended_JSON_encoder.register(date)
def _serialize_date(object_to_serialize: datetime) -> str:
    return object_to_serialize.isoformat()


@extended_JSON_encoder.register(timedelta)
def _serialize_timedelta(object_to_serialize: timedelta) -> float:
    return object_to_serialize.total_seconds()


@extended_JSON_encoder.register(Decimal)
def _serialize_decimal(object_to_serialize: Decimal) -> str:
    return float(object_to_serialize)


@extended_JSON_encoder.register(MappingProxyType)
def _serialize_mappingproxytype(object_to_serialize: MappingProxyType) -> dict:
    return dict(object_to_serialize)


@extended_JSON_encoder.register(IntEnum)
@extended_JSON_encoder.register(Enum)
def _serialize_enum(object_to_serialize: Enum) -> str:
    return object_to_serialize.value


@extended_JSON_encoder.register(set)
@extended_JSON_encoder.register(deque)
@extended_JSON_encoder.register(frozenset)
def _serialize_deque(object_to_serialize) -> list:
    return list(object_to_serialize)


@extended_JSON_encoder.register(Exception)
def _serialize_exception(object_to_serialize: Exception) -> dict:
    return {"error": object_to_serialize.__class__.__name__,
            "args": object_to_serialize.args,
            "__doc__": object_to_serialize.__doc__,
            "__repr__": object_to_serialize.__repr__(),
            "__str__": object_to_serialize.__str__(),
            "__slots__": getattr(object_to_serialize, "__slots__", None)}


##############################################################################


def dumpz(json_dict: dict, compatible: bool=True, *args, **kwargs) -> str:
    json_str = dumps(
        json_dict, sort_keys=True, indent=4,
        separators=("\n,", ":  ") if compatible else ("\n\ufeff", "\u200b\t"),
        default=extended_JSON_encoder, *args, **kwargs)
    return f"\n{json_str}\n"


def loadz(json_str: str, comment_start: str=None, *args, **kwargs) -> dict:
    if comment_start and isinstance(comment_start, str):
        json_lst = []
        for line in json_str.splitlines():
            if line.lstrip().startswith(comment_start):
                continue
            elif len(line.strip().split(comment_start)) >= 2:
                json_lst.append(line.split(comment_start)[0])
            else:
                json_lst.append(line)
        json_str = "\n".join(json_lst)
    return loads(json_str.replace("\ufeff", ",").replace("\u200b", ":"),
                 *args, **kwargs)
