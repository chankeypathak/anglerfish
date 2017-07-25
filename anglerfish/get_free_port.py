#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Get and return a free unused port."""


import logging as log
import socket


def get_free_port(port_range=None):
    """Get and return a free unused port."""
    sockety = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockety.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if port_range and isinstance(port_range, tuple) and len(port_range) == 2:
        for port_number in range(int(port_range[0]), int(port_range[1])):
            try:  # Free port from a User-Provided range of ports,good for Doc.
                sockety.bind(("127.0.0.1", port_number))
            except (socket.error, Exception):
                pass
            else:
                sockety.close()
                del sockety
                log.debug(f"Found 1 free unused port number: { port_number }.")
                return port_number
    else:  # OS-Provided Random free port,good for best practice.
        sockety.bind(("", 0))
        port_number = sockety.getsockname()[1]
        sockety.close()
        del sockety
        log.debug(f"Found 1 free unused port number: { port_number }.")
        return port_number
