import django_filters
from .models import parent

class parentFilter(django_filters.FilterSet):
    # Examples: age range, dob range
    min_age = django_filters.NumberFilter(field_name='age', lookup_expr='gte')
    max_age = django_filters.NumberFilter(field_name='age', lookup_expr='lte')
    dob_after = django_filters.DateFilter(field_name='dob', lookup_expr='gte')
    dob_before = django_filters.DateFilter(field_name='dob', lookup_expr='lte')

    class Meta:
        model = parent
        # exact filters user will commonly want
        fields = {
            'parent_Occupation': ['exact'],}