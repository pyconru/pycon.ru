**[Holger Krekel](http://holgerkrekel.net/)**, founder of the [PyPy Project](http://pypy.org/), author of the [py.test](http://pytest.org/latest/) and [tox](http://codespeak.net/tox/) testing tools.    
**Re-inventing Python packaging and testing**

Python still does not have a built-in installer that can install dependencies.  You have to first install setuptools/distribute and then use easy_install/pip.  Installation of packages is slow and depends on reachability of  pypi.python.org and other servers.  There is no quality control where you could e. g. see on which platforms the package successfully installs, let alone has its automated tests passing.  There is not really a standard way to run tests.  This talk outlines my plans for improving the situation, including a demo of a new (in-development) PyPI server that speeds up installation by an order of magnitude for many packages.    
**Time:** 50 min
