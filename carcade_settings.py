from collections import defaultdict

from webassets import Bundle


LANGUAGES = ('en', 'ru')

DEFAULT_PAGE = 'conference/about'
DEFAULT_LANGUAGE = 'ru'
speeches = [
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
]

DEFAULT_LAYOUT = 'page.html'
LAYOUTS = defaultdict(lambda: 'page.html', {
    'conference/about': 'index.html',
    'program/schedule': 'schedule.html',
    'program/content': 'content.html',
    'partners/list': 'partners.html',
    'register': 'register.html',
})

for speech in speeches:
    LAYOUTS['program/content/%s' % speech] = 'speech.html'

BUNDLES = {
    'css': Bundle('./css/reset.css', './css/normalize.css', 
                  Bundle('./less/styles.less', filters='less'),
                  output='./gen/styles.css'),
}

ORDERING = {
    '*': ['conference', 'summary', 'program', 'participation', 'partners', 'contacts'],
    'conference/*': ['about', 'organizers'],
    'participation/*': ['price', 'venue', 'hotels'],
    'partners/*': ['list', 'join'],
    'program/*': ['headliners', 'content', 'schedule'],
    'program/content/*': speeches,
}
