#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Anglerfish."""


import faulthandler
import logging
import signal
import sys
import time
import zipfile

from copy import copy
from datetime import datetime
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from platform import node, platform, python_version
from random import choice
from tempfile import gettempdir

try:
    import resource
except ImportError:
    resource = None  # MS Window dont have resource


##############################################################################


from anglerfish.autoslots_meta import AutoSlots_meta  # noqa
from anglerfish.bytes2human import bytes2human  # noqa
from anglerfish.check_encoding import check_encoding  # noqa
from anglerfish.check_folder import check_folder  # noqa
from anglerfish.check_hardware import has_battery, on_battery  # noqa
from anglerfish.exceptions import AnglerfishException
from anglerfish.get_clipboard import get_clipboard  # noqa
from anglerfish.get_free_port import get_free_port  # noqa
from anglerfish.get_pdb_on_exception import ipdb_on_exception  # noqa
from anglerfish.get_pdb_on_exception import pdb_on_exception  # noqa
from anglerfish.get_public_ip import get_public_ip, is_online  # noqa
from anglerfish.get_random_font import get_random_font  # noqa
from anglerfish.get_random_font import (get_random_display_font,
                                        get_random_handwriting_font,
                                        get_random_mono_font,
                                        get_random_sans_font,
                                        get_random_serif_font)
from anglerfish.get_random_pastel_color import (get_random_pastel_color,
                                                get_random_pasteldark_color,
                                                get_random_pastelight_color)
from anglerfish.html2ebook import html2ebook  # noqa
from anglerfish.json2xml import json2xml  # noqa
from anglerfish.make_async import Sync2Async  # noqa
from anglerfish.make_autochecksum import autochecksum, get_autochecksum  # noqa
from anglerfish.make_beep import beep  # noqa
from anglerfish.make_chainable_future import ChainableFuture  # noqa
from anglerfish.make_datauri import DataURI, img2webp  # noqa
from anglerfish.make_json_flat import make_json_flat  # noqa
from anglerfish.make_json_pretty import json_pretty  # noqa
from anglerfish.make_log_exception import log_exception  # noqa
from anglerfish.make_multiprocess import multiprocessed  # noqa
from anglerfish.make_multithread import threads  # noqa
from anglerfish.make_notification import make_notification  # noqa
from anglerfish.make_postexec_message import app_is_ready, make_post_exec_msg
from anglerfish.make_retry import retry  # noqa
from anglerfish.make_template_python import TemplatePython  # noqa
from anglerfish.make_tinyslation import tinyslation  # noqa
from anglerfish.make_typecheck import typecheck  # noqa
from anglerfish.make_watch import watch  # noqa
from anglerfish.make_zip_comment import (get_zip_comment,  # noqa
                                         set_zip_comment)
from anglerfish.path2import import path2import  # noqa
from anglerfish.seconds2human import (datetime2human, now2human,  # noqa
                                      timedelta2human, timestamp2human)
from anglerfish.set_desktop_launcher import set_desktop_launcher  # noqa
from anglerfish.set_display_off import set_display_off  # noqa
from anglerfish.set_process_name import set_process_name  # noqa
from anglerfish.set_process_priority import set_process_priority  # noqa
from anglerfish.set_single_instance import set_single_instance  # noqa
from anglerfish.set_terminal_title import set_terminal_title  # noqa
from anglerfish.stealth2string import stealth2string  # noqa
from anglerfish.string2stealth import string2stealth  # noqa
from anglerfish.url2path import url2path  # noqa
from anglerfish.walk2dict import walk2dict  # noqa
from anglerfish.walk2list import walk2list  # noqa


##############################################################################


