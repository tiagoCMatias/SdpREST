from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

JWT_SECRET = 'myteste'
SECRET_KEY = '6e3@hi6^8e8emw@=m#75pl5e7t9o41_z667*09^73k)5y!_&jx'