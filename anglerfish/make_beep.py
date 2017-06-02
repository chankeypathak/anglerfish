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


def beep(waveform=(79, 45, 32, 50, 99, 113, 126, 127)):
    """Cross-platform Sound Playing with StdLib only,No Sound file required."""
    if sys.platform.startswith("win"):
        log.warning("Playing Sound Natively is not supported by this OS.")
        return False
    wavefile = gettempdir() / Path("beep.wav")
    repro = which("aplay" if sys.platform.startswith("linux") else "afplay")
    log.debug("Playing Sound: {0} ({0!r}) using {1}.".format(wavefile, repro))
    if not wavefile.is_file() or not os.access(wavefile.as_posix(), os.R_OK):
        with open(wavefile.as_posix(), "w+") as wave_file:
            for sample in range(0, 1000, 1):
                for wav in range(0, 8, 1):
                    wave_file.write(chr(waveform[wav]))
    return not bool(run("{repro} '{fyle}'".format(
        fyle=wavefile.as_posix(), repro=repro), shell=True).returncode)
