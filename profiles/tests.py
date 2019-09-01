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