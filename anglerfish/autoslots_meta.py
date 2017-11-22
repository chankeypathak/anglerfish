#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Angler Autoslots get __init__ args,make __slot__ variable for all attrs.

All assignments in __init__() MUST looks like:
self.attribute_name = attribute_value  # It does not support Annotations!.

http://tech.oyster.com/save-ram-with-python-slots  # Inspiration and ideas.
https://docs.python.org/3/reference/datamodel.html#slots  # Official docs."""


from collections import namedtuple
from inspect import getsource

import _ast


class AutoSlots_meta(type):

    """Autoslots get __init__ args,make __slot__ variable for all attrs."""
    __slots__ = ()

    def __new__(cls, name: str, bases: list, dictionary: dict) -> object:
        slots, original_slots = dictionary.get('__slots__', []), []
        for base in bases:
            if hasattr(base, "__slots__"):
                original_slots += base.__slots__
        if '__init__' in dictionary:
            init_src = getsource(type.__new__(cls, name, bases, dictionary))
            ast = compile(init_src, "", 'exec', _ast.PyCF_ONLY_AST, optimize=2)
            for declaration in tuple(ast.body[0].body):
                if isinstance(declaration, _ast.FunctionDef):
                    nombre = declaration.name
                    if nombre == '__init__':
                        initbody = declaration.body
                    for statement in initbody:
                        if isinstance(statement, _ast.Assign):
                            for target in statement.targets:
                                nombrecito = target.attr
                                if nombrecito not in original_slots:
                                    slots.append(nombrecito)
            dictionary['__slots__'] = namedtuple("AutoSlots", slots)(*slots)
            dictionary['__doc__'] = dictionary.get(
                '__doc__', f"""{name} class from '{dictionary['__module__']}'.
                \nInstantiated using Angler AutoSlots MetaClass.
                Mutable/writable/readable attributes: {dictionary['__slots__']}
                \nThis does not make the {name} class Inmmutable.
                \nAdding new attributes via assignments/setattr/etc is Blocked.
                \nUses less memory, speeds up attribute accesses and avoid bugs
                \nTry to add new attributes to this {name} class will raise:
                AttributeError: {name} object has no attribute\n\n""" + __doc__
            )
        return type.__new__(cls, name, bases, dictionary)
