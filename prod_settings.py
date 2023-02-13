
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-iyvj!sdce5rsg*_xs@dpe*mc093c5aj^4p5oe7&smp3m_pohow'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_ROOT = os.path.join(BASE_DIR,"static")