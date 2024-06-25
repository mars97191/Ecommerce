from django.test import TestCase,Client, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
from product.models import Category, Product

from .views import add_to_cart, remove_from_cart, update_cart_quantity, cart_view

class CartViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory().get(reverse('cart:cart'))
        self.middleware = SessionMiddleware(self.factory)
        self.middleware.process_request(self.factory)
        self.factory.session.save()

    def test_cart_view(self):
        request = self.factory
        response = cart_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(self.client, 'cart/cart/detail.html')

