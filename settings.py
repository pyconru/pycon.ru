from collections import defaultdict

from webassets import Bundle

from carcade.utils import patterns


LANGUAGES = ('en', 'ru')

BASE_URL = '/2013/'
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
    '*': ['conference', 'program', 'participation', 'partners', 'contacts', 'summary'],
    'conference': ['about', 'organizers'],
    'participation': ['price', 'venue', 'hotels'],
    'partners': ['list', 'join'],
    'program': ['headliners', 'content', 'schedule'],
    'program/content': [
        'django-roadmap',
        'building-a-community',
        'advanced-flask-patterns',
        'packaging-and-testing',
        'scaling-for-success',
        'autosustainable-services',
        'redis-the-hackers-database',
        'pep-3156',
        'static-analysis',
        'transition-to-python-3',
        'celery-for-internal-api',
        'inside-of-asynchronous-code',
        'versioning-in-relational-database',
        'low-latency-and-soft-realtime',
        'synchronization-between-services',
        'saltstack',
        'test-optimization',
        'distributed-execution',
        'test-driven-development',
        'distributed-caching-system',
        'mongoengine-noorm-for-nosql',
        'tornado-not-only-web-sites',
        'workshop-rpython',
        'workshop-network-applications',
        'workshop-porting-from-2-to-3',
        'lightning-talks-1',
        'lightning-talks-2',
    ],
}
