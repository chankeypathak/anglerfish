#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Method to check for updates from Git repo versus this version."""


import logging as log
import socket
from urllib import request


def check_updates():
    """Method to check for updates from Git repo versus this version."""
    try:
        last_version = str(request.urlopen(__source__).read().decode("utf8"))
        this_version = str(open(__file__).read())
    except Exception as e:
        log.warning(e)
    else:
        if this_version != last_version:
            msg = "Theres a new Version!, update the App from: " + __source__
            log.warning(msg)
        else:
            msg = "No new updates!, You have the latest version of this app."
            log.info(msg)
        return msg
