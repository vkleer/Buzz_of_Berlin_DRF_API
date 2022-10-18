from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username='John', password='Trl1209@!3a'
        )

    def test_can_list_posts(self):
        john = User.objects.get(username='John')
        Post.objects.create(owner=john, title='title for john')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        self.client.login(
            username='John', password='Trl1209@!3a'
        )
        response = self.client.post('/posts/', {
            'title': 'title for john',
            'district': 'Mitte',
        })
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_can_not_create_post(self):
        response = self.client.post('/posts/', {'title': 'title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
