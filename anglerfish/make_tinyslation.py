#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tinyslations, smallest possible Translations from Internet with fallback."""


from urllib import parse, request
from locale import getdefaultlocale

try:
    from ujson import loads
except ImportError:
    from json import loads


def tinyslation(strin: str, to: str=getdefaultlocale()[0][:2], frm="en",
                fallback_dict={}, fallback_value=None, timeout=5):
    """Translate from internet via API from mymemory.translated.net,legally."""
    api = "https://mymemory.translated.net/api/get?q={st}&langpair={fm}|{to}"
    req = request.Request(url=api.format(st=parse.quote(strin), fm=frm, to=to),
                          headers={'User-Agent': '', 'DNT': 1})  # DoNotTrack
    try:
        responze = request.urlopen(req, timeout=timeout).read().decode("utf-8")
        return loads(responze)['responseData']['translatedText']
    except Exception:
        return fallback_dict.get(strin.lower().strip(),
                                 fallback_value if fallback_value else strin)
