# coding: utf-8
"""
Settings overrided for test time
"""
from django.conf import settings

INSTALLED_APPS = tuple(settings.INSTALLED_APPS) + (
    'wagtail_modeltranslation.tests',
)

LANGUAGES = (('de', 'Deutsch'),
             ('en', 'English'))
LANGUAGE_CODE = 'de'
MODELTRANSLATION_DEFAULT_LANGUAGE = 'de'

USE_I18N = True
USE_TZ = False
MIDDLEWARE_CLASSES = ()

MODELTRANSLATION_AUTO_POPULATE = False
MODELTRANSLATION_FALLBACK_LANGUAGES = {'default': (MODELTRANSLATION_DEFAULT_LANGUAGE,)}

ROOT_URLCONF = 'wagtail_modeltranslation.tests.urls'
