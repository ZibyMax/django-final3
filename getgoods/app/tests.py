from django.urls import reverse
from rest_framework.test import APITestCase, APIClient


class TestCategory(APITestCase):

    def test_create_category(self):
        url = reverse('order')
        print(url)