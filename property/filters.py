import django_filters
from property.models import Property
from django import forms
from django.db.models import Q


class PropertyFilter(django_filters.FilterSet):
    # City filter
    city = django_filters.CharFilter(field_name='city', lookup_expr='icontains')

    # Price and size filters with custom methods
    property_price_min = django_filters.NumberFilter(field_name='property_price', lookup_expr='gte')
    property_price_max = django_filters.NumberFilter(method='filter_price_max')

    squaremeters_min = django_filters.NumberFilter(field_name='squaremeters', lookup_expr='gte')
    squaremeters_max = django_filters.NumberFilter(method='filter_size_max')

    # Date Range
    listing_start = django_filters.DateFilter(field_name='listing_date', lookup_expr='gte')
    listing_end = django_filters.DateFilter(field_name='listing_date', lookup_expr='lte')

    # Property Type
    type = django_filters.CharFilter(field_name='property_type', lookup_expr='iexact')

    # Status (is_sold)
    status = django_filters.CharFilter(method='filter_status')

    # Search
    search = django_filters.CharFilter(method='filter_search')

    def filter_price_max(self, queryset, name, value):
        # If value is -1 or not provided, don't apply any maximum filter
        if value is None or value == -1:
            return queryset
        # Otherwise, filter normally
        return queryset.filter(property_price__lte=value)

    def filter_size_max(self, queryset, name, value):
        # If value is -1 or not provided, don't apply any maximum filter
        if value is None or value == -1:
            return queryset
        # Otherwise, filter normally
        return queryset.filter(squaremeters__lte=value)

    def filter_status(self, queryset, name, value):
        if value.lower() == 'available':
            return queryset.filter(is_sold=False)
        elif value.lower() == 'sold':
            return queryset.filter(is_sold=True)
        return queryset

    def filter_search(self, queryset, name, value):
        if value:
            return queryset.filter(
                Q(property_address__icontains=value) |
                Q(description__icontains=value) |
                Q(city__icontains=value) |
                Q(property_type__icontains=value) |
                Q(postalcode__icontains=value)
            )
        return queryset

    class Meta:
        model = Property
        fields = [
            'city',
            'type',
            'status',
            'property_price_min',
            'property_price_max',
            'squaremeters_min',
            'squaremeters_max',
            'listing_start',
            'listing_end',
            'search',
            'postalcode',
        ]