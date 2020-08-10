from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# We should put this KEY in an OS variable.
# THIS NEVER SHOULD BEEN SEEN IN THE REPO OR ANYWHERE
SECRET_KEY = '5bzh*gbu_5072a9c^gc@ie$52fqt7_+f-w2pht3cedm0ktn*la'

# Set to False
DEBUG = False

ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Apps.oneSampleApp'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # Adding whitenoise for handling the static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'weeklyChallenge.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'Templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# If you any database you SHOULD put your 
# DB name, password and user in OS variables
WSGI_APPLICATION = 'weeklyChallenge.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# You can change
# (OPTIONAL)
LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/Static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'Static'),)

# Set the dir where the staticfiles should go when 
# running "collecstatic"
STATIC_ROOT =  os.path.join(BASE_DIR, 'staticfiles')

# Set the compression of the files by WhiteNoise
# (OPTIONAL)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'