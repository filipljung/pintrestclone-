 import os
 import dj_database_url
 import django_heroku

 if os.path.isfile('env.py'):
     import env
 SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['*']

 # DATABASES = {
 #     'default': {
 #         'ENGINE': 'django.db.backends.sqlite3',
 #         'NAME': BASE_DIR / 'db.sqlite3',
 #     }
 # }
    
 DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }


STATIC_URL ='/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_DIRS = (os.path.join(BASE_DIR, 'static'),)
django_heroku.settings(locals())