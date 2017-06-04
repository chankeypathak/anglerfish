#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Tinyslations, smallest possible Translations from Internet with fallback."""


from urllib import parse, request
from locale import getdefaultlocale
from json import loads


def tinyslation(s: str, to: str=getdefaultlocale()[0][:2], fm="en",
                falbck={}, timeout=5):
    """Translate from internet via API from mymemory.translated.net,legally."""
    api = "https://mymemory.translated.net/api/get?q={st}&langpair={fm}|{to}"
    req = request.Request(url=api.format(st=parse.quote(s), fm=fm, to=to),
                          headers={'User-Agent': '', 'DNT': 1})  # DoNotTrack
    try:
        responze = request.urlopen(req, timeout=timeout).read().decode("utf-8")
        return loads(responze)['responseData']['translatedText']
    except Exception:
        return falbck.get(s.lower().strip(), s)
