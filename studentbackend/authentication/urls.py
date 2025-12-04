from django.urls import path, include
from rest_framework import routers
from .views import parentViewSet

router = routers.DefaultRouter()
router.register(r'parents', parentViewSet, basename='parent')

urlpatterns = [
    path('', include(router.urls))
]


