from book.models import Book
from django.forms import ModelForm


class AddForms(ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'pdf', 'url', 'current_url']
