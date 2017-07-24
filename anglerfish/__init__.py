#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Anglerfish."""


import faulthandler
import logging
import sys
import signal
import time
import zipfile

from logging.handlers import TimedRotatingFileHandler
from copy import copy
from datetime import datetime
from pathlib import Path
from platform import platform, python_version, node
from tempfile import gettempdir
from random import choice

try:
    import resource
except ImportError:
    resource = None  # MS Window dont have resource


##############################################################################


from anglerfish.check_encoding import check_encoding  # noqa
from anglerfish.check_folder import check_folder  # noqa
from anglerfish.get_clipboard import get_clipboard  # noqa
from anglerfish.make_beep import beep  # noqa
from anglerfish.make_json_pretty import json_pretty  # noqa
from anglerfish.make_log_exception import log_exception  # noqa
from anglerfish.make_multiprocess import multiprocessed  # noqa
from anglerfish.make_multithread import threads  # noqa
from anglerfish.make_postexec_message import make_post_exec_msg, app_is_ready
from anglerfish.make_retry import retry  # noqa
from anglerfish.make_typecheck import typecheck  # noqa
from anglerfish.walk2list import walk2list  # noqa
from anglerfish.make_watch import watch  # noqa
from anglerfish.set_desktop_launcher import set_desktop_launcher  # noqa
from anglerfish.set_process_name import set_process_name  # noqa
from anglerfish.set_single_instance import set_single_instance  # noqa
from anglerfish.set_terminal_title import set_terminal_title  # noqa
from anglerfish.bytes2human import bytes2human  # noqa
from anglerfish.walk2dict import walk2dict  # noqa
from anglerfish.seconds2human import seconds2human, timedelta2human  # noqa
from anglerfish.html2ebook import html2ebook  # noqa
from anglerfish.make_template_python import TemplatePython  # noqa
from anglerfish.get_free_port import get_free_port  # noqa
from anglerfish.path2import import path2import  # noqa
from anglerfish.make_notification import make_notification  # noqa
from anglerfish.make_json_flat import make_json_flat  # noqa
from anglerfish.json2xml import json2xml  # noqa
from anglerfish.check_hardware import has_battery, on_battery  # noqa
from anglerfish.make_zip_comment import set_zip_comment, get_zip_comment  # noqa
from anglerfish.set_display_off import set_display_off  # noqa
from anglerfish.make_chainable_future import ChainableFuture  # noqa

from anglerfish.get_pdb_on_exception import (pdb_on_exception,  # noqa
                                             ipdb_on_exception)  # noqa
from anglerfish.string2stealth import string2stealth  # noqa
from anglerfish.stealth2string import stealth2string  # noqa
from anglerfish.exceptions import AnglerfishException
from anglerfish.get_public_ip import get_public_ip, is_online  # noqa
from anglerfish.set_process_priority import set_process_priority  # noqa
from anglerfish.get_random_pastel_color import (get_random_pastelight_color,
                                                get_random_pasteldark_color,
                                                get_random_pastel_color)
from anglerfish.get_random_font import (get_random_handwriting_font,
                                        get_random_mono_font,
                                        get_random_display_font,
                                        get_random_sans_font,
                                        get_random_serif_font,
                                        get_random_font)  # noqa
from anglerfish.make_datauri import DataURI, img2webp  # noqa
from anglerfish.get_human_datetime import get_human_datetime  # noqa
from anglerfish.make_async import Sync2Async  # noqa
from anglerfish.make_autochecksum import get_autochecksum, autochecksum  # noqa
from anglerfish.url2path import url2path  # noqa
from anglerfish.make_tinyslation import tinyslation  # noqa


##############################################################################


