#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Watch a file path for changes run callback if modified. A WatchDog."""


def watch(file_path, callback=None):
    """Watch a file path for changes run callback if modified. A WatchDog."""
    log.debug("Watching for changes on path: {0}.".format(file_path))
    previous = int(os.stat(file_path).st_mtime)
    while True:
        actual = int(os.stat(file_path).st_mtime)
        if previous == actual:
            time.sleep(60)
        else:
            previous = actual
            log.debug("Modification detected on {0}.".format(file_path))
            return callback(file_path) if callback else file_path
