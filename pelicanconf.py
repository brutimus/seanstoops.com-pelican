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

INDEX_SAVE_AS = 'all_index.html'
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
LINKS = (
    ('Home', '/'),
    ('Van Building', '/pages/van-building/'),
    ('Photos', '/pages/photos'),
    ('Archives', '/archives.html')
)

# Social widget
SOCIAL = (
    ('instagram', 'https://www.instagram.com/seanstoops/'),
    ('facebook', 'https://www.facebook.com/seanstoopsadventurevan/'),
    ('github', 'https://github.com/brutimus'),
    ('reddit', 'https://www.reddit.com/user/brutimus/')
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ('pelican_alias', 'assets', 'related_posts', 'sitemap')

DISQUS_SITENAME = "seanstoops"

TEMPLATE_PAGES = {
    'template_pages/van-index.html': 'pages/van-building/index.html'
}

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-2088185738984134',
    'page_level_ads': True,
    'ads': {
        'aside': '2232269495',
        # 'main_menu': '6690389256',
        'index_top': '7205572181',
        'index_bottom': '7400835696',
        'article_top': '9621828448',
        'article_bottom': '5682583438'
    }
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}