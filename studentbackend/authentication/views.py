from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.parsers import MultiPartParser, FormParser
from .models import parent
from .serializers import ParentSerializer
from.filter import parentFilter
from django_filters.rest_framework import DjangoFilterBackend

class parentViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for Student model.
    Supports: list, retrieve, create, update, partial_update, destroy.
    """
    queryset = parent.objects.all().order_by('-id')
    serializer_class = ParentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser] 
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = parentFilter

    search_fields = [
        'first_name',
        'last_name',
        'email',
        'phone',
        'occupation',
        'address',
    ]


    # Optional: add search & filtering (by first_name, admission_no, etc.)
   



