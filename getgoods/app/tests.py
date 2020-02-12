from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.utils import json


class TestUser(APITestCase):

    def setUp(self):
        pass

    def test_user(self):
        # Создание нового пользователя
        response = self.client.post(reverse('admin-user'),
                                    {'email': 'test@test.test',
                                     'password': 'testpassword1'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Авторизация пользователя
        self.client.login(username=self.email, password=self.password)

        # Восстановление пароля пользователя

        response = self.client.post(reverse('admin-recover'), {})
        print(response.data['error'])


#
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
#         url = reverse('app:category-list')
#         response = self.client.get(url)
#         print(response.status_code)