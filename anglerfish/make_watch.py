#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Watch a file path for changes run callback if modified. A WatchDog."""


import os
import time


def watch(file_path: str, callback=None, interval: int=60,
          backoff: int=1, timeout: int=None, repetitions: int=-1,
          silent: bool=False, logger: object=None) -> object:
    """Watch a file path for changes run callback if modified. A WatchDog."""
    if not silent:
        msg = f"Watching for any changes on the file path: { file_path }."
        logger.debug(msg) if logger else print(msg)
    previous, file_path = int(os.stat(file_path).st_mtime), str(file_path)
    _interval, msg = interval, f"Modification detected on path: { file_path }."
    end_time = time.time() + int(timeout) if timeout else None
    repetitions = int(repetitions) if repetitions > 0 else True
    while repetitions:
        if end_time and time.time() > end_time:
            raise  # Timeout!.
        actual = int(os.stat(file_path).st_mtime)
        if previous == actual:
            time.sleep(int(abs(interval)))
            interval *= backoff if backoff and backoff in range(1, 9) else 1
        else:
            previous, interval = actual, _interval
            if not silent:
                logger.debug(msg) if logger else print(msg)
            return callback(file_path) if callback else file_path
