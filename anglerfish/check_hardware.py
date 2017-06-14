#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Check if running on Battery, return Bool."""


import logging as log
import os

from pathlib import Path

try:
    import dbus
except ImportError:
    dbus = None


def _get_prop(obj, iface, prop):
    """Get object interface properties."""
    if not dbus:
        log.warning("D-Bus module not found or not supported on this OS.")
        return  # Windows probably.
    try:
        return obj.Get(iface, prop, dbus_interface=dbus.PROPERTIES_IFACE)
    except (dbus.DBusException, dbus.exceptions.DBusException) as err:
        print(err)
        return


def has_battery():
    """Check if we are connected to a AC power or Battery."""
    log.debug("Checking if connected to AC-Power or Battery.")
    battery_path = Path("/sys/class/power_supply")  # is universal on Linux ?
    if not battery_path.exists():
        return False
    for folder in os.listdir(battery_path.as_posix()):
        type_path = battery_path / folder / 'type'
        if type_path.is_file():
            if type_path.read_text().lower().strip().startswith('battery'):
                return True
    return False


def on_battery():
    """Check if we are running on Battery power."""
    log.debug("Checking if running on Battery power.")
    if has_battery():
        bus, upower_path = dbus.SystemBus(), '/org/freedesktop/UPower'
        upower = bus.get_object('org.freedesktop.UPower', upower_path)
        result = _get_prop(upower, upower_path, 'OnBattery')
        if result is None:  # Cannot read property, something is wrong.
            print(f"Failed to read D-Bus property: {upower_path}.")
            result = False  # Assume we are connected to a power supply.
        return result
    return False

#
# def on_wifi():
#     """Check if we are running on wifi."""
#     try:
#         bus = dbus.SystemBus()
#         manager = bus.get_object('org.freedesktop.NetworkManager',
#                                  '/org/freedesktop/NetworkManager')
#          # FIXME this returns int, I dunno what they mean ?, investigate.
#         return _get_prop(manager, 'org.freedesktop.NetworkManager',
#                          'WirelessEnabled')
#     except Exception:
#         return False
