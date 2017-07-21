#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sean Stoops'
SITENAME = u'Sean Stoops'
SITETITLE = u'Sean Stoops'
SITESUBTITLE = u'Things I do'
SITEDESCRIPTION = u'A personal website for Sean Stoops to write about van building, rock climbing, programming, and miscellaneous adventures.'
SITEURL = 'http://localhost:8000'
THEME = 'themes/Flex-master'
COPYRIGHT_NAME = 'Sean Stoops'
COPYRIGHT_YEAR = '2017'
USE_FOLDER_AS_CATEGORY = False

PATH = 'content'
STATIC_PATHS = ['images']

CUSTOM_CSS = 'css/custom.css'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

MAIN_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Archives', '/archives.html'),)

# Social widget
SOCIAL = (('instagram', 'https://www.instagram.com/seanstoops/'),
          ('facebook', 'https://www.facebook.com/seanstoopsadventurevan/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ('pelican_alias', 'assets')

DISQUS_SITENAME = "seanstoops"

TEMPLATE_PAGES = {
    'template_pages/van-index.html': 'pages/van-building/index.html'
}