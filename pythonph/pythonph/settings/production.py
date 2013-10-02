from .base import *


###### SITE CONFIGURATION
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS.append('.python.ph')
###### END SITE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp',
    }
}
########## END CACHE CONFIGURATION
