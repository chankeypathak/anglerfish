#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Download accelerator with multiple concurrent downloads for 1 file."""


import logging as log
import os
import ssl
import threading

from datetime import datetime
from tempfile import NamedTemporaryFile
from urllib.request import Request, urlopen

try:
    from make_autochecksum import autochecksum
    from bytes2human import bytes2human
    from seconds2human import timedelta2human
    from get_human_datetime import get_human_datetime
except ImportError:
    from anglerfish import (autochecksum, bytes2human,
                            timedelta2human, get_human_datetime)


def _get_context():
    """Return a context for the downloaders."""
    _context = ssl.create_default_context()
    _context.check_hostname = False  # Do NOT Check server Hostnames
    _context.verify_mode = ssl.CERT_NONE  # Do NOT Check server SSL Certificate
    return _context


def _download_simple(url, data, timeout, filename):
    """Download without multiple concurrent downloads for the same file."""
    with urlopen(url, data=data, timeout=timeout, context=_get_context()
                 ) as urly, open(filename, 'wb') as fyle:
        fyle.write(urly.read())
        return filename


def _calculate_ranges(value, numsplits):
    """Calculate the number of ranges of bytes, return a list of ranges."""
    lst = []
    for i in range(numsplits):
        lst.append('{0}-{1}'.format(
            i if i == 0 else int(round(1 + i * value / (numsplits * 1.0), 0)),
            int(round(1 + i * value / (numsplits * 1.0) +
                      value / (numsplits * 1.0) - 1, 0))))
    return tuple(lst)


def _get_size(url, data, timeout):
    """Get the file Size in bytes from a remote URL."""
    with urlopen(url, data=data, timeout=timeout, context=_get_context()) as u:
        size = int(u.headers.get('content-length', 0))
    log.info(f"Download Size: {bytes2human(size, 'm')} ({size}Bytes) Download")
    log.info(f"Full HTTP Headers data:\n{ u.headers }.\n")
    return size


def _download_a_chunk(idx, irange, dataDict, url, data, timeout):
    req = Request(url, headers={'User-Agent': '', 'DNT': 1})
    req.headers['Range'] = f"bytes={ irange }"
    print(f"Thread {idx} is downloading data: {req.headers['Range']}.")
    with urlopen(req, data=data, timeout=timeout, context=_get_context()) as u:
        dataDict[idx] = u.read()


def url2path(url, data=None, timeout=None,
             filename=None, suffix=None, name_from_url=False,
             concurrent_downloads=5, force_concurrent=False, checksum=False):
    if not url.lower().startswith({"https:", "http:", "ftps:", "ftp:"}):
        return url  # URL is a file path?.
    start_time, dataDict = datetime.now(), {}
    if not filename and bool(name_from_url):  # Get the filename from the URL.
        filename = url.split('/')[-1]
    if not filename:  # Create a temporary file as the filename.
        filename = NamedTemporaryFile(suffix=suffix, prefix="angler_").name
    log.info(f"""Angler download accelerator.\nFrom: {url}.\nTo:   {filename}.
    Time: ~{get_human_datetime(start_time)} ({start_time}).""")
    sizeInBytes = _get_size(url, data=data, timeout=timeout)
    # if sizeInBytes=0,Resume is not supported by server,use _download_simple()
    # if sizeInBytes < 1 Gigabytes,file is small,use _download_simple()
    if not int(sizeInBytes / 1024 / 1024 / 1024) >= 1 and not force_concurrent:
        log.info("Resume is Not supported by the server or file is too small.")
        filename = _download_simple(url, data=data,
                                    timeout=timeout, filename=filename)
        if checksum and autochecksum:
            log.info("Generating Anglers Auto-CheckSum for downloaded file.")
            filename = autochecksum(filename, update=True)
        return filename
    splitBy = concurrent_downloads if concurrent_downloads in range(11) else 10
    ranges = _calculate_ranges(int(sizeInBytes), int(splitBy))
    log.info(f"Using {splitBy} async concurrent downloads for the same file.")
    # multiple concurrent downloads for the same file.
    downloaders = [threading.Thread(
        target=_download_a_chunk,
        args=(idx, irange, dataDict, url, data, timeout), )
                   for idx, irange in enumerate(ranges)]
    for th in downloaders:
        th.start()
    for th in downloaders:
        th.join()
    with open(filename, 'wb') as fh:  # Reassemble file in correct order.
        for _idx, chunk in tuple(sorted(dataDict.items())):
            fh.write(chunk)
    if checksum and autochecksum:
        log.info("Generating Anglers Auto-CheckSum for downloaded file.")
        filename = autochecksum(filename, update=True)
    # Log some nice info.
    fl_size, fl_time = os.path.getsize(filename), datetime.now() - start_time
    log.info(f"Downloaded { len(dataDict) } binary data chunks total.")
    log.info(f"Finished writing downloaded output file: {filename}.")
    log.info(f"Size:     {bytes2human(fl_size, 'm')} ({fl_size} Bytes).")
    log.info(f"Time:     {timedelta2human(fl_time)} ({fl_time}).")
    log.info(f"Finished: {get_human_datetime()} ({datetime.now()}).")
    return filename
