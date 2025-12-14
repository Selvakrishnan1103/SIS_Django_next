from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import teacher
from .serializers import TeacherSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .pagination import TeacherPagination

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    pagination_class = TeacherPagination
    search_fields = [
        'first_name',
        'second_name',
        'Role',
        'phone',
        'Blood_group',
        'Marital_Status',
        'Father_name',
        'Mother_name',
        'Language_Known',
        'Qualification',
        'Work_Experience',
        'address',
    ]


# Create your views here.
