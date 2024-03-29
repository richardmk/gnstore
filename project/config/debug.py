from .settings import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'Hangar18',
        'HOST':'localhost',
        'PORT': 3306,

    }
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')