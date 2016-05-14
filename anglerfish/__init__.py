#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import atexit
import codecs
import functools
import glob
import logging
import os
import socket
import stat
import sys
import time
import traceback
import zipfile

from logging.handlers import TimedRotatingFileHandler
from copy import copy
from ctypes import byref, cdll, create_string_buffer
from datetime import datetime
from getpass import getuser
from json import dumps, loads
from platform import platform, python_version
from shutil import disk_usage, make_archive, rmtree
from subprocess import call
from tempfile import gettempdir
from time import sleep
from urllib import request
from webbrowser import open_new_tab

try:
    import resource
except ImportError:
    resource = None  # MS Window dont have resource


CONFIG, start_time = None, datetime.now()
F = "[%(asctime)s] %(levelname)s:%(name)s: %(message)s %(filename)s:%(lineno)d"


def __zip_old_logs(log_file):
    zip_file, filename = log_file + "s-old.zip", os.path.basename(log_file)
    log.debug("Compressing Old Rotated Logs on ZIP file: " + zip_file)
    logs = [_ for _ in os.listdir(os.path.dirname(log_file))
            if ".log." in _ and not _.endswith("-old.zip") and filename in _]
    with zipfile.ZipFile(zip_file, 'a', zipfile.ZIP_DEFLATED) as myzip:
        myzip.debug = 3  # Log ZIP inner working,and comment with datetime
        for fyle in logs:
            myzip.write(fyle)
            os.remove(os.path.join(os.path.dirname(log_file), fyle))
        myzip.printdir()
    return zip_file


def make_logger(name=str(os.getpid())):
    """Build and return a Logging Logger."""
    global log
    log_file = os.path.join(gettempdir(), str(name).lower().strip() + ".log")
    zip_file = log_file + "s-old.zip"
    comment = "{}'s Compressed Unused Old Rotated Logs since ~{}.".format(
        name.title(), datetime.now().isoformat()[:-7])
    if not os.path.isfile(zip_file):
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as myzip:
            myzip.comment = bytes(comment, encoding="utf-8")
    atexit.register(__zip_old_logs, log_file)  # ZIP Old Logs
    hand = TimedRotatingFileHandler(log_file, when='midnight', backupCount=99,
                                    encoding="utf-8")
    hand.setLevel(-1)
    hand.setFormatter(logging.Formatter(fmt=F, datefmt="%Y-%m-%d %H:%M:%S"))
    log = logging.getLogger()
    log.addHandler(hand)
    log.setLevel(-1)

    if not sys.platform.startswith("win") and sys.stderr.isatty():
        log.debug("Using Colored Logs on current Terminal (256 Colors).")
        def add_color_emit_ansi(fn):
            """Add methods we need to the class."""
            def new(*args):
                """Method overload."""
                if len(args) == 2:
                    new_args = (args[0], copy(args[1]))
                else:
                    new_args = (args[0], copy(args[1]), args[2:])
                if hasattr(args[0], 'baseFilename'):
                    return fn(*args)
                levelno = new_args[1].levelno
                if levelno >= 50:
                    color = '\x1b[31;5;7m\n '  # blinking red with black
                elif levelno >= 40:
                    color = '\x1b[31m'  # red
                elif levelno >= 30:
                    color = '\x1b[33m'  # yellow
                elif levelno >= 20:
                    color = '\x1b[32m'  # green
                elif levelno >= 10:
                    color = '\x1b[35m'  # pink
                else:
                    color = '\x1b[0m'  # normal
                try:
                    new_args[1].msg = color + str(new_args[1].msg) + ' \x1b[0m'
                except Exception as reason:
                    print(reason)  # Do not use log here.
                return fn(*new_args)
            return new
        logging.StreamHandler.emit = add_color_emit_ansi(logging.StreamHandler.emit)

    logging.getLogger().addHandler(logging.StreamHandler(sys.stderr))
    adrs = "/dev/log" if sys.platform.startswith("lin") else "/var/run/syslog"
    try:
        handler = logging.handlers.SysLogHandler(address=adrs)
    except Exception:
        log.debug("Unix SysLog Server not found, ignored Logging to SysLog.")
    else:
        logging.getLogger().addHandler(handler)
        log.debug("Unix SysLog Server found,trying to Log to SysLog: " + adrs)
    log.debug("Logger created with Log file at: {0}.".format(log_file))
    return log


from anglerfish.check_encoding import *  # noqa lint
from anglerfish.check_updates import *  # noqa lint
from anglerfish.check_working_folder import *  # noqa lint
from anglerfish.get_clipboard import *  # noqa lint
from anglerfish.get_pdb_on_exception import *  # noqa lint
from anglerfish.make_atomic import *  # noqa lint
from anglerfish.make_beep import *  # noqa lint
from anglerfish.make_config import *  # noqa lint
from anglerfish.make_info import *  # noqa lint
from anglerfish.make_json_pretty import *  # noqa lint
from anglerfish.make_log_exception import *  # noqa lint
from anglerfish.make_multiprocess import *  # noqa lint
from anglerfish.make_multithread import *  # noqa lint
from anglerfish.make_postexec_message import *  # noqa lint
from anglerfish.make_progressbar import *  # noqa lint
from anglerfish.make_retry import *  # noqa lint
from anglerfish.make_typecheck import *  # noqa lint
from anglerfish.make_walkdir import *  # noqa lint
from anglerfish.make_watch import *  # noqa lint
from anglerfish.set_desktop_launcher import *  # noqa lint
from anglerfish.set_process_name import *  # noqa lint
from anglerfish.set_signals import *  # noqa lint
from anglerfish.set_single_instance import *  # noqa lint
from anglerfish.set_temp_folder import *  # noqa lint
from anglerfish.set_terminal_title import *  # noqa lint
