"""
WSGI config for Wymarzony_pies_szkolenia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Wymarzony_pies_szkolenia.settings')

application = get_wsgi_application()
