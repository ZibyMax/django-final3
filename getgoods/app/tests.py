from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient


class TestCategory(APITestCase):

    def test_create_category(self):
        url_detail = reverse('app:category-detail', kwargs={'pk': 1})
        print(url_detail)
        url_list = reverse('app:category-list')
        print((url_list))
        url = reverse('price', args=[1])
        print(url)