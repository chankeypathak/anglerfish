#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Common exceptions for anglerfish"""


class AnglerfishException(Exception):
    pass


class NamespaceConflictError(ImportError, AnglerfishException):
    pass
