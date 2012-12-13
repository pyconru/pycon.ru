from fabric.api import env, local

from build import build


env.hosts = ['']

def deploy():
    local('msgfmt ./messages.po -o ./messages.mo')
    local('rm -rf ./_build')
    local('cp -r ./static ./_build')
    local('lessc --compress ./_build/less/styles.less ./_build/css/styles.css')
    build()
