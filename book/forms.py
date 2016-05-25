from django import forms
from book.models import Book
from django.forms import ModelForm
import magic


class AddForms(ModelForm):

    def clean_file(self):
        pdf = self.cleaned_data['pdf']
        mime = magic.from_buffer(pdf.read(), mime=True)
        print(mime)
        if not mime == 'application/pdf':
            raise forms.ValidationError('File must be a PDF document')
        else:
            return pdf

    class Meta:
        model = Book
        fields = ['name', 'pdf', 'url']
