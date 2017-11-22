#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""example of Angler `url2path()`."""


URL0 = "http://releases.ubuntu.com/16.04.2/ubuntu-16.04.2-server-amd64.iso"
URL1 = "http://www.nasa.gov/images/content/607800main_kepler1200_1600-1200.jpg"
URL2 = "http://releases.ubuntu.com/16.04.2/ubuntu-16.04.2-desktop-amd64.iso"

try:
    from anglerfish import url2path
except ImportError:
    from url2path import url2path


url2path(URL0, use_tqdm=True)

# url2path(URL1, name_from_url=True, concurrent_downloads=2,
#          force_concurrent=True, checksum=True, use_tqdm=True)
