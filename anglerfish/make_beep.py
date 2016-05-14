#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Cross-platform Sound Playing with StdLib only,No Sound file required."""


import logging as log
import os
import sys

from subprocess import call
from tempfile import gettempdir


def beep(waveform=(79, 45, 32, 50, 99, 113, 126, 127)):
    """Cross-platform Sound Playing with StdLib only,No Sound file required."""
    log.debug("Generating and Playing Sound...")
    wavefile = os.path.join(gettempdir(), "beep.wav")
    if not os.path.isfile(wavefile) or not os.access(wavefile, os.R_OK):
        with open(wavefile, "w+") as wave_file:
            for sample in range(0, 1000, 1):
                for wav in range(0, 8, 1):
                    wave_file.write(chr(waveform[wav]))
    if sys.platform.startswith("linux"):
        return call("chrt -i 0 aplay '{fyle}'".format(fyle=wavefile), shell=1)
    if sys.platform.startswith("darwin"):
        return call("afplay '{fyle}'".format(fyle=wavefile), shell=True)
    if sys.platform.startswith("win"):  # FIXME: This is Ugly.
        return call("start /low /min '{fyle}'".format(fyle=wavefile), shell=1)


# def music8bit():
#     """Crossplatform Sound Playing with StdLib only,No Sound file required."""
#     log.debug("Generating and Playing 8-Bit Music...")
#     wavefile = os.path.join(gettempdir(), "8bit_music.wav")
#     music = "".join([str(
#         (t >> 15 & (t >> (2 if (t % 2) else 4)) %
#         (3 + (t >> (8 if (t % 2) else 11)) % 4) +
#         (t >> 10) | 42 & t >> 7 & t << 9))
#         for t in range(2 ** 20)
#     ])
#     if not os.path.isfile(wavefile) or not os.access(wavefile, os.R_OK):
#         with open(wavefile, "w") as wave_file:
#             wave_file.write(music)
#     if sys.platform.startswith("linux"):
#         return call("aplay -c2 -r4 '{fyle}'".format(fyle=wavefile), shell=1)
#     if sys.platform.startswith("darwin"):
#         return call("afplay '{fyle}'".format(fyle=wavefile), shell=True)
#     if sys.platform.startswith("win"):  # FIXME: This is Ugly.
#         return call("start /low /min '{fyle}'".format(fyle=wavefile), shell=1)
