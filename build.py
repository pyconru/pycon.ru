import os
import glob
import shutil
import codecs
import gettext
import subprocess

import markdown
from jinja2 import Environment, FileSystemLoader, contextfunction


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_DIR = os.path.join(PROJECT_DIR, '_build')

DEFAULT_PAGE = 'about'
DEFAULT_LANGUAGE = 'ru'


def path_for(name, language=None):
    url = ''
    if language != DEFAULT_LANGUAGE:
        url += '%s/' % language
    if name != DEFAULT_PAGE:
        url += '%s/' % name
    return url


@contextfunction
def url_for(context, name, language=None):
    language = language or context.resolve('LANGUAGE')
    return '/' + path_for(name, language=language)


def create_jinja2_environment(language):
    env = Environment(loader=FileSystemLoader('layouts'),
                      extensions=['jinja2.ext.i18n'])
    
    if language == 'ru':
        translations = gettext.GNUTranslations(open('messages.mo'))
        env.install_gettext_translations(translations, newstyle=True)
        # Hack:
        globals_gettext = env.globals['gettext']
        env.globals['gettext'] = contextfunction(
            lambda context, s: unicode(globals_gettext(context, s).decode('utf-8')))
    elif language == 'en':
        env.install_null_translations(newstyle=False)
    
    env.globals.update(url_for=url_for, LANGUAGE=language)
    return env


def render_template(template, context, target_fname):
    target_dir = os.path.dirname(target_fname)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    render = template.render(**context)
    with codecs.open(target_fname, 'w', 'utf-8') as f:
        f.write(render) 


def build():
    pages = ('about', 'venue', 'schedule', 'speakers', 'partners', 'register')
    layouts = dict(zip(pages, ['index.html'] + ['page.html'] * 5))

    for language in ('ru', 'en'):
        env = create_jinja2_environment(language)

        for page in pages:
            template = env.get_template(layouts[page])

            context = {
                'page_name': page,        
            }
            page_dir = os.path.join(PROJECT_DIR, 'pages', page, language)
            for fname in glob.glob('%s/*.md' % page_dir):
                block_name, ext = os.path.splitext(os.path.basename(fname))
                with codecs.open(fname, 'r', 'utf-8') as f:
                    context[block_name] = markdown.markdown(f.read())

            target_fname = os.path.join(BUILD_DIR, path_for(page, language=language), 'index.html')
            render_template(template, context, target_fname)
