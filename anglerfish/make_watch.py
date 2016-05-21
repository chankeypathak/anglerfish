#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Watch a file path for changes run callback if modified. A WatchDog."""


import logging as log
import os
import stat

import time


def watch(file_path, callback=None, interval=60):
    """Watch a file path for changes run callback if modified. A WatchDog."""
    log.debug("Watching for changes on path: {0}.".format(file_path))
    previous, file_path = int(os.stat(file_path).st_mtime), str(file_path)
    while True:
        actual = int(os.stat(file_path).st_mtime)
        if previous == actual:
            time.sleep(int(abs(interval)))
        else:
            previous = actual
            log.debug("Modification detected on {0}.".format(file_path))
            return callback(file_path) if callback else file_path
