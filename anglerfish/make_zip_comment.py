#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Check if running on Battery, return Bool."""


from zipfile import ZipFile


def set_zip_comment(zip_path, comment):
    """Set a ZIP comment."""
    try:
        with ZipFile(str(zip_path), 'w') as myzip:
            myzip.comment = bytes(str(comment).strip().encode("utf-8"))
    except Exception:
        return False
    else:
        return True


def get_zip_comment(zip_path):
    """Get a ZIP comment."""
    try:
        with ZipFile(str(zip_path), 'r') as myzip:
            return str(myzip.comment.decode("utf-8")).strip()
    except Exception:
        return ""
