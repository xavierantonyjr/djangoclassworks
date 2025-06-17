# from django import forms
#
# class BookForm(forms.Form):
#     title=forms.CharField(max_length=50)
#     author=forms.CharField(max_length=50)
#     price=forms.IntegerField()
#     pages=forms.IntegerField()
#     language=forms.CharField(max_length=50)
#     image=forms.ImageField()

from django import forms
from books.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

