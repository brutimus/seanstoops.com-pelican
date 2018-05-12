#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


# STRINGS

AUTHOR = u'Sean Stoops'
COPYRIGHT_NAME = 'Sean Stoops'
COPYRIGHT_YEAR = '2018'
ROBOTS = 'index, follow'
SITENAME = u'SeanStoops.com'
SITETITLE = u'Sean Stoops'
SITEDESCRIPTION = u'A personal website for Sean Stoops to write about van building, rock climbing, programming, and miscellaneous adventures.'
SITEURL = 'http://localhost:8000'


# CORE

CACHE_CONTENT = True
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%A, %b. %d, %Y'
DEFAULT_PAGINATION = 10
DISABLE_URL_HASH = True
LOAD_CONTENT_CACHE = True
MAIN_MENU = False
TIMEZONE = 'America/Los_Angeles'
TYPOGRIFY = True
USE_FOLDER_AS_CATEGORY = False


# FEEDS

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# PHOTOS

PHOTO_LIBRARY = "content/images"
PHOTO_RESIZE_JOBS = 8
PHOTO_WATERMARK = True
# PHOTO_WATERMARK_TEXT = "© Sean Stoops"
PHOTO_WATERMARK_TEXT = False
# PHOTO_WATERMARK_IMG = "content/assets/watermark.png"
PHOTO_GALLERY = (2500, 1700, 80)
PHOTO_ARTICLE = (1600, 1100, 60)
PHOTO_THUMB = (900, 400, 60)
PHOTO_EXIF_KEEP = True
PHOTO_EXIF_COPYRIGHT = 'COPYRIGHT'
PHOTO_EXIF_COPYRIGHT_AUTHOR = 'Sean Stoops'


# PLUGINS

DISQUS_SITENAME = "seanstoops"
MARKDOWN = {
    'extensions': [
        'markdown.extensions.smarty',
        'markdown.extensions.extra',
        'markdown.extensions.meta',
        'figureAltCaption'
    ]
}
PLUGIN_PATHS = ['pelican-plugins', 'custom-plugins']
PLUGINS = (
    'assets',
    'collate_content',
    'pelican_alias',
    'photos',
    'related_posts',
    # 'series',
    'sitemap'
)
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


# THEME

CUSTOM_CSS = 'css/custom.css'
SOCIAL = (
    ('instagram', 'https://www.instagram.com/seanstoops/'),
    ('facebook', 'https://www.facebook.com/seanstoopsadventurevan/'),
    ('github', 'https://github.com/brutimus'),
    ('reddit', 'https://www.reddit.com/user/brutimus/')
)
THEME = './themes/Flex'


# URLS

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
CUSTOM_CATEGORY_URLS = {
    'photo-gallery': 'pages/photos/',
    'van-building': 'pages/camper-van-conversions/'
}
INDEX_SAVE_AS = 'all_index.html'
LINKS = (
    ('Home', '/'),
    ('Van Building', '/pages/camper-van-conversions/'),
    ('Photos', '/pages/photos/'),
    ('Archives', '/archives.html'),
    ('Search', '/search/')
)
MENUITEMS = LINKS[1:]
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%b}/index.html'
PATH = 'content'
STATIC_PATHS = ['assets']
TEMPLATE_PAGES = {
    'template_pages/camper-van-conversions.html': 'pages/camper-van-conversions/index.html',
    'template_pages/photos.html': 'pages/photos/index.html',
    'template_pages/search.html': 'search/index.html',
    'pages/google553619ee5f1c5922.html': 'google553619ee5f1c5922.html'
}
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
