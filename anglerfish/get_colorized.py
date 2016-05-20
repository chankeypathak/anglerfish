#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Take and Return a string, but ANSI colored, as requested or random."""


from random import randint


def get_colorized(stringy, color=None, background=None):
    background = background if background else 40
    color = color if color else randint(30, 38)
    return "\033[1;{c};{b}m {msg} \033[0m".format(c=color, b=background, msg=stringy)


print(get_colorized("test"))
