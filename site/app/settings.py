import os
import sys
from django.conf import settings


BASE_DIR = os.path.split( os.path.dirname(__file__) )[0]

settings.configure(
    DEBUG=True,
    SECRET_KEY='thesecretkey',
    ROOT_URLCONF='app.urls',
    STATIC_URL='/static/',
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
    ),
    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'template'),
    ),
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'bbdjango',
            'USER': 'bbdjangouser',
            'PASSWORD': '111',
        }
    },
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'rest_framework',

        'app',
    ),
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)
