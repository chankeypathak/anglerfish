#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Set or Get a ZIP comment on its Metadata, return Bool."""


import logging as log
from zipfile import ZipFile


def set_zip_comment(zip_path: str, comment: str="") -> bool:
    """Set a ZIP comment."""
    try:
        with ZipFile(zip_path, 'a') as myzip:
            myzip.comment = bytes(str(comment).strip().encode("utf-8"))
    except Exception as error:
        log.warning(f"Failed to set comments to ZIP file: {zip_path}.")
        log.debug(error)
        return False
    else:
        log.debug(f"Setting comments to ZIP file: {zip_path}.")
        return True


def get_zip_comment(zip_path: str) -> str:
    """Get a ZIP comment."""
    try:
        log.debug(f"Getting comments from ZIP file: {zip_path}.")
        with ZipFile(zip_path, 'r') as myzip:
            return str(myzip.comment.decode("utf-8")).strip()
    except Exception as error:
        log.warning(f"Failed to get comments from ZIP file: {zip_path}.")
        log.debug(error)
        return ""
