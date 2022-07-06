from .base_settings import *



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pzqirc45gpvlkh#wym^fs@!5yb$0x*8a08cy1%gzylu0xv=@92'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



STATICFILES_DIRS = [
    BASE_DIR / 'static'
]