__version__ = "3.0.0"
__license__ = "GPLv3+ LGPLv3+"
__author__ = "Juan Carlos"
__email__ = "juancarlospaco@gmail.com"
__contact__ = "https://t.me/juancarlospaco"
__maintainer__ = "Juan Carlos"
__url__ = "https://github.com/juancarlospaco/anglerfish"
__all__ = (
    'AnglerfishException',  # Exceptions.
    'AutoSlots_meta',       # MetaClasses.
    'ChainableFuture', 'DataURI', 'Sync2Async', 'TemplatePython',  # Classes.
    'app_is_ready', 'autochecksum', 'beep', 'bytes2human',         # Functions.
    'check_encoding', 'check_folder', 'datetime2human', 'get_autochecksum',
    'get_clipboard', 'get_free_port', 'get_public_ip',
    'get_random_display_font', 'get_random_font',
    'get_random_handwriting_font', 'get_random_mono_font',
    'get_random_pastel_color', 'get_random_pasteldark_color',
    'get_random_pastelight_color', 'get_random_sans_font',
    'get_random_serif_font', 'get_zip_comment', 'has_battery', 'html2ebook',
    'img2webp', 'ipdb_on_exception', 'is_online', 'json2xml', 'json_pretty',
    'log_exception', 'make_json_flat', 'make_logger', 'make_notification',
    'make_post_exec_msg', 'multiprocessed', 'now2human', 'on_battery',
    'path2import', 'pdb_on_exception', 'retry', 'set_desktop_launcher',
    'set_display_off', 'set_process_name', 'set_process_priority',
    'set_single_instance', 'set_terminal_title', 'set_zip_comment',
    'stealth2string', 'string2stealth', 'threads', 'timedelta2human',
    'timestamp2human', 'tinyslation', 'typecheck', 'url2path', 'walk2dict',
    'walk2list', 'watch',
)


sys.dont_write_bytecode = True
signal.signal(signal.SIGINT, signal.SIG_DFL)


##############################################################################


_LOG_FORMAT = (
    "%(asctime)s %(levelname)s: %(processName)s (%(process)d) %(threadName)s "
    "(%(thread)d) %(name)s.%(funcName)s: %(message)s %(pathname)s:%(lineno)d")


class _ZipRotator(object):

    """Log Rotator with ZIP compression."""
    __slots__ = ("origin", "target")

    def __call__(self, origin, target):
        """Log Rotator with ZIP compression, comments, checksum and cipher."""
        origin, target = Path(origin), Path(target + ".zip")
        comment = bytes(f"""ZIP Compressed Unused Old Rotated Python Logs.
            From {node()}, {platform()}, Python {python_version()} to {target}
            at ~{now2human().human} ({datetime.now()}).""".encode("utf-8"))
        with zipfile.ZipFile(target, 'w', compression=8) as log_zip:
            log_zip.comment, log_zip.debug = comment, 3  # ZIP debug
            log_zip.write(origin.as_posix(), arcname=origin.name)
            log_zip.printdir()
            origin.unlink()
        return target

    def __setattr__(self, *args, **kwargs):
        raise TypeError("Internal _ZipRotator object is inmmutable read-only.")

    def __delattr__(self, *args, **kwargs):
        raise TypeError("Internal _ZipRotator object is inmmutable read-only.")


class SizedTimedRotatingFileHandler(TimedRotatingFileHandler):

    """TimedRotatingFileHandler with added file size based rotation."""
    __slots__ = ("filename", "maxMegaBytes", "backupCount",
                 "delay", "when", "interval", "utc", "atTime")

    def __init__(self, filename, maxMegaBytes=0, backupCount=0,
                 delay=0, when='h', interval=1, utc=False, atTime=None):
        """Overwrite the method shouldRollover."""
        TimedRotatingFileHandler.__init__(
            self, filename=filename, when=when, interval=interval,
            backupCount=backupCount, encoding="utf-8", delay=delay, utc=utc)
        self.maxMegaBytes = int(abs(maxMegaBytes))  # Extra class attribute.

    def shouldRollover(self, record):
        """Determine if rollover should occur."""
        if self.stream is None:  # Delay was set.
            self.stream = self._open()
        if self.maxMegaBytes > 0:  # Are we rolling over?.
            msg = str(self.format(record))
            self.stream.seek(0, 2)  # Non-posix-compliant Windows feature.
            if self.stream.tell() + len(msg) > self.maxMegaBytes * 1024 * 1024:
                return 1
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        return 0


