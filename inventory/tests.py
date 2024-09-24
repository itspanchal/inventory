from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import InventoryItem
from rest_framework_simplejwt.tokens import RefreshToken

class InventoryTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.item_data = {'name': 'Test Item', 'description': 'A test item'}

    def test_create_item(self):
        response = self.client.post(reverse('item-create'), self.item_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item(self):
        item = InventoryItem.objects.create(**self.item_data)
        response = self.client.get(reverse('item-detail', args=[item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        item = InventoryItem.objects.create(**self.item_data)
        updated_data = {'name': 'Updated Item', 'description': 'Updated description'}
        response = self.client.put(reverse('item-detail', args=[item.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        item = InventoryItem.objects.create(**self.item_data)
        response = self.client.delete(reverse('item-detail', args=[item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
