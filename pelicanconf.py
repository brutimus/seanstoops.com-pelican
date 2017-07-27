#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sean Stoops'
SITENAME = u'Sean Stoops'
SITETITLE = u'Sean Stoops'
SITESUBTITLE = u'I make things.'
SITEDESCRIPTION = u'A personal website for Sean Stoops to write about van building, rock climbing, programming, and miscellaneous adventures.'
SITEURL = 'http://localhost:8000'
THEME = 'themes/Flex-master'
COPYRIGHT_NAME = 'Sean Stoops'
COPYRIGHT_YEAR = '2017'
ROBOTS = 'index, follow'
USE_FOLDER_AS_CATEGORY = False

PATH = 'content'
STATIC_PATHS = ['assets']

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
    ('Van Building', '/pages/camper-van-conversions/'),
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

PLUGIN_PATHS = ['pelican-plugins', 'custom-plugins']
PLUGINS = (
    'assets',
    'pelican_alias',
    'photos',
    'related_posts',
    'sitemap'
)

DISQUS_SITENAME = "seanstoops"

TEMPLATE_PAGES = {
    'template_pages/camper-van-conversions.html': 'pages/camper-van-conversions/index.html'
}

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-2088185738984134',
    'page_level_ads': True,
    'ads': {
        # 'aside': '2232269495',
        # 'main_menu': '6690389256',
        # 'index_top': '7205572181',
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

PHOTO_LIBRARY = "content/images"
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = True
# PHOTO_WATERMARK_TEXT = "© Sean Stoops"
PHOTO_WATERMARK_TEXT = False
# PHOTO_WATERMARK_IMG = "content/assets/watermark.png"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (1600, 1100, 40)
PHOTO_THUMB = (500, 333, 40)
