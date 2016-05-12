#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Debug and Log Encodings and Check for root/administrator,return Bool."""


def make_root_check_and_encoding_debug():
    """Debug and Log Encodings and Check for root/administrator,return Bool."""
    log.debug("Python {0} on {1}.".format(python_version(), platform()))
    log.debug("STDIN Encoding: {0}.".format(sys.stdin.encoding))
    log.debug("STDERR Encoding: {0}.".format(sys.stderr.encoding))
    log.debug("STDOUT Encoding:{}".format(getattr(sys.stdout, "encoding", "")))
    log.debug("Default Encoding: {0}.".format(sys.getdefaultencoding()))
    log.debug("FileSystem Encoding: {0}.".format(sys.getfilesystemencoding()))
    log.debug("PYTHONIOENCODING Encoding: {0}.".format(
        os.environ.get("PYTHONIOENCODING", None)))
    os.environ["PYTHONIOENCODING"], sys.dont_write_bytecode = "utf-8", True
    if not sys.platform.startswith("windows"):  # root check
        if not os.geteuid():
            log.warning("Runing as root is not Recommended !.")
            return False
    elif sys.platform.startswith("windows"):  # administrator check
        if getuser().lower().startswith("admin"):
            log.warning("Runing as Administrator is not Recommended !.")
            return False
    return True
