#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Make a automagic-checksuming file using Adler32 Hash and Hexadecimal.

Resulting on a short ~8 character checksum added to the filename,
easy to parse with standard pattern,not crypto secure but useful for checksum,
is more human friendly than SHA512 checksum and its builtin on the filename,
Adler32 is standard on all ZIP files and its builtin on Python std lib.
I do this tired of people not using SHA512 on 1 separate txt file for checksum,
this not require user command line skills to check the checksum, its automagic.
"""


from pathlib import Path
from zlib import adler32


_STANDARD_PATTERN = ".✔"  # (check mark) use this to signal a selfchecksum


def get_autochecksum(filepath: str, pattern: str=_STANDARD_PATTERN) -> str:
    """Get a standard autochecksum string from file path argument."""
    return pattern + hex(adler32(Path(filepath).read_bytes()) & 0xffffffff)[2:]


def autochecksum(filepath: str, update: bool=False) -> str:
    """Make a automagic-checksuming file using Adler32 Hash and Hexadecimal."""
    filepath = Path(filepath)
    ext = "".join((_ for _ in filepath.suffixes if _STANDARD_PATTERN not in _))
    checksum = get_autochecksum(filepath.as_posix())  # Get a selfchecksum str.
    if _STANDARD_PATTERN in filepath.as_posix() and filepath.is_file():
        if checksum in filepath.as_posix():
            return True  # File SelfChecksum is Ok, Integrity is Ok.
        elif checksum not in filepath.as_posix() and not update:
            return False  # File SelfChecksum is Wrong, Integrity is NOT Ok.
        elif checksum not in filepath.as_posix() and update:
            new_file = "{0}{1}{2}".format(
                filepath.as_posix().split(_STANDARD_PATTERN)[0], checksum, ext)
            filepath.rename(new_file)
            return new_file  # SelfChecksum Wrong,Update checksum.
    elif filepath.is_file():  # File has no selfchecksum,get selfchecksum
        new_file = "{0}{1}{2}".format(
            filepath.as_posix().replace(ext, ""), checksum, ext)
        filepath.rename(new_file)
        return new_file
