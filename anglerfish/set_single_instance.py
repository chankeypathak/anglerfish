#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Set process name and cpu priority,return socket.socket or None."""


import logging as log
import socket
import sys


def set_single_instance(name: str, port: int=8_888) -> socket.socket:
    """Set process name and cpu priority,return socket.socket or None."""
    try:  # Single instance app ~crossplatform, uses udp socket.
        log.info("Creating Abstract UDP Socket Lock for Single Instance.")
        __lock = socket.socket(
            socket.AF_UNIX if sys.platform.startswith("linux")
            else socket.AF_INET, socket.SOCK_STREAM)
        __lock.bind(f"\0_{name}__lock" if sys.platform.startswith("linux")
                    else ("127.0.0.1", port))
    except (socket.error, OSError, Exception) as e:
        __lock = None
        log.critical("Another instance of App is already running!, Exiting!.")
        log.exception(e)
        sys.exit()
        exit()
        0 / 0  # should never reach here.
    else:
        log.info(f"Socket Lock for 1 Single App Instance: {__lock},{__lock!r}")
    finally:
        return __lock
