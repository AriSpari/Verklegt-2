import django_filters
from property.models import Property


class PropertyFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')

    property_price_min = django_filters.NumberFilter(field_name='property_price', lookup_expr='gte')
    property_price_max = django_filters.NumberFilter(field_name='property_price', lookup_expr='lte')

    squaremeters_min = django_filters.NumberFilter(field_name='squaremeters', lookup_expr='gte')
    squaremeters_max = django_filters.NumberFilter(field_name='squaremeters', lookup_expr='lte')

    listing_date = django_filters.DateFromToRangeFilter(field_name='listing_date')

    class Meta:
        model = Property
        fields = {
            'property_type': ['iexact'],
            'is_sold': ['exact'],
        }

