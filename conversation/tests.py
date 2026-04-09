from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from item.models import Category, Item

from .models import Conversation


class ConversationViewsTests(TestCase):
    def setUp(self):
        self.seller = User.objects.create_user(username='seller', password='password123')
        self.buyer = User.objects.create_user(username='buyer', password='password123')
        self.intruder = User.objects.create_user(username='intruder', password='password123')

        category = Category.objects.create(name='People')
        self.item = Item.objects.create(
            category=category,
            name='Portrait',
            description='Test',
            price='12.50',
            created_by=self.seller,
        )

        self.conversation = Conversation.objects.create(item=self.item)
        self.conversation.members.add(self.seller, self.buyer)

    def test_conversation_detail_requires_membership(self):
        self.client.login(username='intruder', password='password123')

        response = self.client.get(reverse('conversation:detail', args=[self.conversation.id]))
        self.assertEqual(response.status_code, 404)

    def test_conversation_detail_allows_member(self):
        self.client.login(username='buyer', password='password123')

        response = self.client.get(reverse('conversation:detail', args=[self.conversation.id]))
        self.assertEqual(response.status_code, 200)
