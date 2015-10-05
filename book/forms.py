from django import forms
from book.models import Book


class BookForms(forms.Form):
    class Meta:
        model = Book
        fields = ['name', 'note', 'pdf']
