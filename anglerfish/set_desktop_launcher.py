#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Add to autostart or launcher icon on the Desktop."""


import logging as log
import os
import sys


def set_desktop_launcher(app, desktop_file_content, autostart=False):
    """Add to autostart or launcher icon on the Desktop."""
    if not sys.platform.startswith("linux"):
        return  # .desktop files are Linux only AFAIK.
    config_dir = os.path.join(os.path.expanduser("~"), ".config", "autostart")
    autostart_file = os.path.join(config_dir, app + ".desktop")
    if os.path.isdir(config_dir) and not os.path.isfile(autostart_file):
        if autostart:
            log.info("Writing Auto-Start file: " + autostart_file)
            with open(autostart_file, "w", encoding="utf-8") as start_file:
                start_file.write(desktop_file_content)
    apps_dir = os.path.join(os.path.expanduser("~"),
                            ".local", "share", "applications")
    desktop_file = os.path.join(apps_dir, app + ".desktop")
    if os.path.isdir(apps_dir) and not os.path.isfile(desktop_file):
        log.info("Writing Desktop Launcher file: " + desktop_file)
        with open(desktop_file, "w", encoding="utf-8") as desktop_file_obj:
            desktop_file_obj.write(desktop_file_content)
    return desktop_file
