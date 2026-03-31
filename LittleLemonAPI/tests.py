from django.test import TestCase
from .models import MenuItem

# Create your tests here.


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='Icecream', price=80.0, inventory=100)
        self.assertEqual(str(item), "Icecream:80.0")