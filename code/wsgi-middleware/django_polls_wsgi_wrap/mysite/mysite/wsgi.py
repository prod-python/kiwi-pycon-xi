"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

from latency_reporter import MyLatencyReporter
from opentelemetry.instrumentation.wsgi import OpenTelemetryMiddleware

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()
application = OpenTelemetryMiddleware(application)

application = MyLatencyReporter(application)
