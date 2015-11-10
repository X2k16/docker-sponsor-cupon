# encoding=utf-8
import os
from ticket.settings import *

STATIC_ROOT = "/app/static"
STATIC_URL = "/sponsor/static/"
MEDIA_ROOT = "/media"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/var/lib/sqlite3/db.sqlite3',
    }
}

WEBDRIVER = "chrome-hub"
WEBDRIVER_URL = "http://hub:4444/wd/hub"
TICKET_EMAIL_FORMAT = os.environ.get("TICKET_EMAIL_FORMAT")
PTX_EVENT_ID = os.environ.get("PTX_EVENT_ID")
PTX_TICKET_ID = os.environ.get("PTX_TICKET_ID")
PTX_CUPON_CODE = os.environ.get("PTX_CUPON_CODE")
