from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationTests(APITestCase):
    def setUp(self):
        """Set up the test client and initial conditions."""
        self.url = reverse('auth_register')  # Adjust this name as needed
        self.valid_payload = {
            'username': 'testuser',
            'password': 'testpass123',
            'email': 'testuser@example.com',
        }
        self.invalid_payload = {
            'username': '',  # Invalid username
            'password': 'testpass123',
            'email': 'testuser@example.com',
        }

    def test_register_user_success(self):
        """Test user registration with valid data."""
        response = self.client.post(self.url, self.valid_payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'testuser')

    def test_register_user_invalid(self):
        """Test user registration with invalid data."""
        response = self.client.post(self.url, self.invalid_payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)


class SwaggerDocsTest(APITestCase):
    def test_swagger_docs(self):
        url = reverse('schema-swagger-ui')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
