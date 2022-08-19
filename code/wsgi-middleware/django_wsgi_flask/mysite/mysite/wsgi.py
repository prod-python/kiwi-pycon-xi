import os

from django.core.wsgi import get_wsgi_application

from v2_flask_app import FlaskAppWrapper

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
application = FlaskAppWrapper(application)
