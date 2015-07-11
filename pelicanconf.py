#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alterpony'
SITENAME = u'Clopedia'
SITEURL = 'https://clopedia.alterpony.ru'

PATH = 'content'
TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = u'ru'
THEME = 'clopedia'

PLUGINS = ['sitemap', 'tipue_search', 'tag_cloud', 'related_posts', 'series', 'assets', ]

FAVICON = "images/favicon.png"



FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SHOW_ARTICLE_AUTHOR = True
SHOE_ARTICLE_TRANSLATOR = True
SHOW_SERIES = True
SHOW_ARTICLE_CATEGORY = True

DISPLAY_BREADCRUMBS = True
DISPLAY_ARTICLE_INFO_ON_INDEX = None
DISPLAY_CATEGORIES_ON_SIDEBAR = None
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_TAGS_INLINE = True
DISPLAY_PAGES_ON_MENU = True


# TAG_CLOUD_MAX_ITEMS = 10
DISQUS_SITENAME = 'clopedia'
DISQUS_NO_ID = True
DISQUS_DISPLAY_COUNTS = True

DIRECT_TEMPLATES =  (('index', 'tags', 'categories', 'archives', 'authors', 'search', ))
TAGS_URL = (('tags.html'))
# Blogroll
LINKS = (('Alterpony', 'https://alterpony.ru'),
         ('Клопедия 3.0', 'https://docs.google.com/document/d/1VzbC7Asi_bNdk_Bjla3WsYWOyBCTTdCxvdboOGYHFzY'),)

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

DEFAULT_METADATA = {
    'status': 'draft',
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Sitemap
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

ASSET_CONFIG = (('closure_compressor_optimization', 'WHITESPACE_ONLY'),
                ('less_bin', 'lessc.cmd'), )
