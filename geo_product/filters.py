from django_filters import rest_framework as filters
from .models import GeoProduct


class GeoProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    os_platform = filters.MultipleChoiceFilter(field_name="os_platform", choices=GeoProduct.OS_CHOICES)

    class Meta:
        model = GeoProduct
        fields = ['min_price', 'max_price', 'os_platform']
