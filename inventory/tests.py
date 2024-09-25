from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from inventory.models import Item  # Import your Item model

User = get_user_model()


class InventoryItemTests(APITestCase):
    def setUp(self):
        """Set up a user and an inventory item for testing."""
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.item = Item.objects.create(name='Test Item', description='A test item.')
        self.token = self.obtain_jwt_token()

    def obtain_jwt_token(self):
        """Obtain a JWT token for the user."""
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        return response.data['access']

    def test_create_item(self):
        """Test creating a new inventory item with JWT authentication."""
        url = reverse('item_create')  # Replace with your actual URL name
        data = {'name': 'New Item', 'description': 'A new item.'}
        response = self.client.post(url, data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_existing_item(self):
        """Test creating an item that already exists."""
        url = reverse('item_create')  # Replace with your actual URL name
        data = {'name': 'Test Item', 'description': 'A duplicate item.'}
        response = self.client.post(url, data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_read_item(self):
        """Test reading an existing inventory item."""
        url = reverse('item_detail', kwargs={'pk': self.item.id})  # Replace with your actual URL name
        response = self.client.get(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        """Test updating an existing inventory item."""
        url = reverse('item_detail', kwargs={'pk': self.item.id})  # Replace with your actual URL name
        data = {'name': 'Updated Item', 'description': 'An updated description.'}
        response = self.client.put(url, data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        """Test deleting an existing inventory item."""
        url = reverse('item_detail', kwargs={'pk': self.item.id})  # Replace with your actual URL name
        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
