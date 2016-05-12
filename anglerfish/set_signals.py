#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Force CTRL+C to work to quit the app."""


import signal


signal.signal(signal.SIGINT, signal.SIG_DFL)
