# -*- coding: utf-8 -*-
import os
import glob
import codecs
import gettext

import markdown
from jinja2 import Environment, FileSystemLoader, contextfunction


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


def build(build_dir):
    pages = {
        'about': 'index.html',
        'organizers': 'page.html',
        'schedule': 'page.html',
        'speakers': 'page.html',
        'partners': 'page.html',
        'register': 'register.html',
        'venue': 'page.html',
    }

    for language in ('ru', 'en'):
        env = create_jinja2_environment(language)

        for page, layout in pages.iteritems():
            template = env.get_template(layout)

            context = {
                'page_name': page,
            }
            page_dir = os.path.join('pages', page, language)
            for fname in glob.glob('%s/*.md' % page_dir):
                block_name, ext = os.path.splitext(os.path.basename(fname))
                with codecs.open(fname, 'r', 'utf-8') as f:
                    context[block_name] = markdown.markdown(f.read())

            target_fname = os.path.join(
                build_dir, path_for(page, language=language), 'index.html')
            render_template(template, context, target_fname)
