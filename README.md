Forked from https://bitbucket.org/luke/static/

static
======

A really simple WSGI way to serve static (or mixed) content.

See docstrings of static module for details.

Changes in this fork
====================

Following features are added:

* Custom mimetypes support for StatusApp. Used for html 404 errors.
Example:
```
app = static.Cling('.', not_found=static.StatusApp('404 Not Found', file='./404.html'))
```
* Gzip support. Automatically detects and sends if gzipped content is
requested and available. Example: `index.html` tries to find `index.html.gz`
in the same directory.
* Expire/Cache-Control headers support for better performance.
Example:
```
EXPIRES = [
    # html
    ('text/html', 0),

    # feed
    ('application/atom+xml', 60*60),
    ('application/rss+xml', 60*60),

    # favicon
    ('image/x-icon', 7*24*60*60),

    # media
    ('image/gif', 30*24*60*60),
    ('image/jpeg', 30*24*60*60),
    ('image/png', 30*24*60*60),

    # CSS and Javascript
    ('application/javascript', 365*24*60*60),
    ('text/css', 365*24*60*60),
]
app = static.Cling(STATIC_DIR, expire_headers=EXPIRES)
```

TODO
====

Here are the suggested features for future:

* Support for sending custom headers

License
=======

Created and maintained by Luke Arno <luke.arno@gmail.com>

Modified by Irfan Ahmad <http://i.com.pk/>

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