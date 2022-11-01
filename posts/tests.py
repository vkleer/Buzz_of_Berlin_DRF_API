from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Post


class PostListViewTests(APITestCase):
    def setUp(self):
        """
        Runs before every test, creating a test user
        """
        User.objects.create_user(
            username='John', password='Trl1209@!3a'
        )

    def test_can_list_posts(self):
        """
        Test to check if a logged in user can list posts
        """
        john = User.objects.get(username='John')
        Post.objects.create(owner=john, title='title for john')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_create_post(self):
        """
        Test to check if a logged in user can create a post
        """
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
        """
        Test to check if an anonymous user is unable to create a post
        """
        response = self.client.post('/posts/', {'title': 'title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        """
        Runs before every test, creating two test users
        """
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
        """
        Test to check if a post can be retrieved with a valid ID
        """
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'Title for john')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_not_retrieve_post_using_invalid_id(self):
        """
        Test to check if a post is unable to be retrieved with an invalid ID
        """
        response = self.client.get('/posts/918/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        """
        Test to check if a user can update their own posts
        """
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
        """
        Test to check if a user is unable to update a post they do not own
        """
        self.client.login(
            username='John', password='Trl1209@!3a'
        )
        response = self.client.put(
            '/posts/2/', {'title': 'New title for john'}
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