__version__ = "3.0.0"
__license__ = "GPLv3+ LGPLv3+"
__author__ = "Juan Carlos"
__email__ = "juancarlospaco@gmail.com"
__contact__ = "https://t.me/juancarlospaco"
__maintainer__ = "Juan Carlos"
__url__ = "https://github.com/juancarlospaco/anglerfish"
__all__ = (
    'ChainableFuture', 'TemplatePython', 'Sync2Async',  # Those are Classes.
    'beep', 'bytes2human', 'check_encoding', 'check_folder',
    'get_clipboard', 'get_free_port', 'app_is_ready', 'url2path',
    'get_autochecksum', 'autochecksum',  # Functions.
    'get_zip_comment', 'has_battery', 'html2ebook',
    'ipdb_on_exception', 'json2xml', 'json_pretty', 'log_exception',
    'make_json_flat', 'make_logger', 'make_notification', 'make_post_exec_msg',
    'multiprocessed', 'on_battery', 'path2import', 'pdb_on_exception',
    'retry', 'seconds2human', 'set_desktop_launcher',
    'set_display_off', 'set_process_name', 'set_single_instance',
    'set_terminal_title', 'set_zip_comment', 'threads',
    'timedelta2human', 'typecheck', 'walk2dict', 'walk2list', 'watch',
    'string2stealth', 'stealth2string',
    'get_public_ip', 'is_online', 'set_process_priority',
    'get_random_pastelight_color', 'get_random_pasteldark_color',
    'get_random_pastel_color', 'get_random_handwriting_font',
    'get_random_mono_font', 'get_random_display_font', 'get_random_sans_font',
    'get_random_serif_font', 'get_random_font', 'DataURI', 'img2webp',
    'get_human_datetime', 'tinyslation',
    'AnglerfishException',  # Exceptions
)


sys.dont_write_bytecode = True
signal.signal(signal.SIGINT, signal.SIG_DFL)


##############################################################################


_LOG_FORMAT = (
    "%(asctime)s %(levelname)s: %(processName)s (%(process)d) %(threadName)s "
    "(%(thread)d) %(name)s.%(funcName)s: %(message)s %(pathname)s:%(lineno)d")


class _ZipRotator(object):

    """Log Rotator with ZIP compression."""

    def __call__(self, origin, target, *args, **kwargs):
        """Log Rotator with ZIP compression, comments, checksum and cipher."""
        origin, target = Path(origin), Path(target + ".zip")
        comment = bytes(f"""ZIP Compressed Unused Old Rotated Python Logs.
            From {node()}, {platform()}, Python {python_version()} to {target}
            at ~{get_human_datetime()} ({datetime.now()}).""".encode("utf-8"))
        with zipfile.ZipFile(target.as_posix(), 'w', compression=8) as log_zip:
            log_zip.comment, log_zip.debug = comment, 3  # ZIP debug
            log_zip.write(origin.as_posix(), arcname=origin.name)
            log_zip.printdir()
            origin.unlink()


class SizedTimedRotatingFileHandler(TimedRotatingFileHandler):

    """TimedRotatingFileHandler with added file size based rotation."""

    def __init__(self, filename, maxMegaBytes=0, backupCount=0, encoding=None,
                 delay=0, when='h', interval=1, utc=False, atTime=None):
        """Overwrite the method shouldRollover."""
        TimedRotatingFileHandler.__init__(
            self, filename=filename, when=when, interval=interval,
            backupCount=backupCount, encoding=encoding, delay=delay, utc=utc)
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
                backupCount=100, encoding="utf-8", delay=False, utc=False,
                atTime=None, level=-1, slog=True, stder=True, crashandler=None,
                emoji=False, color=True, maxMegaBytes=1, *args, **kwargs):
    """Build and return a Logging Logger."""
    global log
    if not filename:
        filename = str(gettempdir() / Path(name.lower() + ".log"))
    # Handler with Rotator and Renamer.
    handler = SizedTimedRotatingFileHandler(
        filename=filename, when=when, interval=interval, delay=False,
        backupCount=backupCount, encoding=encoding, utc=utc, atTime=atTime,
        maxMegaBytes=maxMegaBytes)
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
    log.debug("""ZIP-Compressed Timed-Rotating and FileSize-Rotating Logger.
              Logger Log files write to: {filename}  ({filename!r}).""")
    return log
