from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Test', price=10, inventory=1)

    def test_title(self):
        menu = Menu.objects.get(id=1)
        self.assertEqual(menu.title, "Test")

    def test_price(self):
        menu = Menu.objects.get(id=1)
        self.assertEqual(menu.price, 10)
