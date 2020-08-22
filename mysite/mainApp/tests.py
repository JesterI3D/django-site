import pytest
import requests
from django.conf import settings
from django.test import TestCase


class TestDB(TestCase):
    @pytest.fixture(scope='session')
    def setting_db(self):
        settings.DATABASES['default'] = \
            {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': 'postgres',
                'USER': 'db',
                'PASSWORD': 'root',
                'HOST': 'db',
                'PORT': '5432'
            }

    def django_db_setup(self):
        settings_ = settings.objects.get(['django.db.backends.postgresql'])
        self.assertEqual(settings_.DATABASES(['default']), "postgres")\


    @pytest.mark.request(transaction=True)
    def test_an_admin_view(self):
        url = 'http://127.0.0.1:8000'
        response = requests.get(url)
        if response.status_code == 200:
            print('Success!')
        elif response.status_code == 404 or 500:
            print('Connection Error!')
        print("TIME RESPONSE FROM SERVER: ", response.elapsed.total_seconds())