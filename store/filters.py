import django_filters
from store.models import *
from django_filters import DateFilter
class OrderFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="Year",lookup_expr='gte')
    class Meta:
        model=Games
        fields='__all__'