#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Check working folder,from argument,for everything that can go wrong."""


import logging as log
import os

from pathlib import Path
from shutil import disk_usage

try:
    from anglerfish.bytes2human import bytes2human
except ImportError:
    from anglerfish import bytes2human


def check_folder(folder_to_check=Path.home().as_posix(), check_space=1):
    """Check working folder,from argument,for everything that can go wrong."""
    folder = Path(str(folder_to_check))
    m = "Folder {0} ({0!r}) free space {1} ({2} Bytes) of Minimum {3} GigaByte"
    log.debug("Checking Working Folder: {0} ({0!r}).".format(folder))
    if not folder.is_dir():  # What if folder not a folder.
        log.critical("Folder does not exist: {0} ({0!r}).".format(folder))
        return False
    elif not os.access(folder.as_posix(), os.R_OK):  # What if not Readable.
        log.critical("Folder not readable: {0} ({0!r}).".format(folder))
        return False
    elif not os.access(folder.as_posix(), os.W_OK):  # What if not Writable.
        log.critical("Folder not writable: {0} ({0!r}).".format(folder))
        return False
    elif disk_usage and folder.exists() and bool(check_space):
        hdd = int(disk_usage(folder.as_posix()).free)
        if int(hdd / 1_024 / 1_024 / 1_024) >= int(check_space):  # Check_space
            log.info(m.format(
                folder, bytes2human(hdd), hdd, check_space))
            return True
        else:  # < check_space Gb.
            log.critical(m.format(
                folder, bytes2human(hdd), hdd, check_space))
            return False
    return False
