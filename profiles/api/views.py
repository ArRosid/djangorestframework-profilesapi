from rest_framework import generics, mixins, viewsets
from rest_framework import permissions
from profiles import models
from . import serializers
from . import permissions as custom_permissions

# class ProfileList(generics.ListAPIView):
#     queryset = models.Profile.objects.all()
#     serializer_class = serializers.ProfileSerializer
#     permission_classes = [IsAuthenticated]

# class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = models.Profile.objects.all()
#     serializer_class = serializers.ProfileSerializer
#     permission_classes = [IsAuthenticated]

class ProfileViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,
                        custom_permissions.IsOwnProfileOrReadOnly]


class ProfileStatusViewSet(viewsets.ModelViewSet):
    queryset = models.ProfileStatus.objects.all()
    serializer_class = serializers.ProfileStatusSerializer
    permission_classes = [permissions.IsAuthenticated,
                        custom_permissions.IsOwnStatusOrReadOnly]
    
    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)