import pytest
import requests


@pytest.mark.django_db(transaction=True)
def transaction():
    response = requests.get('http://127.0.0.1:8000/')

    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')