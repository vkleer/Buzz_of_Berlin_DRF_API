from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Profile


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        """
        Runs before every test, creating two test users and profiles,
        which is done automatically with a signal
        """
        john = User.objects.create_user(
            username='John', password='Trl1209@!3a'
        )
        tim = User.objects.create_user(
            username='Tim', password='Ael@(019Ad'
        )

    def test_user_can_view_existing_profile(self):
        """
        Test to check if a user can view an existing profile
        """
        self.client.login(
            username='John', password='Trl1209@!3a'
        )
        response = self.client.get('/profiles/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_not_view_non_existent_profile(self):
        """
        Test to check if a user can view a profile which doesn't exist
        """
        self.client.login(
            username='John', password='Trl1209@!3a'
        )
        response = self.client.get('/profiles/1839')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_their_own_profile(self):
        """
        Test to check if a user can update their own profile
        """
        self.client.login(
            username='John', password='Trl1209@!3a'
        )
        response = self.client.put('/profiles/1',
                                   {'description': 'A new description'})
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.description, 'A new description')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_not_update_other_profiles(self):
        """
        Test to check if a user is unable to update another users' profile
        """
        self.client.login(
            username='John', password='Trl1209@!3a'
        )
        response = self.client.put('/profiles/2',
                                   {'description': 'A new description'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_out_user_can_not_update_a_profile(self):
        """
        Test to check if a logged out user is unable to update a profile
        """
        response = self.client.put('/profiles/2',
                                   {'description': 'A new description'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
