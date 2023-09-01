from django.shortcuts import render
from application.models import Book
from django.views.generic import TemplateView


class BookView(TemplateView):
    model = Book
    template_name = 'application/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        return {'books': Book.objects.all()}

