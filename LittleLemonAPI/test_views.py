from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuViewTest(APITestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Create token
        self.token = Token.objects.create(user=self.user)

        # Create test data
        self.item1 = MenuItem.objects.create(title="Pizza", price=10, inventory=10)
        self.item2 = MenuItem.objects.create(title="Burger", price=5, inventory=15)

    def test_getall(self):
        url = reverse('menu-items')

        # Attach token
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )

        response = self.client.get(url)

        data = MenuItem.objects.all()
        serializer = MenuItemSerializer(data, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)