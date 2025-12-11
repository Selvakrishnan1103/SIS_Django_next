from rest_framework import serializers
from .models import student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'
        read_only_fields = ('admission_date', 'id',)
