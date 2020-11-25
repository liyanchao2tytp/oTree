'''
Author: lyc
Date: 2020-09-25 12:56:39
LastEditors: lyc
LastEditTime: 2020-11-25 20:39:15
Description: file content
'''
from os import environ
import os



SESSION_CONFIGS = [
    dict(
        name='Test',
        display_name="Test",
        num_demo_participants=3,
        app_sequence=['login','public_goods','my_trust','questionnaire_investigations']
        #'login','one_questionnaire','pre_public_goods', 'public_goods', 'my_trust','pre_public_goods',
    ),
]

ROOT_URLCONF = 'urls'

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
# SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))
# # Find templates in the same folder as settings.py.
# TEMPLATE_DIRS = (
#     os.path.join(SETTINGS_PATH, 'one_questionnaire/templates/one_questionnaire'),
# )
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR,'oTree/one_questionnaire/templates').replace('\\','/')
        ],
        'APP_DIRS':True,
    },
]


# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'zh-hans'


STATIC_ROOT = os.path.join(PROJECT_DIR, 'collect_static')
STATIC_URL = '/static/'



#DEBUG = False

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = []

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'g^*7ma&hn*a&@d7swv!%#^6qnow4@glu1k#t=pf@pj)(l*d*jt'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
