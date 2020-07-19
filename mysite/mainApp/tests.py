import pytest
import requests

import mysite.mysite.settings


@pytest.fixture(scope='session')
def django_db_setup():
    mysite.mysite.settings.DATABASES['default'] = \
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
        print('Success!')
    elif response.status_code == 404 or 500:
        print('Connection Error!')
    print(response.elapsed.total_seconds())