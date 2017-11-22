#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tests for path2import."""


import unittest
from pathlib import Path
from random import randint
from tempfile import NamedTemporaryFile

from anglerfish import path2import


# Random order for tests runs. (Original is: -1 if x<y, 0 if x==y, 1 if x>y).
unittest.TestLoader.sortTestMethodsUsing = lambda _, x, y: randint(-1, 1)


class TestName(unittest.TestCase):

    maxDiff, __slots__ = None, ()

    def test_normal(self):
        with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
            tf.write_text('export = "anglerfish"')
            my_module = path2import(tf.as_posix())
            self.assertEqual(my_module.export, 'anglerfish')

    def test_syntax_error(self):
        with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
            tf.write_text('export = ')
            with self.assertRaises(SyntaxError):
                my_module = path2import(tf.as_posix())
                print(my_module)  # to avoid warning "assigned but never used"

            self.assertIsNone(path2import(tf.as_posix(), ignore_exceptions=True))

    def test_permission_denied(self):
        pass
        # FIXME: this should work, why is not working ?.
        # with Path(NamedTemporaryFile("w", suffix=".py", delete=False).name) as tf:
        #     os.chmod(tf.as_posix(), 0o400)  # Reduce file permissions to non-readable
        #     with self.assertRaises(PermissionError):
        #         my_module = path2import(tf.as_posix())
        #         self.assertEqual(my_module.export, 'anglerfish')

    def test_not_found(self):
        with self.assertRaises(ModuleNotFoundError):
            my_module = path2import('not_existed_module.py')
            print(my_module)  # to avoid warning "assigned but never used"

        self.assertIsNone(path2import('not_existed_module.py', ignore_exceptions=True))

    def test_invaild_module(self):
        with Path(NamedTemporaryFile("w", suffix=".txt", delete=False).name) as tf:
            tf.write_text('export = "anglerfish"')  # Not a .py module.
            with self.assertRaises(ImportError):
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
            with self.assertRaises(ImportWarning):
                my_module3 = path2import(tf.as_posix(), name='os')
                print(my_module3)  # to avoid warning "assigned but never used"

            my_module4 = path2import(
                tf.as_posix(), name='os', ignore_exceptions=True) is None
            print(my_module4)  # to avoid warning "assigned but never used"

        del(global_module)


if __name__.__contains__("__main__"):
    print(__doc__)
    unittest.main()
