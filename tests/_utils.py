#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Utils for testing, this module should not raise exceptions'''

import tempfile
import os

class TempFile:
    '''Make it easier to operate temp files'''
    def __init__(self, content=None, mode='w', suffix='.py', path=None):
        self.mode = mode
        if path is None:
            self.file = tempfile.NamedTemporaryFile(self.mode, suffix=suffix, delete=False)
            self.name = self.file.name
        else:
            self.name = path
            self.file = open(self.name, self.mode)

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
