from collections import defaultdict

from webassets import Bundle


LANGUAGES = ('en', 'ru')

DEFAULT_PAGE = 'conference/about'
DEFAULT_LANGUAGE = 'ru'

LAYOUTS = defaultdict(lambda: 'page.html', {
    'conference/about': 'index.html',
    'program/schedule': 'schedule.html',
    'partners/list': 'partners.html',
    'register': 'register.html',
})

BUNDLES = {
    'css': Bundle('./css/reset.css', './css/normalize.css', 
                  Bundle('./less/styles.less', filters='less'),
                  output='./gen/styles.css'),
}

ORDERING = {
    '*': ['conference', 'program', 'participation', 'partners', 'contacts', 'register'],
    'conference/*': ['about', 'organizers'],
    'participation/*': ['price', 'venue', 'hotels'],
    'partners/*': ['list', 'join'],
    'program/*': ['headliners', 'content', 'schedule', 'call-for-papers'],
}
