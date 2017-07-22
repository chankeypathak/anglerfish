# -*- coding: utf-8 -*-


"""Minimum possible example demo for `anglerfish.Sync2Async()` class."""


import time
import asyncio

from anglerfish import Sync2Async


def blocking_function():  # This is any common normal blocking function.
    print("Executing Synchronous Blocking code 'time.sleep(1)' as Async!.")
    return time.sleep(1)  # Can be any for, open, with, slow operation, etc.


async def async_function(sync_code):
    return await Sync2Async.run_async(sync_code)


async def async_on_process(sync_code):
    return await Sync2Async.run_async_on_process(sync_code)


async def async_on_thread(sync_code):
    return await Sync2Async.run_async_on_thread(sync_code)


async_tasks = (asyncio.ensure_future(async_function(blocking_function)),
               asyncio.ensure_future(async_on_process(blocking_function)),
               asyncio.ensure_future(async_on_thread(blocking_function)))
asyncio.get_event_loop().run_until_complete(asyncio.wait(async_tasks))
