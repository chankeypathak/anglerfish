#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Decorator for PEP-526 & PEP-484, Python3 Static Type hinting annotations."""


# docs.python.org/3.6/whatsnew/3.6.html#pep-526-syntax-for-variable-annotations
# https://www.python.org/dev/peps/pep-0484
# Ideas welcome. We keep it without annotations itself. Checks Variables too!.


import sys

import logging as log

from functools import wraps


class typecheck(object):

    """Class that copies values of locals of a function or method."""

    def __init__(self, func):
        """Init class."""
        self._locals, self.func = {}, func

    def __call__(self, *args, **kwargs):
        """Calls the function but copy its values on return."""
        def tracer(frame, event, arg):
            if event == 'return':
                self._locals = frame.f_locals.copy()
        _old_profile = sys.getprofile()
        sys.setprofile(tracer)  # tracer activate on next call,return,exception
        try:  # this try is used to always restore the sys.setprofile(None)
            res = self.func(*args, **kwargs)  # trace the function call
        finally:
            sys.setprofile(_old_profile)  # Disable tracer,replace with old one
        return res

    def clear_locals(self, force_del=False):
        """Helper to clean. Optional force to 'del' all objects"""
        if force_del:
            for object_to_del in self._locals:
                del object_to_del
        self._locals = {}

    @property
    def locals(self):
        """Persistent values of locals of decorated functions."""
        return self._locals


def typecheck(f):
    """Decorator for PEP-526/PEP-484,Python Static Type hinting annotations."""
    def _check_annotations(tipe):
        """Checks argument types,return tuple of type and bool,True if Ok."""
        _type, is_ok = None, isinstance(tipe, (type, tuple, type(None)))
        if is_ok:  # Annotations can be Type or Tuple or None
            _type = tipe if isinstance(tipe, tuple) else tuple((tipe, ))
            if None in set(_type):  # if None on tuple replace with type(None)
                _type = tuple([_ if _ is not None else type(_) for _ in _type])
        return _type, is_ok  # _type is the parsed Type, is_ok is True if Ok.

    @wraps(f)  # wrap a function or method to Type Check it.
    def decorated(*args, **kwargs):
        """Decorator logic to extract '__annotations__' dict."""
        msg = "Type check error: {0} must be {1} but is {2} on function {3}()."
        notations, f_name = f.__annotations__.keys(), f.__code__.co_name
        doc = str(f.__doc__).splitlines()[0]  # Function DocString 1 line.
        print(doc)

        # __import__("ptpdb").set_trace()
        for i, name in enumerate(f.__code__.co_varnames):
            if name not in set(notations):
                continue  # this arg name has no annotation then skip it.
            _type, is_ok = _check_annotations(f.__annotations__.get(name))
            if is_ok:  # Force to tuple
                if i < len(args) and not isinstance(args[i], _type):
                    log.critical(msg.format(repr(args[i])[:50], _type,
                                            type(args[i]), f_name))
                elif name in kwargs and not isinstance(kwargs[name], _type):
                    log.critical(msg.format(repr(kwargs[name])[:50], _type,
                                            type(kwargs[name]), f_name))
        out = f(*args, **kwargs)
        _type, is_ok = _check_annotations(f.__annotations__.get("return"))
        if is_ok and not isinstance(out, _type) and "return" in notations:
            log.critical(msg.format(repr(out)[:50], _type, type(out), f_name))
        return out    # The output result of function or method.
    return decorated  # The decorated function or method.
