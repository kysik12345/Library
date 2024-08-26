from .models import *
from django import forms 

class AuthorForms(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
