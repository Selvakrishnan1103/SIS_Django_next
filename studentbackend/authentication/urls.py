from django.urls import path, include
from rest_framework import routers
from .views import ParentPhotoUpload, ParentViewSet

router = routers.DefaultRouter()
router.register(r'parents', ParentViewSet, basename='parent')

urlpatterns = [
    path('', include(router.urls)),
    path('parent/<int:pk>/upload-photo/', ParentPhotoUpload.as_view(), name='parent-photo-upload'),
]


