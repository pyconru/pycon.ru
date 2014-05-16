from collections import defaultdict

from webassets import Bundle

from carcade.utils import patterns


LANGUAGES = ('en', 'ru')

BASE_URL = '/2014/'
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
    '*': ['conference', 'program', 'participation', 'partners', 'archive', 'summary'],
    'conference': ['about', 'coc', 'organizers', 'contacts'],
    'participation': ['price', 'venue', 'hotels'],
    'partners': ['list', 'join'],
    'program': ['speakers', 'content', 'schedule'],
    'program/content': [
        'python3',
        'writing-secure-apis',
        'the-sorry-state-of-ssl',
        'explore-your-data',
        'autoscaling-on-the-cloud',
        'python_in_yandex',
        'open_source_advices',
        'jetbrains',
        'memory',
        'pony_orm',
        'asyncio',
        'python_pytest',
        'underscore',
        'soa',
        'bdd_in_python',
        'data_analysis',
        'scrapinghub',
        'kivy',
        'hamly',
        'workshop',
        'workshop2',
    ],
}
