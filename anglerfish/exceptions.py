#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Common exceptions for anglerfish."""


class AnglerfishException(Exception):
    """Common Exceptions for Anglerfish.

    Angler is a Simple Multipurpose Helper Utility Library for Python 3.6+ Apps

    For more info, docs, bugs, ideas, feedback and source code of Angler:
        https://github.com/juancarlospaco/anglerfish#angler
    Angler on PyPI:
        https://pypi.python.org/pypi/anglerfish
    Angler on Arch:
        https://aur.archlinux.org/packages/python-anglerfish

    AnglerfishException object is inmmutable (read-only) to avoid bugs,
    its '__setattr__', '__delattr__' and '__slots__' are all set to nothing.

    This Exception is meant to be used when Apps that use Angler fail.
    """
    __slots__ = ()

    def __setattr__(self, *args, **kwargs):
        raise TypeError("AnglerfishException object is inmmutable read-only.")

    def __delattr__(self, *args, **kwargs):
        raise TypeError("AnglerfishException object is inmmutable read-only.")
