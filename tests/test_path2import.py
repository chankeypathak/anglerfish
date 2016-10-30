#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Tests for path2import'''

import pytest
import os
from _utils import TempFile
from anglerfish import path2import

try:
    from anglerfish.exceptions import NamespaceConflictError
except ImportError:
    NamespaceConflictError = Exception


def test_normal():
    with TempFile('export = "anglerfish"') as tf:
        my_module = path2import(tf.name)
        assert my_module.export == 'anglerfish'

def test_syntax_error():
    with TempFile('export = ') as tf: # invaild python statements
        with pytest.raises(SyntaxError):
            my_module = path2import(tf.name)

        assert path2import(tf.name, ignore_exceptions=True) is None

def test_permission_denied():
    with TempFile('export = "anglerfish"') as tf:
        os.chmod(tf.name, 0o700)
        with pytest.raises(PermissionError):
            my_module = path2import(tf.name)
            assert my_module.export == 'anglerfish'

def test_not_found():
    with pytest.raises(FileNotFoundError):
        my_module = path2import('not_existed_module.py')

    assert path2import('not_existed_module.py', ignore_exceptions=True) is None

def test_invaild_module():
    with TempFile('export = "anglerfish"', suffix='.txt') as tf: # not a .py module
        with pytest.raises(ImportError):
            my_module = path2import(tf.name)

        assert path2import(tf.name, ignore_exceptions=True) is None

def test_reimport():
    with TempFile('export = "anglerfish"') as tf:
        my_module1 = path2import(tf.name)
        assert my_module1.export == 'anglerfish'
        my_module2 = path2import(tf.name)
        assert my_module1.export == my_module2.export
        assert my_module1 == my_module2

def test_check_namespace():
    global global_module
    global_module = None
    assert 'global_module' in globals()

    with TempFile('export = "anglerfish"') as tf:
        my_module1 = path2import(tf.name, 'global_module')
        global_module = my_module1

        my_module2 = path2import(tf.name, 'global_module', check_namespace=True)
        assert my_module2 == global_module

    with TempFile('export = "anglerfish"') as tf:
        with pytest.raises(NamespaceConflictError):
            my_module3 = path2import(tf.name, name='os')

        my_module4 = path2import(tf.name, name='os', ignore_exceptions=True) == None


    del(global_module)
