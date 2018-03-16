from collections import defaultdict

from webassets import Bundle

from carcade.utils import patterns


LANGUAGES = ('en', 'ru')

BASE_URL = '/2018/'
STATIC_URL = BASE_URL

DEFAULT_PAGE = 'conference/about'
DEFAULT_LANGUAGE = 'ru'

BUNDLES = {
    'css': Bundle('./css/reset.css', './css/normalize.css', 
                  Bundle('./less/styles.less', filters='less'),
                  output='./gen/styles.css'),
}

LAYOUTS = patterns(
    (r'^conference/about$', 'index.html'),
    (r'^partners/list$', 'partners.html'),
    (r'^register$', 'register.html'),
    (r'^program/schedule$', 'schedule.html'),
    (r'^program/content$', 'content.html'),
    (r'^program/content/.*$', 'speech.html'),
    (r'^.*$', 'page.html'),
)

ORDERING = {
    '*': ['conference', 'program', 'participation', 'partners', 'archive', 'register'],
    'conference': ['about', 'coc', 'organizers', 'contacts'],
    'participation': ['price', 'venue', 'hotels'],
    'partners': ['list', 'join'],
    'program': ['cfp', 'speakers', 'content', 'schedule', 'Unconference'],
    'archive': ['2013', '2014', '2015', '2016', '2017'],
    'program/content': [],
}
