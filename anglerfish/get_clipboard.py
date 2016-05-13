#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Determine OS and set copy() and paste() functions accordingly."""


import logging as log
import os
import sys

from getpass import getuser
import subprocess


def __osx_clipboard():
    def copy_osx(text):
        subprocess.Popen(["pbcopy"], stdin=subprocess.PIPE,
                         close_fds=True).communicate(text.encode("utf-8"))

    def paste_osx():
        os.environ["LANG"] = "en_US.utf-8"
        return str(subprocess.Popen(
            ["pbpaste"], stdout=subprocess.PIPE, close_fds=True
            ).communicate()[0].decode("utf-8"))

    return copy_osx, paste_osx


def __gtk_clipboard():
    import gtk

    def copy_gtk(text):
        global cb
        cb = gtk.Clipboard()
        cb.set_text(text)
        cb.store()

    def paste_gtk():
        return gtk.Clipboard().wait_for_text()

    return copy_gtk, paste_gtk


def __qt_clipboard():
    from PyQt5.QtGui import QApplication
    app = QApplication([])

    def copy_qt(text):
        cb = app.clipboard()
        cb.setText(text)

    def paste_qt():
        cb = app.clipboard()
        return text_type(cb.text())

    return copy_qt, paste_qt


def __tkinter_clibboard():
    from Tkinter import Tk

    def copy_tk(text):
        """Copy given text into system clipboard."""
        window = Tk()
        window.withdraw()
        window.clipboard_clear()
        window.clipboard_append(text)
        window.destroy()

    def paste_tk():
        """Returns system clipboard contents."""
        window = Tk()
        window.withdraw()
        d = window.selection_get(selection = 'CLIPBOARD')
        return d

    return copy_tk, paste_tk


def __xclip_clipboard():
    def copy_xclip(text):
        subprocess.Popen(["xclip", "-selection", "clipboard"],
                         stdin=subprocess.PIPE, close_fds=True).communicate(
                         text.encode('utf-8'))
        if which("xsel"):
            subprocess.Popen(["xclip", "-selection", "primary"],
                             stdin=subprocess.PIPE, close_fds=True
                             ).communicate(text.encode('utf-8'))

    def paste_xclip():
        return subprocess.Popen(["xclip", "-selection",
                                "primary" if which("xsel") else "clipboard",
                                "-o"], stdout=subprocess.PIPE, close_fds=True
                                ).communicate()[0].decode("utf-8")

    return copy_xclip, paste_xclip


def __win32_clibboard():
    import win32clipboard
    import win32con

    def copy_win32(text):
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT, text)
        win32clipboard.CloseClipboard()

    def paste_win32():
        win32clipboard.OpenClipboard()
        text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
        win32clipboard.CloseClipboard()
        return text

    return copy_win32, paste_win32


def __determine_clipboard():
    """Determine OS and set copy() and paste() functions accordingly."""
    if sys.platform.startswith("darwin"):
        return __osx_clipboard()
    if sys.platform.startswith(("linux", "windows")):
        try:  # Determine which command/module is installed, if any.
            import win32clipboard  # check if win32clipboard is installed
        except ImportError:
            pass
        else:
            return __win32_clibboard()
        try:  # Determine which command/module is installed, if any.
            import gtk  # check if gtk is installed
        except ImportError:
            pass
        else:
            return __gtk_clipboard()
        try:
            assert bool(os.getenv("DISPLAY", False))  # Qt needs a DISPLAY
            import PyQt5  # check if PyQt5 is installed
        except ImportError, Exception:
            pass
        else:
            return __qt_clipboard()
        try:
            import Tkinter  # check if Tkinter is installed
        except ImportError:
            pass
        else:
            return __tk_clipboard()
    if sys.platform.startswith("linux") and which("xclip"):
        return __xclip_clipboard()
    else:
        return None, None  # install Qt or GTK or Tk or XClip.


def get_clipboard():
    """Crossplatform crossdesktop Clipboard."""
    global clipboard_copy, clipboard_paste
    clipboard_copy, clipboard_paste = None, None
    clipboard_copy, clipboard_paste = __determine_clipboard()
    return clipboard_copy, clipboard_paste
