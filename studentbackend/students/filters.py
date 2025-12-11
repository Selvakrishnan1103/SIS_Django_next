import django_filters
from .models import student

class StudentFilter(django_filters.FilterSet):
    # Examples: age range, admission_date range, dob range
    min_age = django_filters.NumberFilter(field_name='age', lookup_expr='gte')
    max_age = django_filters.NumberFilter(field_name='age', lookup_expr='lte')
    admission_date_after = django_filters.DateTimeFilter(field_name='admission_date', lookup_expr='gte')
    admission_date_before = django_filters.DateTimeFilter(field_name='admission_date', lookup_expr='lte')
    dob_after = django_filters.DateFilter(field_name='dob', lookup_expr='gte')
    dob_before = django_filters.DateFilter(field_name='dob', lookup_expr='lte')

    class Meta:
        model = student
        # exact filters user will commonly want
        fields = {
            'class_name': ['exact'],
            'section': ['exact'],
            'blood_group': ['exact'],
            'gender': ['exact'],
            'academic_year': ['exact'],
            'route_name': ['exact'],
            'vechile_no': ['exact'],
        }
