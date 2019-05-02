import django_filters

from .models import Book


class BookFilterSet(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'name': ['icontains'],
            'price': ['lt', 'gt'],
            'author': ['exact'],
        }