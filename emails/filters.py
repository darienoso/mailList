import django_filters
from django_filters import DateFilter, NumberFilter

from .models import *

class PersonFilter(django_filters.FilterSet):
    start_age = NumberFilter(field_name="age",lookup_expr="gte")
    final_age = NumberFilter(field_name="age",lookup_expr="lte")
    start_date = DateFilter(field_name="purchaseDate",lookup_expr="gte")
    final_date = DateFilter(field_name="purchaseDate",lookup_expr="lte")
    class Meta:
        model = Persons
        fields = 'name','city','age'
