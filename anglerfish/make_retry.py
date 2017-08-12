#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Retry calling the decorated function using an exponential backoff."""


from functools import wraps
import time


def retry(tries: int=5, delay: int=3, backoff: int=2,
          timeout: int=None, silent: bool=False,
          logger: object=None, exceptions: tuple=(Exception, )) -> object:
    """Retry calling the decorated function using an exponential backoff."""
    def deco_retry(f):

        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = int(tries), int(delay)
            end_time = time.time() + int(timeout) if timeout else None
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except exceptions as error:
                    if end_time and time.time() > end_time:
                        raise
                    msg = f"{error}. Retrying in ~{mdelay} seconds..."
                    if mtries < 3:
                        msg += " (Warning: This is the last Retry!)."
                    if not silent:
                        logger.warning(msg) if logger else print(msg)
                    time.sleep(mdelay + int(mtries % 2))
                    mtries -= 1  # Backoff multiplier should be between 1 ~ 8
                    mdelay *= int(backoff if backoff in range(1, 9) else 1)
            return f(*args, **kwargs)

        return f_retry

    return deco_retry
