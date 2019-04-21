import os
import django
from django.conf import settings
import pytest

# We manually designate which settings we will be using in an environment variable
# This is similar to what occurs in the `manage.py`
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'techinterview.settings')


# `pytest` automatically calls this function once when tests are run.
def pytest_configure():
    settings.DEBUG = False
    django.setup()


@pytest.fixture(scope='session')
def django_db_setup():
    maindb = settings.DATABASES['default']
