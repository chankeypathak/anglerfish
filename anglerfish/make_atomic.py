#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Context manager with a writable file which will be moved into place
as long as no exceptions are raised within the context manager's block.
These "part files" are created in the same directory as the destination
path to ensure atomic move operations. Similar to Chrome Downloads."""


import logging as log
import os
import stat
import sys

from tempfile import gettempdir


def write_atomic(dest_path, **kwargs):
    """A convenient interface to AtomicWriter type."""
    log.debug("Atomic Writing File: {0}".format(dest_path))
    return AtomicWriter(dest_path, **kwargs)


def rename_atomic(path, new_path, overwrite=False):
    """Atomic rename of a path."""
    log.debug("Atomic Renaming File: from {0} to {1}.".format(path, new_path))
    if overwrite:
        os.rename(path, new_path)
    else:
        os.link(path, new_path)
        os.unlink(path)


_TEXT_OPENFLAGS = os.O_RDWR | os.O_CREAT | os.O_EXCL
if hasattr(os, 'O_NOINHERIT'):
    _TEXT_OPENFLAGS |= os.O_NOINHERIT
if hasattr(os, 'O_NOFOLLOW'):
    _TEXT_OPENFLAGS |= os.O_NOFOLLOW
_BIN_OPENFLAGS = _TEXT_OPENFLAGS
if hasattr(os, 'O_BINARY'):
    _BIN_OPENFLAGS |= os.O_BINARY

try:
    import fcntl as fcntl
except ImportError:
    def set_cloexec(fd):
        "Dummy set_cloexec for platforms without fcntl support."
        pass
else:
    def set_cloexec(fd):
        """Does a best-effort fcntl.fcntl call to set a fd to be
        automatically closed by any future child processes."""
        try:
            flags = fcntl.fcntl(fd, fcntl.F_GETFD, 0)
        except IOError:
            pass
        else:
            flags |= fcntl.FD_CLOEXEC  # flags read successfully, modify
            fcntl.fcntl(fd, fcntl.F_SETFD, flags)


class AtomicWriter(object):

    """context manager with a writable file which will be moved into place
    as long as no exceptions are raised within the context manager's block.
    These "part files" are created in the same directory as the destination
    path to ensure atomic move operations. Similar to Chrome Downloads.

    Args:
        dest_path (str): The path where the completed file will be written.
        overwrite (bool): overwrite destination file if exists. Defaults True.
        delete_part_if_fail (bool): Move *.part to temp folder if exception.
    """

    def __init__(self, dest_path, **kwargs):
        super(AtomicWriter, self).__init__(dest_path, **kwargs)
        self.dest_path = dest_path
        self.overwrite = kwargs.pop('overwrite', True)
        self.delete_part_if_fail = kwargs.pop('delete_part_if_fail', True)
        self.text_mode = kwargs.pop('text_mode', False)  # for windows
        self.dest_path = os.path.abspath(self.dest_path)
        self.dest_dir = os.path.dirname(self.dest_path)
        self.part_path = dest_path + '.part'
        self.mode = 'w+' if self.text_mode else 'w+b'
        self.open_flags = _TEXT_OPENFLAGS if self.text_mode else _BIN_OPENFLAGS
        self.part_file = None

    def _open_part_file(self):
        do_chmod = True
        try:
            stat_res = os.stat(self.dest_path)  # copy from file being replaced
            file_perms = stat.S_IMODE(stat_res.st_mode)
        except (OSError, IOError):
            file_perms = 0o644  # default if no file exists
            do_chmod = False  # respect the umask
        fd = os.open(self.part_path, self.open_flags, file_perms)
        set_cloexec(fd)
        self.part_file = os.fdopen(fd, self.mode, -1)
        if do_chmod:  # if default perms are overridden by the user or
            try:  # previous dest_path chmod away the effects of the umask
                os.chmod(self.part_path, file_perms)
            except (OSError, IOError):
                self.part_file.close()
                raise

    def setup(self):
        """Called on context manager entry (the with statement)."""
        if os.path.lexists(self.dest_path):
            if not self.overwrite:
                raise OSError('File already exists!: ' + self.dest_path)
        if os.path.lexists(self.part_path):
            os.unlink(self.part_path)
        self._open_part_file()

    def __enter__(self):
        self.setup()
        return self.part_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.part_file.close()
        tmp_file = os.path.join(gettempdir(), os.path.basename(self.part_path))
        if exc_type:
            if self.delete_part_if_fail:
                try:
                    rename_atomic(self.part_path, tmp_file, True)  # os.unlink
                except:
                    pass
            return
        try:
            rename_atomic(self.part_path, self.dest_path,
                          overwrite=self.overwrite)
        except OSError:
            if self.delete_part_if_fail:
                rename_atomic(self.part_path, tmp_file, True)  # os.unlink()
            raise  # could not save destination file
