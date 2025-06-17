from django import forms
from app1.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['movie_name','description','directors_name','language','year','image']
    # movie_name = forms.CharField(max_length=50)
    # description = forms.CharField(max_length=50)
    # directors_name = forms.CharField(max_length=50)
    # language = forms.CharField(max_length=50)
    # year = forms.IntegerField()
    # image = forms.ImageField()