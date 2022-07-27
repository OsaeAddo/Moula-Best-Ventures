from .base_settings import *

import dj_database_url
import os


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-pzqirc45gpvlkh#wym^fs@!5yb$0x*8a08cy1%gzylu0xv=@92'

SECRET_KEY = os.environ.get('SECRET_KEY', default='django-insecure-pzqirc45gpvlkh#wym^fs@!5yb$0x*8a08cy1%gzylu0xv=@92')

DEBUG = 'RENDER' not in os.environ
DEBUG = True
ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    
    
DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgresql://postgres:postgres@localhost:5432/latestdb',
        conn_max_age=600
    )
}
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
# if not DEBUG:
#     STATIC_ROOT = BASE_DIR / 'staticfiles'
#     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'