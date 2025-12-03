from rest_framework import viewsets, permissions, filters
from rest_framework.parsers import MultiPartParser, FormParser
from .models import student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for Student model.
    Supports: list, retrieve, create, update, partial_update, destroy.
    """
    queryset = student.objects.all().order_by('-id')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]  # for file/image uploads

    # Optional: add search & filtering (by first_name, admission_no, etc.)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name', 'last_name', 'admission_no', 'phone', 'email']
    ordering_fields = ['id', 'admission_date', 'first_name']

