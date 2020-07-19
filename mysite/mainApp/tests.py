import pytest
import requests

from mysite.mysite import settings


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = \
        {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'sqlite.db',
            'USER': 'JesterI3D',
            'PASSWORD': 'root',
            'HOST': '172.0.0.2',
            'PORT': '3306'
        }


@pytest.mark.request(transaction=True)
def test_an_admin_view():
    url = 'http://127.0.0.1:8000'
    response = requests.post(url, data={'key': 'value'}, timeout=1)
    if response.status_code == 200:
        return 1
    elif response.status_code == 404 or 500:
        return ConnectionError
    print(response.elapsed.total_seconds())