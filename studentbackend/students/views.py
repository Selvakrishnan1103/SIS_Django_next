from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import student
from .serializers import StudentSerializer
from .filters import StudentFilter



class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all().order_by('-admission_date')
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]
  # change as needed

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = StudentFilter

    # fields used by ?search=term (full-text-like across these fields)
    search_fields = [
        'first_name',
        'last_name',
        'admission_no',
        'email',
        'phone',
        'route_name',
        'vechile_no',
        'class_name',
        'section',
        'address',
    ]

    # allow ?ordering=first_name or ?ordering=-admission_date
    ordering_fields = [
        'first_name', 'last_name', 'admission_date', 'admission_no', 'class_name'
    ]
    ordering = ['-admission_date']


