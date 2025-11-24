from rest_framework import viewsets
from .models import parent
from .serializers import ParentSerializer

class ParentViewSet(viewsets.ModelViewSet):
    queryset = parent.objects.all()
    serializer_class = ParentSerializer



