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
    #(r'^program/schedule$', 'page.html'),
    (r'^program/content$', 'content.html'),
    (r'^program/content/.*$', 'speech.html'),
    (r'^.*$', 'page.html'),
)

ORDERING = {
    '*': ['conference', 'program', 'participation', 'partners', 'archive', 'summary'],
    'conference': ['about', 'coc', 'organizers', 'contacts'],
    'participation': ['price', 'venue', 'hotels'],
    'partners': ['list', 'join'],
    'program': ['cfp', 'headliners', 'content', 'schedule'],
    'program/content': [
        'writing-secure-apis',
        'the-sorry-state-of-ssl',
        'explore-your-data',
        'python_in_yandex',
        'pony_orm',
        'open_source_advices',
        'python_pytest',
        'soa',
    ],
}
