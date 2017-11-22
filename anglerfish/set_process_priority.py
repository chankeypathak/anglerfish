#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Set process I/O and cpu priority."""


import atexit
import logging as log
import os
from shutil import which
from subprocess import Popen, call


def set_process_priority(nice: bool=True, ionice: bool=False,
                         cpulimit: int=0) -> bool:
    """Set process name and cpu priority."""
    w = " may delay I/O Operations, not recommended on user-facing GUI!."
    try:
        if nice:
            _old = os.getpriority(os.PRIO_PROCESS, 0)
            os.nice(19)  # smooth cpu priority
            log.debug(f"Process CPUs Priority set: from {_old} to 19.")
        elif ionice and which("ionice"):
            log.warning("ionice" + w)
            cmnd = f"{which('ionice')} --ignore --class 3 --pid {os.getpid()}"
            call(cmnd, shell=True)  # I/O nice,should work on Linux and Os X
            log.debug(f"Process PID {os.getpid()} I/O Priority set to: {cmnd}")
        elif cpulimit and which("cpulimit"):
            log.warning("cpulimit" + w)
            log.debug("Launching 1 background 'cpulimit' child subprocess...")
            cpulimit = int(cpulimit if cpulimit > 4 else 5)  # makes 5 the min.
            command = "{0} --include-children --pid={1} --limit={2}".format(
                which("cpulimit"), os.getpid(), cpulimit)
            proces = Popen(command, shell=True)  # This launch a subprocess.
            atexit.register(proces.kill)  # Force Kill subprocess at exit.
            log.debug(f"Process CPUs Max Limits capped to: {command}.")
    except Exception as error:
        log.warning(error)
        return False  # this may fail on windows and its normal, so be silent.
    else:
        return True
