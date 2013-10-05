from os import environ
from os.path import basename
from unipath import Path
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(varname, default=None):
    """ Get environment variable or return exception. 
        If the default argument is provided, set it as the value and return that.
    """
    try:
        return environ[varname]
    except KeyError:
        if default:
            environ.setdefault(varname, default)
            return environ[varname]
        else:
            msg = 'Set the {} environment variable.'.format(varname)
            raise ImproperlyConfigured(msg)


###### PATH CONFIGURATION
# Absolute filesystem path to the project directory. Requires unipath library.
# Ancestor 3 will point to /path/to/repo/pythonph/pythonph
SITE_ROOT = Path(__file__).ancestor(3)
SITE_NAME = basename(SITE_ROOT)
###### END PATH CONFIGURATION


###### DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
###### END DEBUG CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = get_env_variable('PYTHONPH_EMAIL_HOST')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = get_env_variable('PYTHONPH_EMAIL_HOST_PASSWORD')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = get_env_variable('PYTHONPH_EMAIL_HOST_USER')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = get_env_variable('PYTHONPH_EMAIL_HOST_PORT')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[{}] '.format(SITE_NAME)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION


###### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Webmaster', get_env_variable('PYTHONPH_EMAIL_HOST_USER')),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
###### END MANAGER CONFIGURATION


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


###### GENERAL CONFIGURATION
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Asia/Manila'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#languages
LANGUAGES = [
    ('en', 'English'),
]

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
###### END GENERAL CONFIGURATION


###### MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = SITE_ROOT.child('media')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
###### END MEDIA CONFIGURATION


###### STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = SITE_ROOT.child('static')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    # Additional paths here should utilize SITE_ROOT
    # Example: SITE_ROOT.child('example_dir'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
###### END STATIC FILE CONFIGURATION


###### SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_variable('PYTHONPH_SECRETKEY')
###### END SECRET CONFIGURATION


###### SESSION SERIALIZATION CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/topics/http/sessions/#session-serialization
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
###### END SESSION SERIALIZATION CONFIGURATION


###### SITE CONFIGURATION
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
###### END SITE CONFIGURATION


###### FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
    # Additional paths here should utilize SITE_ROOT
    # Example: SITE_ROOT.child('example_dir'),
)
###### END FIXTURE CONFIGURATION


###### TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # Django CMS
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    # Additional paths here should utilize SITE_ROOT
    # Example: SITE_ROOT.child('example_dir'),
    SITE_ROOT.child('templates'),
)

# See: http://docs.django-cms.org/en/2.4.2/getting_started/configuration.html#std:setting-CMS_TEMPLATES
CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)
###### END TEMPLATE CONFIGURATION


###### MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
DJANGO_MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

THIRD_PARTY_MIDDLEWARE = (
    # Django CMS
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

LOCAL_MIDDLEWARE = (
)

MIDDLEWARE_CLASSES = DJANGO_MIDDLEWARE + THIRD_PARTY_MIDDLEWARE + LOCAL_MIDDLEWARE

###### END MIDDLEWARE CONFIGURATION


###### URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '{}.urls'.format(SITE_NAME)
###### END URL CONFIGURATION


###### APP CONFIGURATION
DJANGO_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin panel and documentation
    'django.contrib.admin',
    # 'django.contrib.admindocs',
)

THIRD_PARTY_APPS = (
    # Database migration helpers
    'south',
    # Django CMS
    'cms',
    'mptt',
    'sekizai',
    # Django CMS Plugins
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.teaser',
    'cms.plugins.text',
    'cms.plugins.video',
    'cms.plugins.twitter',
)

# Project-specific apps
LOCAL_APPS = (
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
###### END APP CONFIGURATION


###### LOGGING CONFIGURATION
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
SITE_LOGS = SITE_ROOT.ancestor(1).child('logs')
DEFAULT_LOGFILE = '{}/{}.log'.format(SITE_LOGS, SITE_NAME)

try:
    open(DEFAULT_LOGFILE, 'w').close()
except IOError:
    raise

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        # See: http://docs.python.org/2/library/logging.html#logrecord-attributes
        'default': {
            'format': '%(asctime)s [%(process)d] [%(levelname)s] - %(messages)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': DEFAULT_LOGFILE,
            'maxBytes': 1024*1024*10,  # 10 megabytes
            'backupCount': 5
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
###### END LOGGING CONFIGURATION


###### WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '{}.wsgi.application'.format(SITE_NAME)
###### END WSGI CONFIGURATION
