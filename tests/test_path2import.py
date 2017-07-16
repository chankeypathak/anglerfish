#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tests for path2import."""


from pathlib import Path
from tempfile import NamedTemporaryFile

import pytest
from anglerfish import path2import

try:
    from anglerfish.exceptions import NamespaceConflictError
except ImportError:
    NamespaceConflictError = Exception

import unittest


class TestName(unittest.TestCase):

    def test_dummy(self):
        pass

    def test_normal(self):
        with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
            tf.write_text('export = "anglerfish"')
            my_module = path2import(tf.as_posix())
            self.assertEqual(my_module.export, 'anglerfish')

    def test_syntax_error(self):
        with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
            tf.write_text('export = ')
            with pytest.raises(SyntaxError):
                my_module = path2import(tf.as_posix())
                print(my_module)  # to avoid warning "assigned but never used"

            self.assertIsNone(path2import(tf.as_posix(), ignore_exceptions=True))

    def test_permission_denied(self):
        pass
        # FIXME: this should work, why is not working ?.
        # with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
        #     os.chmod(tf.as_posix(), 0o400)  # Reduce file permissions to non-readable
        #     with pytest.raises(PermissionError):
        #         my_module = path2import(tf.as_posix())
        #         self.assertEqual(my_module.export, 'anglerfish')

    def test_not_found(self):
        with pytest.raises(ModuleNotFoundError):
            my_module = path2import('not_existed_module.py')
            print(my_module)  # to avoid warning "assigned but never used"

        self.assertIsNone(path2import('not_existed_module.py', ignore_exceptions=True))

    def test_invaild_module(self):
        with Path(NamedTemporaryFile("w", suffix=".txt", delete=False).name) as tf:
            tf.write_text('export = "anglerfish"')  # Not a .py module.
            with pytest.raises(ImportError):
                my_module = path2import(tf.as_posix())
                print(my_module)  # to avoid warning "assigned but never used"

            self.assertIsNone(path2import(tf.as_posix(), ignore_exceptions=True))

    def test_reimport(self):
        with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
            tf.write_text('export = "anglerfish"')
            my_module1 = path2import(tf.as_posix())
            self.assertEqual(my_module1.export, 'anglerfish')
            my_module2 = path2import(tf.as_posix())
            self.assertEqual(my_module1.export, my_module2.export)
            self.assertEqual(my_module1, my_module2)

    def test_check_namespace(self):
        global global_module
        global_module = None
        self.assertTrue('global_module' in globals())

        with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
            tf.write_text('export = "anglerfish"')
            my_module1 = path2import(tf.as_posix(), 'global_module')
            global_module = my_module1

            my_module2 = path2import(tf.as_posix(), 'global_module', check_namespace=True)
            self.assertEqual(my_module2, global_module)

        with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
            tf.write_text('export = "anglerfish"')
            with pytest.raises(NamespaceConflictError):
                my_module3 = path2import(tf.as_posix(), name='os')
                print(my_module3)  # to avoid warning "assigned but never used"

            my_module4 = path2import(tf.as_posix(), name='os', ignore_exceptions=True) == None
            print(my_module4)  # to avoid warning "assigned but never used"

        del(global_module)
