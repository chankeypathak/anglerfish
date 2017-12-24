#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""JSON encoder with support for datetime, date, timedelta, Decimal,
IntEnum, Enum, MappingProxyType, deque, Exception, set, frozenset."""


from collections import deque
from datetime import date, datetime, timedelta
from decimal import Decimal
from enum import Enum, IntEnum
from functools import singledispatch
from types import MappingProxyType


__all__ = ("extended_JSON_encoder", )


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


@extended_JSON_encoder.register(IntEnum)
@extended_JSON_encoder.register(Enum)
def _serialize_enum(object_to_serialize: Enum) -> str:
    return object_to_serialize.value


@extended_JSON_encoder.register(MappingProxyType)
def _serialize_mappingproxytype(object_to_serialize: MappingProxyType) -> dict:
    return dict(object_to_serialize)


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
