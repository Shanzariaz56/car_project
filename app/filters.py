import django_filters
from .models import *

class carFilter(django_filters.FilterSet):
    class Mete:
        name=django_filters.CharFilter("name",lookup_expr="icontain")
        model=Car
        fields="__all__"