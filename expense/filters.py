import django_filters
from .models import Expense,Income
from django_filters import DateFilter

class ExpenseFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="datetime",lookup_expr='gte')
    end_date=DateFilter(field_name="datetime",lookup_expr='lte')
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'description']

class IncomeFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name="datetime",lookup_expr='gte')
    end_date=DateFilter(field_name="datetime",lookup_expr='lte')
    class Meta:
        model = Income
        fields = ['amount', 'source']        