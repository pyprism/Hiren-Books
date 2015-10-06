from django import forms
from book.models import Book
from django.forms import ModelForm


class BookForms(forms.Form):
    class Meta:
        model = Book
        fields = ['name', 'note']


class AddForms(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'pdf']
