from webassets import Bundle


LANGUAGES = ('en', 'ru')

DEFAULT_PAGE = 'about'
DEFAULT_LANGUAGE = 'ru'

DEFAULT_LAYOUT = 'page.html'
LAYOUTS = {
    'about': 'index.html',
    'register': 'register.html',
}

BUNDLES = {
    'css': Bundle('./css/reset.css', './css/normalize.css', 
                  Bundle('./less/styles.less', filters='less'),
                  output='./gen/styles.css'),
}
