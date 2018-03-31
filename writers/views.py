from django.shortcuts import render, get_object_or_404

from .models import Author


def index(request):
    authors = Author.objects.order_by('start_carrier')

    context = {
        'authors': authors
    }

    return render(request, 'index.html', context)


def books(request, author_id):
    query = {
        'id': author_id
    }

    author = get_object_or_404(Author, **query)

    context = {
        'author': author,
        'books': author.books.all()
    }

    return render(request, 'book-store.html', context)
