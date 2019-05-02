from django.shortcuts import render
from django.db.models import Q

from .models import Book
from .filters import BookFilterSet


def index(request):
    #### 舊的
    # q = request.GET.get('q', '')
    # books = Book.objects.all()
    # if q:
    #     books = books.filter(name__icontains=q)
    # return render(request, 'books/index.html', {
    #     'books': books,
    # })

    #### 新的
    filter = BookFilterSet(request.GET or None, queryset=Book.objects.all())
    return render(request, 'books/filter-index.html', {
        'filter': filter,
    })

def result(request):
    q = request.GET.get('q', '')

    books = None
    if q:
        books = Book.objects.filter(
            Q(name__icontains=q) | Q(author__name__icontains=q)
        )
    else:
        filter = BookFilterSet(request.GET or None, queryset=Book.objects.all())
        books = filter.qs

    return render(request, 'books/result.html', {
        'books': books,
    })