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


class PostDetailViewTests(APITestCase):
    def setUp(self):
        john = User.objects.create_user(
            username='John', password='Trl1209@!3a'
        )
        tim = User.objects.create_user(
            username='Tim', password='Ael@(019Ad'
        )
        Post.objects.create(
            owner=john, title='Title for john', caption='caption for john'
        )
        Post.objects.create(
            owner=tim, title='Title for tim', caption='caption for tim'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'Title for john')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_not_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/918/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(
            username='John', password='Trl1209@!3a'
        )
        response = self.client.put('/posts/1/', {
            'title': 'New title for john',
            'district': 'Mitte',
        })
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'New title for john')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_not_update_post_they_do_not_own(self):
        self.client.login(
            username='John', password='Trl1209@!3a'
        )
        response = self.client.put(
            '/posts/2/', {'title': 'New title for john'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
