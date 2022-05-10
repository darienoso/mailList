import django_filters
from django_filters import DateFilter, NumberFilter, DateTimeFromToRangeFilter, widgets

from .models import *


class PersonFilter(django_filters.FilterSet):
    start_age = NumberFilter(field_name="Edad", lookup_expr="gte",label="Edad es >=")
    final_age = NumberFilter(field_name="Edad", lookup_expr="lte",label="Edad es <=")

    start_date = DateTimeFromToRangeFilter(field_name="purchaseDate",widget=widgets.RangeWidget(
        attrs={'type': 'date'}),label="Fecha de compra   ")

    class Meta:
        model = Persons
        fields = ['Ciudad']