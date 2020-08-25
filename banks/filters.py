import django_filters
from django_filters import DateFilter, CharFilter

from .models import *
class OrderFilter(django_filters.FilterSet):
    start_amount = django_filters.NumberFilter(field_name="amount", lookup_expr='gte')
    end_amount = django_filters.NumberFilter(field_name="amount", lookup_expr='lte')
    start_date = DateFilter(field_name="date_pub", lookup_expr='gte')
    end_date = DateFilter(field_name="date_pub", lookup_expr='lte')

    class Meta:
        model = Transaction
        fields = '__all__'
        exclude = ['payer', 'date_pub', 'amount']
