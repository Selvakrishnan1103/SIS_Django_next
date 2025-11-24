from rest_framework import serializers
from .models import parent   # use the correct model class name

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = parent
        fields = '__all__'
