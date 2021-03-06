#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ahmad Jarara'
SITENAME = 'No Odd Cycles'
SITEURL = 'https://jarmac.org'



PATH = 'content'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# ('Pelican', 'http://getpelican.com/'),
# ('Jinja2', 'http://jinja.pocoo.org/'),
LINKS = (('Source', 'https://github.com/alphor/jarmac.org'),
         ('nixOS', '//jarmac.org/category/nixos.html'),
         ('linux', '//jarmac.org/category/linux.html'),
         ('meta', '//jarmac.org/category/meta.html'),
         ('math', '//jarmac.org/category/math.html'))

# Social widget
SOCIAL = (('Github', 'https://github.com/alphor', '//jarmac.org/theme/img/GitHub-Mark-Light-32px.png'),
          ('RSS', 'https://jarmac.org/feed', '//jarmac.org/theme/img/feed-icon-28x28.png'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

# Begin theme config
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']
THEME = './pelican-themes/pelican-bootstrap3'


CUSTOM_CSS = 'theme/css/sitewide.css'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

HIDE_SIDEBAR = True

# PIWIK_URL = 'piwik.jarmac.org'
# PIWIK_SITE_ID = "'1'"

DISABLE_URL_HASH = True

FEED_ALL_RSS = 'feed'
CATEGORY_FEED_RSS = '%s'
