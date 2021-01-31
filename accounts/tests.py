from django.test import TestCase

# Create your tests here.
import json
from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

from accounts.models import User


class TokenTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_token(self):
        username = 'abc'
        email = 'developinghuman1015@gmail.com'
        password = 'password'
        User.objects.create_user(username, email, password)

        data = {'username': username, 'password': password}
        response = self.client.post(reverse('token_obtain_pair'), data, format='json')

        response_content = json.loads(response.content)

        assert response.status_code == 200

        required_fields = [
            'access',
            'refresh',
            'id',
            'first_name',
            'last_name',
            'username',
            'role',
        ]
        response_keys = response_content.keys()
        for required_field in required_fields:
            assert required_field in response_keys
