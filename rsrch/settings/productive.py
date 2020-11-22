import django_heroku

from rsrch.settings.base import *

DEBUG = os.environ.get('DEBUG', False)

SITE_HOST = 'https://rsrch.herokuapp.com'

DATABASES = {
    'default': os.environ.get('DATABASE_URL'),
}

django_heroku.settings(locals())
