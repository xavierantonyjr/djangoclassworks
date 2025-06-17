from django.shortcuts import render, redirect,  get_object_or_404
from .forms import MovieForm
from .models import Movie

def home(request):
    movies = Movie.objects.all()
    return render(request, 'index.html',{'movies':movies})

def addmovie(request):
    if request.method == 'POST':
        form_instance = MovieForm(request.POST,request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            # m = Movie.objects.create(
            #     movie_name = form_instance.cleaned_data['movie_name'],
            #     description = form_instance.cleaned_data['description'],
            #     directors_name = form_instance.cleaned_data['directors_name'],
            #     language = form_instance.cleaned_data['language'],
            #     year = form_instance.cleaned_data['year'],
            #     image = form_instance.cleaned_data['image'],
            # )
            # m.save()
            return redirect('home')
    form_instance = MovieForm()
    return render(request, 'addmovie.html', {'form': form_instance})


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'movie_detail.html', {'movie': movie})

def deletemovie(request, id):
    movie = Movie.objects.get(id=id)
    movie.delete()
    return redirect('home')

def editmovie(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'POST':
        form_instance = MovieForm(request.POST,request.FILES,instance=movie)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('home')
    form_instance = MovieForm(instance=movie)
    return render(request, 'editmovie.html', {'form': form_instance})