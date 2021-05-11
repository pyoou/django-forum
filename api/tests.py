from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from forum import models as m
from django.core import serializers
import json


class TestCategoryListAPIView(APITestCase):

    def test_get_method_is_return_status_200_ok(self):
        url = reverse('category_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_method_is_return_status_201_created(self):
        url = reverse('category_list')
        data = {'name': 'test_category'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(m.Category.objects.all().count(), 1)

    def test_post_method_is_return_status_400_bad_request(self):
        url = reverse('category_list')
        data = {'some': 'test'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(m.Category.objects.all().count(), 0)


class TestQuestionListAPIView(APITestCase):

    def test_get_method_is_return_status_200_ok(self):
        url = reverse('question_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_method_is_return_status_201_created(self):
        category = m.Category.objects.create(name='test_category')
        user = m.NewUser.objects.create_user('test@user.com', 'username', 'nickname', 'password')

        url = reverse('question_list')
        data = {'content': 'test_content', 'category': category.id, 'author': user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(m.Category.objects.all().count(), 1)

    def test_post_method_is_return_status_400_bad_request(self):
        url = reverse('question_list')
        data = {'content': 'test_content', 'category': 1, 'author': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(m.Category.objects.all().count(), 0)


class TestAnswerListAPIView(APITestCase):

    def test_get_method_is_return_status_200_ok(self):
        url = reverse('answer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_method_is_return_status_201_created(self):
        test_category = m.Category.objects.create(name='test_category_2')
        user = m.NewUser.objects.create_user('test@user.com', 'username', 'nickname', 'password')
        question = m.Question.objects.create(content='test', category=test_category, author=user)

        url = reverse('answer_list')
        data = {'question_id': question.id, 'content': 'test content', 'author': user.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_method_is_return_status_400_bad_request(self):
        url = reverse('answer_list')
        data = {'question_id': 1, 'content': 'test content', 'author': 1}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(m.Answer.objects.all().count(), 0)
