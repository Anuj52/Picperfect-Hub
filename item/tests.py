from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Category, Item


class ItemViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='password123')
        self.category = Category.objects.create(name='Nature')

    def test_new_item_invalid_form_renders(self):
        self.client.login(username='alice', password='password123')

        response = self.client.post(
            reverse('item:new'),
            data={
                'category': self.category.id,
                'name': '',  # required -> invalid
                'description': 'Test',
                'price': '10.00',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Item')

    def test_delete_requires_post(self):
        item = Item.objects.create(
            category=self.category,
            name='Test Photo',
            description='Test',
            price='10.00',
            created_by=self.user,
        )

        self.client.login(username='alice', password='password123')

        response = self.client.get(reverse('item:delete', args=[item.id]))
        self.assertEqual(response.status_code, 405)

        response = self.client.post(reverse('item:delete', args=[item.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Item.objects.filter(id=item.id).exists())
