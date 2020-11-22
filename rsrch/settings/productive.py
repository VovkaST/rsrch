from rsrch.settings.base import *

DEBUG = False

SITE_HOST = 'https://rsrch.herokuapp.com'

DATABASES = {
    'default': os.environ['DATABASE_URL']
}
