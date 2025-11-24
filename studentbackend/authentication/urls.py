from django.urls import path, include
from rest_framework import routers
from .views import ParentViewSet

router = routers.DefaultRouter()
router.register(r'parents', ParentViewSet, basename='parent')

urlpatterns = [
    path('', include(router.urls)),
]

