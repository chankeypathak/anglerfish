#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Calculate time, with precision from seconds to days."""


import time

from collections import namedtuple


def seconds2human(time_on_seconds: int) -> namedtuple:
    """Calculate time, with precision from seconds to days."""
    # Calculate all time units from time_on_seconds positive integer.
    seconds = int(abs(time_on_seconds))  # 1 Seconds    = 1 Seconds.
    minutes = divmod(seconds, 60)[0]     # 1 Minutes    = 60 Seconds.
    hours = divmod(minutes, 60)[0]       # 1 Hours      = 60 Minutes.
    days = divmod(hours, 24)[0]          # 1 Days       = 24 Hours.
    weeks = divmod(days, 7)[0]           # 1 Weeks      = 7 Days.
    months = divmod(weeks, 4)[0]         # 1 Months     = 4 Weeks.
    years = divmod(months, 12)[0]        # 1 Years      = 12 Months.
    decades = divmod(years, 10)[0]       # 1 Decade     = 10 Years.
    centuries = divmod(decades, 10)[0]   # 1 Century    = 10 decades.

    # Build a namedtuple with all named time units and all its integer values.
    time_units = namedtuple(
        "AllHumanFriendlyFrequentTimeUnits",
        "seconds minutes hours days weeks months years decades centuries")(
        seconds, minutes, hours, days, weeks, months, years, decades, centuries
    )

    # Build a human friendly time string with frequent time units.
    human_time_parts = []
    if centuries:
        human_time_parts += f"{ centuries } Centuries"
    if decades:
        human_time_parts += f"{ decades } Decades"
    if years:
        human_time_parts += f"{ years } Years"
    if months:
        human_time_parts += f"{ months } Months"
    if weeks:
        human_time_parts += f"{ weeks } Weeks"
    if days:
        human_time_parts += f"{ days } Days"
    if hours:
        human_time_parts += f"{ hours } Hours"
    if minutes:
        human_time_parts += f"{ minutes } minutes"
    human_time_parts += f"{ seconds } Seconds"
    human_time = " ".join(human_time_parts)

    return namedtuple("Times", "human_time time_units")(human_time, time_units)


def timedelta2human(time_delta) -> namedtuple:  # Just a shortcut :)
    """Convert a timedelta object to human string representation."""
    return seconds2human(time_delta.total_seconds())


def datetime2human(date_time) -> namedtuple:  # Just a shortcut :)
    """Convert a datetime object to human string representation."""
    return seconds2human(time.mktime(date_time.timetuple()))
