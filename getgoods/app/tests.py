from django.test import TestCase
from rest_framework.test import APITestCase, APIClient

# Create your tests here.


class TestOneEqualOne(TestCase):

    def test_11(self):
        self.assertEqual(1, 1)

    def test_12(self):
        self.assertEqual(1, 2)