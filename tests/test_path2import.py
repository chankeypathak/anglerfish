#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Tests for path2import'''

import pytest
import tempfile
import os
from anglerfish import path2import


class TempFile:
    '''Make it easier to operate temp files'''
    def __init__(self, content=None, mode='w', suffix='.py'):
        self.mode = mode
        self.file = tempfile.NamedTemporaryFile('w', suffix=suffix, delete=False)
        self.name = self.file.name

        if content != None:
            self.rewrite(content)

    def rewrite(self, content):
        if self.file.closed:
            self.file = open(self.name, self.mode)

        with self.file:
             self.file.write(content)

    def __enter__(self):
        return self

    def __exit__(self, exc, value, tb):
        self.remove()

    def remove(self):
        if os.path.exists(self.name):
            os.remove(self.name)


def test_normal():
    with TempFile('export = "anglerfish"') as tf:
        my_module = path2import(tf.name)
        assert my_module.export == 'anglerfish'

def test_syntax_error():
    with TempFile('export = ') as tf: # invaild python statements
        with pytest.raises(SyntaxError):
            my_module = path2import(tf.name)

        assert path2import(tf.name, ignore_exceptions=True) == None


def test_permission_denied():
    pass
    # TODO: Make a premission error case
    # with pytest.raises(PermissionError):
    #    my_module = path2import('permission_denied_module.py')

def test_not_found():
    with pytest.raises(FileNotFoundError):
        my_module = path2import('not_existed_module.py')

    assert path2import('not_existed_module.py', ignore_exceptions=True) == None


def test_is_directory():
    with pytest.raises(IsADirectoryError):
        my_module = path2import('anglerfish')

    assert path2import('anglerfish', ignore_exceptions=True) == None


def test_invaild_module():
    with TempFile('export = "anglerfish"', suffix='.txt') as tf: # not a .py module
        with pytest.raises(ImportError):
            my_module = path2import(tf.name)

        assert path2import(tf.name, ignore_exceptions=True) == None


def test_reimport():
    with TempFile('export = "anglerfish"') as tf:
        my_module1 = path2import(tf.name)
        assert my_module1.export == 'anglerfish'
        my_module2 = path2import(tf.name)
        assert my_module1.export == my_module2.export
        assert my_module1 == my_module2

def test_reload():
    with TempFile('export = "anglerfish"') as tf:
        my_module1 = path2import(tf.name)
        assert my_module1.export == 'anglerfish'

        tf.rewrite('export = "anglerfish2"')
        assert my_module1.export == 'anglerfish'
        my_module2 = path2import(tf.name)

        # The assertment below will fail.
        # Because "module1" and "module2" is actually a same instance,
        # the second time you call "path2import" it will update the "module1" as well

        # assert my_module1.export == 'anglerfish' # It's 'anglerfish2' actually

        assert my_module2.export == 'anglerfish2'
        assert my_module1 == my_module2
