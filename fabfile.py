import os
import time

from fabric.api import env, local

from build import build


def deploy():
    # Compile gettext messages
    local('msgfmt ./messages.po -o ./messages.mo')

    # Build site in separate folder
    build_dir = '_build-%s' % int(time.time())
    local('cp -r ./static ./%s' % build_dir)
    local('lessc --compress '
          './%(build_dir)s/less/styles.less '
          './%(build_dir)s/css/styles.css' % {'build_dir': build_dir})
    build(build_dir)

    prev_build_dir = os.path.exists('./www') and os.readlink('./www')

    # Link new build to ./www 
    local('ln -snf ./%s ./www' % build_dir)
    # Remove old build if it exists
    if prev_build_dir:
        local('rm -rf %s' % prev_build_dir)
