from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"profiles", views.ProfileViewSet)
router.register(r"status", views.ProfileStatusViewSet, base_name="status")

# profile_list = views.ProfileViewSet.as_view({"get":"list"})
# profile_detail = views.ProfileViewSet.as_view({"get":"retrieve"})

urlpatterns = [
    # path('profiles/', views.ProfileList.as_view(), name='profile-list'),
    # path("profiles/", profile_list, name="profile-list"),
    # path('profiles/<int:pk>/', profile_detail, name="profile-detail"),
    path("", include(router.urls)),
    path("avatar/", views.AvatarUpdateView.as_view(), name="avatar-update"),
]