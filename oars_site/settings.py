"""
Django settings for oars project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'lt)c@$4+z5yolszn81$h#1p&gpmfkr48r9z9v)@3)+(c45kdzg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oars',
    'student',
    'professor',
    'dugc',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oars.middleware.RestrictAccessMiddleware',
)

ROOT_URLCONF = 'oars_site.urls'

WSGI_APPLICATION = 'oars_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic/')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)

GRAPPELLI_ADMIN_TITLE = 'OARS Administration'
GRAPPELLI_ADMIN_HEADLINE = 'OARS Administration'

AUTH_USER_MODEL = 'oars.User'

USER_NONE = 0
USER_STUDENT = 1
USER_PROFESSOR = 2
USER_DUGC = 3

VALID_USER_TYPES = (USER_STUDENT, USER_PROFESSOR, USER_DUGC)

USER_TYPE_CHOICES = (
    (USER_STUDENT, "Student"),
    (USER_PROFESSOR, "Professor"),
    (USER_DUGC, "DUGC"),
)

ADMIN_URL = '/admin'

STUDENT_URL = '/student'
PROFESSOR_URL = '/professor'
DUGC_URL = '/dugc'

STUDENT_ACCESS_URL = r'^/student/(.*)$'
PROFESSOR_ACCESS_URL = r'^/professor/(.*)$'
DUGC_ACCESS_URL = r'^/dugc/(.*)$'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout'

DEFAULT_FROM_EMAIL = 'webmaster@oars'
SERVER_EMAIL = 'admin@oars'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'oars.django@gmail.com'
EMAIL_HOST_PASSWORD = 'django.oars'
EMAIL_PORT = 587

WAITING = 0
ACCEPTED = 1
REJECTED = 2

REQUEST_STATUS_CHOICES = (
    (WAITING, 'Waiting'),
    (ACCEPTED, 'Accepted'),
    (REJECTED, 'Rejected'),
)