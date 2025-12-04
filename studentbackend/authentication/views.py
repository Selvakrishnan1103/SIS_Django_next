from rest_framework import viewsets, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from .models import parent
from .serializers import ParentSerializer

class parentViewSet(viewsets.ModelViewSet):
    """
    Full CRUD for Student model.
    Supports: list, retrieve, create, update, partial_update, destroy.
    """
    queryset = parent.objects.all().order_by('-id')
    serializer_class = ParentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    parser_classes = [MultiPartParser, FormParser]  # for file/image uploads

    # Optional: add search & filtering (by first_name, admission_no, etc.)
   



