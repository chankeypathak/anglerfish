#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Test the Lock for the Single Instance feature."""


from anglerfish import set_single_instance

lock = set_single_instance("test")
input(" Waiting... ")
