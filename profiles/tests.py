import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from profiles.api import serializers

from . import models

class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {"username": "testcase", "email":"test@test.com",
                "password1": "StrongPassword", "password2": "StrongPassword"}

        response = self.client.post("/api/v1/rest-auth/registration/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ProfileViewSetTestCase(APITestCase):
    list_url = reverse('profile-list')

    def setUp(self):
        self.user = User.objects.create_user(username="test1",
                                             password="test12345678")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
    
    def test_profile_list_authenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenitcated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_profile_detail_retrieve(self):
        response = self.client.get(reverse('profile-detail', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["user"], "test1")

    def test_profile_update_by_owner(self):
        response = self.client.put(reverse('profile-detail', kwargs={"pk": 1}),
                                        {"city": "TestCity", "bio": "TestBio"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content),
                        {"id": 1, "user": "test1", "bio": "TestBio",
                        "city": "TestCity", "avatar":None})

    def test_profile_update_by_random_user(self):
        random_user = User.objects.create_user(username="random",
                                                password="random12345")
        self.client.force_authenticate(user=random_user)
        response = self.client.put(reverse("profile-detail", kwargs={"pk":1}),
                                            {"bio": "Bio Hacked!"})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
