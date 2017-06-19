"""
Django settings for sistemaweb project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '23%z1-@0*fbsjm2b^vpst-x0f8zbb30-69*2jpz%@!!f@l!a)c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'usuario.Usuario'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor','djangobower',
    'django_nose','modules.core',
    'modules.usuario',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'compressor.finders.CompressorFinder',
]

ROOT_URLCONF = 'sistemaweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
if sys.platform == 'linux':
    BOWER_PATH = '/usr/local/bin/bower'
else:
    if "lucas" in BASE_DIR:
        BOWER_PATH = 'C:/Users/lucas/AppData/Roaming/npm/bower.cmd'
    else:
        BOWER_PATH = 'C:/Users/diego/AppData/Roaming/npm/bower.cmd'

#BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'static/bower')

BOWER_INSTALLED_APPS = (
    'angular#1.6.4',
    'jquery#3.2.1',
    'bootstrap#3.3.7',#3.3.2
    'font-awesome#4.6.3',#4.2
    'angular#1.6.4',
    'animate.css',
    'gauge.js',
    'chart.js',
    'bootstrap-progressbar#0.9.0',
    'jquery.nicescroll',
    'moment',
    "bootstrap-daterangepicker",
    'fastclick',
    'nprogress',
    'pnotify',
    'qunit',
    'blanket',
    'https://github.com/yairEO/validator.git'

)

WSGI_APPLICATION = 'sistemaweb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'data/db.sqlite3'),
    }
}
# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pt-br'

#TIME_ZONE = 'UTC'
#USE_TZ = True
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

LOGIN_REDIRECT_URL = "/"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
TEST_URL = BASE_DIR+os.path.join('/test/')
#TEST_RUNNER = 'xmlrunner.extra.djangotestrunner.XMLTestRunner'
#TEST_OUTPUT_DIR = "test/unit/report/backend_unit_report"


'''TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--verbosity=2',  # verbose output
    '--with-coverage',
    '--cover-inclusive',
    '--cover-xml',  # produle XML coverage info
    '--cover-xml-file=coverage.xml',  # the coverage info file
    '--with-xunit',  # enable XUnit plugin
    '--xunit-file=xunittest.xml'#test/unit/report/backend_unit_report/xunittest.xml',  # the XUnit report file
]
'''

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = [ BASE_DIR+os.path.join('/static/'), ]

WORKING_CONFIGURATION = os.path.join(BASE_DIR, 'conf/working.json')
WORKING_SERVER = "http://192.168.1.116:8010"

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'melinuxsistemas@gmail.com>'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'melinuxsistemas@gmail.com'
EMAIL_HOST_PASSWORD = '61109119'
EMAIL_PORT = 587


from conf import configuration
from modules.core.working_api import WorkingManager

SELENIUM_GECKODRIVER_MOZILLA = configuration.geckodriver_path
MOZILLA_FIREFOX_TEST_PATH = configuration.mozilla_firefox_path
SELENIUM_URL_PROJECT_TEST = "http://127.0.0.1:8000"

try:
    if "runserver" in sys.argv:
        WorkingManager().register_programming_backend()

    elif "test" in sys.argv:
        WorkingManager().register_test_backend()

    else:
        pass

except:
    pass
