from rest_framework import (generics, mixins,
                            viewsets, permissions,
                            filters)
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

class AvatarUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.ProfileAvatarSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        profile_obj = self.request.user.profile
        return profile_obj

class ProfileViewSet(mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated,
                        custom_permissions.IsOwnProfileOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["city"]

class ProfileStatusViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.ProfileStatusSerializer
    permission_classes = [permissions.IsAuthenticated,
                        custom_permissions.IsOwnStatusOrReadOnly]
    
    def get_queryset(self):
        queryset = models.ProfileStatus.objects.all()
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = queryset.filter(user_profile__user__username=username)
        
        return queryset

    def perform_create(self, serializer):
        user_profile = self.request.user.profile
        serializer.save(user_profile=user_profile)