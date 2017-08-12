#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Calculate time, with precision from seconds to days."""


import time

from collections import namedtuple


def seconds2human(time_on_seconds: int) -> namedtuple:
    """Calculate time, with precision from seconds to days."""
    # Calculate all time units from time_on_seconds positive integer.
    minutes, seconds = divmod(int(abs(time_on_seconds)), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    months, weeks = divmod(weeks, 4)
    years, months = divmod(months, 12)
    decades, years = divmod(years, 10)
    centuries, decades = divmod(decades, 10)

    # Build a namedtuple with all named time units and all its integer values.
    time_units = namedtuple(
        "AllHumanFriendlyFrequentTimeUnits",
        "seconds minutes hours days weeks months years decades centuries")(
        seconds, minutes, hours, days, weeks, months, years, decades, centuries
    )

    # Build a human friendly time string with frequent time units.
    t_parts = []
    if centuries:
        t_parts.append(f"{centuries} Centur{'ies' if centuries > 1 else 'y'}")
    if decades:
        t_parts.append(f"{decades} Decade{'s' if decades > 1 else ''}")
    if years:
        t_parts.append(f"{years} Year{'s' if years > 1 else ''}")
    if months:
        t_parts.append(f"{months} Month{'s' if months > 1 else ''}")
    if weeks:
        t_parts.append(f"{weeks} Week{'s' if weeks > 1 else ''}")
    if days:
        t_parts.append(f"{days} Day{'s' if days > 1 else ''}")
    if hours:
        t_parts.append(f"{hours} Hour{'s' if hours > 1 else ''}")
    if minutes:
        t_parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    t_parts.append(f"{seconds} Second{'s' if seconds > 1 else ''}")
    human_time = " ".join(t_parts)

    return namedtuple("Times", "human_time time_units")(human_time, time_units)


def timedelta2human(time_delta) -> namedtuple:  # Just a shortcut :)
    """Convert a timedelta object to human string representation."""
    return seconds2human(time_delta.total_seconds())


def datetime2human(date_time) -> namedtuple:  # Just a shortcut :)
    """Convert a datetime object to human string representation."""
    return seconds2human(time.mktime(date_time.timetuple()))
