django-newrelic-extensions
==========================

This package provides a Django middleware class that attaches custom attributes
to the stack trace that the New Relic agent sends to your console.  For
example, if a server error occurs you may wish to know the username of the user
who received it.

Installation
------------

Install via pip:

::

    $ pip install django-newrelic-extensions

Or from Github:

::

    $ pip install -e git://github.com/sheepdoginc/django-newrelic-extensions.git#egg=django-newrelic-extensions

Add the middleware class to your ``MIDDLEWARE_CLASSES``:

::

    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'newrelicextensions.middleware.NewRelicMiddleware',
    )

And then add your settings.

Settings
--------


* ``NEW_RELIC_EXTENSIONS_ENABLED``: This allows you to disable the extensions
  during development. (Default: ``False``)

* ``NEW_RELIC_EXTENSIONS_DEBUG``: This enables the extensions but instead of
  sending trace backs to New Relic, it prints them out to the console.
  (Default: ``True``)

* ``NEW_RELIC_EXTENSIONS_ATTRIBUTES``: This is how you specify what attributes
  of the Django ``HttpRequest`` instance you care about.  This should be a ``dict``.
  Please see below for examples.

Examples
--------

::
    
    NEW_RELIC_EXTENSIONS_ATTRIBUTES = {
        'user': {
            'username': 'Django username',
            'is_superuser': 'Django super user'
        },
        'is_secure': 'Django secure conneciton',
        'something random': 'Name'
    }

This will log the user's username under the key of ``Django username`` and so
on.  If a variable is callable (like ``is_secure`` above), it will be called.
If it doesn't exist, it will silently die (unless you have debug on).

For a list of examples attributes that you can log, see the `HttpRequest docs
<https://docs.djangoproject.com/en/dev/ref/request-response/#httprequest-objects>`_.

To learn more about New Relic's Python integration, please see their `Python
tips and tricks <https://newrelic.com/docs/python/python-tips-and-tricks>`_
page.


License
-------

BSD, short and sweet.
