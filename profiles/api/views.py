from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles import models
from . import serializers

class ProfileList(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [IsAuthenticated]