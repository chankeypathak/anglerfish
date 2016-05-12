 #!/usr/bin/env python3
 # -*- coding: utf-8 -*-


 import functools
 import logging as log
 import os
 import socket
 import stat
 import sys
 import traceback

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


 def make_logger(name=str(os.getpid())):
     """Build and return a Logging Logger."""
     if not sys.platform.startswith("win") and sys.stderr.isatty():
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
         log.StreamHandler.emit = add_color_emit_ansi(log.StreamHandler.emit)
     log_file = os.path.join(gettempdir(), str(name).lower().strip() + ".log")
     log.basicConfig(level=-1, filemode="w", filename=log_file)
     log.getLogger().addHandler(log.StreamHandler(sys.stderr))
     adrs = "/dev/log" if sys.platform.startswith("lin") else "/var/run/syslog"
     try:
         handler = log.handlers.SysLogHandler(address=adrs)
     except Exception:
         log.debug("Unix SysLog Server not found, ignored Logging to SysLog.")
     else:
         log.getLogger().addHandler(handler)
     log.debug("Logger created with Log file at: {0}.".format(log_file))
     return log
