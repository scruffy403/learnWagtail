from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-3_s%ihx1=#a4ivuf&8sej97(g43%*qwf4vhs)k50o1^f&9=n+0'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'




try:
    from .local import *
except ImportError:
    pass
