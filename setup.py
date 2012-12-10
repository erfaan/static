"""setup - setuptools based setup for static

Copyright (C) 2006-2009 Luke Arno - http://lukearno.com/

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to:

The Free Software Foundation, Inc., 
51 Franklin Street, Fifth Floor, 
Boston, MA  02110-1301, USA.

Luke Arno can be found at http://lukearno.com/

"""

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(name='static',
      version='0.4',
      description=\
        'A really simple WSGI way to serve static (or mixed) content.',
      long_description="""\
This distribution provides an easy way to include static content 
in your WSGI applications. There is a convenience method for serving 
files located via pkg_resources. There are also facilities for serving 
mixed (static and dynamic) content using "magic" file handlers. 
Python builtin string substitution and Kid template support are provided 
and it is easy to roll your own handlers. Note that this distribution 
does not require Kid unless you want to use that type of template. Also 
provides a command of the same name as a convenience when you just want 
to share a little content over HTTP, ad hoc.""",
      author='Luke Arno',
      author_email='luke.arno@gmail.com',
      url='http://lukearno.com/projects/static/',
      license="LGPL",
      py_modules=['static'],
      packages = [],
      install_requires="wsgiref",
      extras_require={'KidMagic': 'kid'},
      entry_points = """
          [console_scripts]
              static=static:command
      """,
      keywords="wsgi web http static content webapps",
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries',
                   'Topic :: Utilities'])

