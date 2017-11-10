#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Get a random pastel color as string, useful for HTML/CSS styling."""


# This 2 groups have been tested on HTML/CSS with one each other,
# they look pretty good on all combinations, we are not Designers,
# but this is useful for quick templating and boilerplates styling.


from random import choice


def get_random_pastelight_color(black_list: list=None) -> str:
    """Get a random pastel light color as string, useful for CSS styling."""
    colors_tuple = (
        'aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige',
        'cornsilk', 'floralwhite', 'ghostwhite', 'grey', 'honeydew', 'ivory',
        'lavender', 'lavenderblush', 'lemonchiffon', 'lightcyan',
        'lightgoldenrodyellow', 'lightgrey', 'lightpink', 'lightskyblue',
        'lightyellow', 'linen', 'mint', 'mintcream', 'oldlace', 'papayawhip',
        'peachpuff', 'seashell', 'skyblue', 'snow', 'thistle', 'white')
    if black_list:
        colors_tuple = tuple(set(colors_tuple).difference(set(black_list)))
    return choice(colors_tuple)


def get_random_pasteldark_color(black_list: list=None) -> str:
    """Get a random dark color as string, useful for CSS styling."""
    colors_tuple = (
        'brown', 'chocolate', 'crimson', 'darkblue', 'darkgoldenrod',
        'darkgray', 'darkgreen', 'darkolivegreen', 'darkorange', 'darkred',
        'darkslateblue', 'darkslategray', 'dimgray', 'dodgerblue',
        'firebrick', 'forestgreen', 'indigo', 'maroon', 'mediumblue',
        'midnightblue', 'navy', 'olive', 'olivedrab', 'royalblue',
        'saddlebrown', 'seagreen', 'sienna', 'slategray', 'teal')
    if black_list:
        colors_tuple = tuple(set(colors_tuple).difference(set(black_list)))
    return choice(colors_tuple)


def get_random_pastel_color(black_list: list=None) -> str:
    """Get a random dark or light color as string, useful for CSS styling."""
    colors_tuple = (get_random_pastelight_color(),
                    get_random_pasteldark_color())
    if black_list:
        colors_tuple = tuple(set(colors_tuple).difference(set(black_list)))
    return choice(colors_tuple)