def make_logger(name, when='midnight', filename=None, interval=1,
                backupCount=100, delay=False, utc=False,
                atTime=None, level=-1, slog=True, stder=True, crashandler=None,
                emoji=False, color=True, maxMegaBytes=1, *args, **kwargs):
    """Build and return a Logging Logger."""
    global log
    if not filename:
        filename = str(gettempdir() / Path(name.lower() + ".log"))
    # Handler with Rotator and Renamer.
    handler = SizedTimedRotatingFileHandler(
        filename=filename, when=when, interval=interval, delay=False, utc=utc,
        backupCount=backupCount, atTime=atTime, maxMegaBytes=maxMegaBytes)
    handler.setLevel(level)
    handler.setFormatter(logging.Formatter(
        fmt=_LOG_FORMAT, datefmt=r"%Y-%m-%d %H:%M:%S%z"))
    handler.rotator = _ZipRotator
    log = logging.getLogger()
    log.addHandler(handler)
    log.setLevel(level)
    # Colors and Emoji.
    if not sys.platform.startswith("win") and sys.stderr.isatty() and color:
        log.debug("Colored Logs on current Terminal enabled.")

        def add_color_emit_ansi(fn):
            """Add methods we need to the class."""
            def new(*args):
                """Overload."""
                if len(args) == 2:
                    new_args = (args[0], copy(args[1]))
                else:
                    new_args = (args[0], copy(args[1]), args[2:])
                if hasattr(args[0], 'baseFilename'):
                    return fn(*args)
                levelno, end = new_args[1].levelno, ' \x1b[0m'
                if levelno >= 50:
                    color = '\x1b[31;5;7m\n '  # blinking red with black
                    if emoji:
                        end += choice((' 😿\n', ' 🙀\n', ' 💩\n', ' ☠\n', ''))
                elif levelno >= 40:
                    color = '\x1b[31m'  # red
                    if emoji:
                        end += choice((' 😾 ', ' 😼 ', ''))
                elif levelno >= 30:
                    color = '\x1b[33m'  # yellow
                    if emoji:
                        end += choice((' 😺 ', ' 😻 ', ''))
                elif levelno >= 20:
                    color = '\x1b[32m'  # green
                    if emoji:
                        end += choice((' 😸 ', ' 😽 ', ''))
                elif levelno >= 10:
                    color = '\x1b[35m'  # pink
                    if emoji:
                        end += choice((' 🐱 ', ' 😹 ', ''))
                else:
                    color = '\x1b[0m'  # normal
                try:
                    new_args[1].msg = color + str(new_args[1].msg) + end
                except Exception as reason:
                    print(reason)  # Do not use log here.
                return fn(*new_args)
            return new
        logging.StreamHandler.emit = add_color_emit_ansi(
            logging.StreamHandler.emit)
    # Std Error.
    if stder:
        log.addHandler(logging.StreamHandler(sys.stderr))
    # SysLog server.
    if Path("/dev/log").exists() or Path("/var/run/syslog").exists() and slog:
        is_linux = sys.platform.startswith("linux")
        addrss = Path("/dev/log" if is_linux else "/var/run/syslog").as_posix()
        try:
            handler = logging.handlers.SysLogHandler(address=str(addrss))
            handler.setFormatter(logging.Formatter(
                fmt=_LOG_FORMAT, datefmt=r"%Y-%m-%d %H:%M:%S%z"))
        except Exception:
            log.debug("Unix SysLog Server not found,ignore Logging to SysLog.")
        else:
            log.addHandler(handler)
            log.debug(f"Unix SysLog Server Logs to: {addrss} ({addrss!r}).")
    # Fault handler.
    if crashandler:
        try:
            faulthandler.enable(crashandler)
        except Exception as error:
            log.waring(f"FaultHander {crashandler} Failed with error: {error}")
        else:
            log.debug(f"FaultHander ON!, Logs Fatal Errors to: {crashandler}.")
    log.debug(f"""ZIP-Compressed Timed-Rotating and FileSize-Rotating Logger.
              Logger Log files write to: {filename}  ({filename!r}).""")
    return log
