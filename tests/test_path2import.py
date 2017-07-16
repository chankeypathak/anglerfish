#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tests for path2import."""


from tempfile import NamedTemporaryFile
from pathlib import Path

import pytest

from anglerfish import path2import

try:
    from anglerfish.exceptions import NamespaceConflictError
except ImportError:
    NamespaceConflictError = Exception


def test_normal():
    with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
        tf.write_text('export = "anglerfish"')
        my_module = path2import(tf.as_posix())
        assert my_module.export == 'anglerfish'


def test_syntax_error():
    with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
        tf.write_text('export = ')
        with pytest.raises(SyntaxError):
            my_module = path2import(tf.as_posix())
            print(my_module)  # to avoid warning "assigned but never used"

        assert path2import(tf.as_posix(), ignore_exceptions=True) is None


def test_permission_denied():
    pass

    # FIXME: this should work, why is not working ?.
    # with TempFile('export = "anglerfish"') as tf:
    #     os.chmod(tf.name, 0o400)  # Reduce file permissions to non-readable
    #     with pytest.raises(PermissionError):
    #         my_module = path2import(tf.name)
    #         assert my_module.export == 'anglerfish'


def test_not_found():
    with pytest.raises(ModuleNotFoundError):
        my_module = path2import('not_existed_module.py')
        print(my_module)  # to avoid warning "assigned but never used"

    assert path2import('not_existed_module.py', ignore_exceptions=True) is None


def test_invaild_module():
    with Path(NamedTemporaryFile("w", suffix=".txt", delete=False).name) as tf:
        tf.write_text('export = "anglerfish"')  # Not a .py module.
        with pytest.raises(ImportError):
            my_module = path2import(tf.as_posix())
            print(my_module)  # to avoid warning "assigned but never used"

        assert path2import(tf.as_posix(), ignore_exceptions=True) is None


def test_reimport():
    with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
        tf.write_text('export = "anglerfish"')
        my_module1 = path2import(tf.as_posix())
        assert my_module1.export == 'anglerfish'
        my_module2 = path2import(tf.as_posix())
        assert my_module1.export == my_module2.export
        assert my_module1 == my_module2


def test_check_namespace():
    global global_module
    global_module = None
    assert 'global_module' in globals()

    with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
        tf.write_text('export = "anglerfish"')
        my_module1 = path2import(tf.as_posix(), 'global_module')
        global_module = my_module1

        my_module2 = path2import(tf.as_posix(), 'global_module', check_namespace=True)
        assert my_module2 == global_module

    with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
        tf.write_text('export = "anglerfish"')
        with pytest.raises(NamespaceConflictError):
            my_module3 = path2import(tf.as_posix(), name='os')
            print(my_module3)  # to avoid warning "assigned but never used"

        my_module4 = path2import(tf.as_posix(), name='os', ignore_exceptions=True) == None
        print(my_module4)  # to avoid warning "assigned but never used"

    del(global_module)
