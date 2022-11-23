from .base import *
import os
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
            'NAME': 'chatbot',
            'USER': 'root',
            'PASSWORD': '00247887',
            'HOST': 'localhost',
            'PORT': '3306',
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR,"static")]
MEDIA_URL='/media/'
MEDIA_ROOT= BASE_DIR/"media/"