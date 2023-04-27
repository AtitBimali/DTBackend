
import django_filters
from .models import Event


class EventFilter(django_filters.FilterSet):
    type = django_filters.CharFilter(method='filter_type',label="Type")
    limit = django_filters.NumberFilter(method='filter_limit',label="Limit")
    page = django_filters.NumberFilter(method='filter_page',label="Page")

    class Meta:
        model = Event
        fields = ['page', 'limit']

    def filter_type(self, queryset, name, value):
        return queryset

    def filter_page(self, queryset, name, value):
        page_size = int(self.request.query_params.get('limit', 5))
        start = (int(value) - 1) * page_size
        end = start + page_size
        queryset = queryset[start:end]
        return queryset

    def filter_limit(self, queryset, name, value):
        page = self.request.query_params.get('page', 1)
        page_size = int(self.request.query_params.get('limit', 5))
        start = (int(page) - 1) * page_size
        end = start + value
        return queryset[start:end]