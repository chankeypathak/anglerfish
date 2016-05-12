#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Get config folder cross-platform, try to always return a path."""


def make_config(app):
    """Make a global config object."""
    global CONFIG
    config_file = os.path.join(get_or_set_config_folder(app), "config.json")
    if not os.path.isfile(config_file):
        log.debug("Creating a new JSON Config file: " + config_file)
        with open(config_file, "w", encoding="utf-8") as config_object:
            config_object.write("{}\n")
    with open(config_file, "r", encoding="utf-8") as config_object:
        log.debug("Reading JSON Config file: " + config_file)
        CONFIG = loads(config_object.read().strip())


def view_config(app):
    """Open the JSON config file for app."""
    log.debug("Opening JSON Config file: config.json")
    return open_new_tab(
        os.path.join(get_or_set_config_folder(app), "config.json"))


def autosave_config(app):
    log.debug("Cleaning up, AutoSaving Configs and Shutting Down...")
    config_file = os.path.join(get_or_set_config_folder(app), "config.json")
    with open(config_file, "w", encoding="utf-8") as config_object:
        config_object.write(dumps(CONFIG, sort_keys=1, indent=4))


def delete_config(app):
    """Delete config folder."""
    log.debug("Deleting Config folder and all its contents recursively...")
    return rmtree(get_or_set_config_folder(app), ignore_errors=True)


def backup_config(app):
    """AutoBackup config settings to a compressed ZIP."""
    log.debug("Making Compressed ZIP Back-Up of Config folder...")
    output_file = os.path.join(os.path.expanduser("~"), app)
    make_archive(output_file, 'zip', get_or_set_config_folder(app), logger=log)
    return output_file + ".zip"


def get_or_set_config_folder(appname):
    """Get config folder cross-platform, try to always return a path."""
    if sys.platform.startswith("darwin"):  # Apples Macos
        config_path = os.path.expanduser("~/Library/Preferences")
    elif sys.platform.startswith("win"):  # Windown
        config_path = os.getenv("APPDATA", os.path.expanduser("~/.config"))
    else:
        config_path = os.getenv("XDG_CONFIG_HOME",
                                os.path.expanduser("~/.config"))
    if appname and len(appname) and isinstance(appname, str):
        config_path = os.path.join(config_path, appname.strip())
    log.debug("Config folder for {0} is: {1}".format(appname, config_path))
    if not os.path.isdir(config_path):
        log.debug("Creating new Config folder: {0}.".format(config_path))
        os.makedirs(config_path)
    return config_path
