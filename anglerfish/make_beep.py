#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Cross-platform Sound Playing with StdLib only,No Sound file required."""


import logging as log
import os
import sys
from pathlib import Path
from shutil import which
from subprocess import run
from tempfile import gettempdir

try:
    from winsound import Beep
    from random import randint
except ImportError:
    Beep = None


def beep(waveform=(79, 45, 32, 50, 99, 113, 126, 127)):
    """Cross-platform Sound Playing with StdLib only,No Sound file required."""
    if sys.platform.startswith("win") and Beep:
        Beep(randint(37, 32_767), 3)
        return True  # https://docs.python.org/3.6/library/winsound.html
    wavefile = gettempdir() / Path("beep.wav")
    repro = which("aplay" if sys.platform.startswith("linux") else "afplay")
    log.debug(f"Playing Sound Beep: {wavefile} ({wavefile!r}) using {repro}.")
    if not wavefile.is_file() or not os.access(wavefile.as_posix(), os.R_OK):
        with open(wavefile.as_posix(), "w+") as wave_file:
            for sample in range(0, 1000, 1):
                for wav in range(0, 8, 1):
                    wave_file.write(chr(waveform[wav]))
    return not bool(run(f"{repro} '{wavefile}'", shell=True).returncode)
