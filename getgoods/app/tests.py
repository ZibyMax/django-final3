from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.utils import json


class TestUser(APITestCase):

    def test_can_create_user(self):
        url = reverse('test')
        data = {'question': 'GO?'}
        # response = self.client.post(url, data=data, content_type='json')
        response = self.client.post(url, {'question': 'b'})
        print(response.status_code)
        print(response.data['answer'])






# class TestCategory(APITestCase):
#
#     # def test_create_category(self):
#     #     url_detail = reverse('app:category-detail', kwargs={'pk': 1})
#     #     print(url_detail)
#     #     url_list = reverse('app:category-list')
#     #     print((url_list))
#     #     url = reverse('price', args=[1])
#     #     print(url)
#
#     def setUp(self):
#         pass
#
#     def test_can_create_category(self):
#         pass