#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://www.seanstoops.com'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

GOOGLE_ANALYTICS = "UA-72134577-1"
GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-2088185738984134',
    'page_level_ads': True,
    'ads': {
        # 'aside': '2232269495',
        # 'main_menu': '6690389256',
        'index_top': '7205572181',
        'index_bottom': '7400835696',
        'article_top': '9621828448',
        'article_bottom': '5682583438'
    }
}

print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.abspath(os.curdir))
print(sys.path)
print(os.listdir('.'))
print(THEME)