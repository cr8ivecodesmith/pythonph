from .base import *


###### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
###### END DEBUG CONFIGURATION


###### DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('PYTHONPH_DATABASE'),
        'USER': get_env_variable('PYTHONPH_DATABASE_USER'),
        'PASSWORD': get_env_variable('PYTHONPH_DATABASE_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '',
    }
}
###### END DATABASE CONFIGURATION


###### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Developer', get_env_variable('PYTHONPH_EMAIL_HOST_USER')),
)
###### END MANAGER CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


###### APP CONFIGURATION
INSTALLED_APPS += (
    # See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
    'debug_toolbar',
)
###### END APP CONFIGURATION


###### DEBUG TOOLBAR CONFIGURATION
# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
INTERNAL_IPS = ('127.0.0.1',)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# See: https://github.com/django-debug-toolbar/django-debug-toolbar#installation
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TEMPLATE_CONTEXT': True,
}
###### END DEBUG TOOLBAR CONFIGURATION
