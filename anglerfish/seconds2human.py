#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Calculate time, with precision from seconds to days."""


def seconds2human(time_on_seconds=0):
    """Calculate time, with precision from seconds to days."""
    minutes, seconds = divmod(int(abs(time_on_seconds)), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    human_time_string = ""
    if days:
        human_time_string += "%02d Days " % days
    if hours:
        human_time_string += "%02d Hours " % hours
    if minutes:
        human_time_string += "%02d Minutes " % minutes
    human_time_string += "%02d Seconds" % seconds
    return human_time_string
