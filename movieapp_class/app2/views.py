from django.shortcuts import render, redirect,  get_object_or_404
from .forms import MovieForm
from .models import Movie
from django.views import View
from django.views.generic import DetailView, CreateView


# class HomeMovieView(View):
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, 'index.html', {'movies': movies})
#
#     def post(self, request):
#         search_query = request.POST.get('search', '')
#         return render(request, 'index.html', {'movies': Movie.objects.filter(movie_name__icontains=search_query)})

from django.views.generic import ListView
class MovieListView(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movies'

# class AddMovieView(View):
#     def get(self, request):
#         form_instance = MovieForm()
#         return render(request, 'addmovie.html', {'form': form_instance})
#
#     def post(self, request):
#         form_instance = MovieForm(request.POST, request.FILES)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('home')
#         return render(request, 'addmovie.html', {'form': form_instance})

from django.views.generic import CreateView
from django.urls import reverse_lazy

class AddMovieView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'addmovie.html'
    success_url = reverse_lazy('home')

class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie_detail.html'
    context_object_name = 'movie'

from django.views.generic.edit import UpdateView

class EditMovieView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'editmovie.html'
    success_url = reverse_lazy('home')

# class EditMovieView(View):
#     def get(self, request, id):
#         movie = Movie.objects.get(id=id)
#         form_instance = MovieForm(instance=movie)
#         return render(request, 'editmovie.html', {'form': form_instance})
#
#     def post(self, request, id):
#         movie = Movie.objects.get(id=id)
#         form_instance = MovieForm(request.POST, request.FILES, instance=movie)
#         if form_instance.is_valid():
#             form_instance.save()
#             return redirect('home')
#         return render(request, 'editmovie.html', {'form': form_instance})

from django.views.generic.edit import DeleteView
class DeleteMovieView(DeleteView):
    model = Movie
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('home')

# class DeleteMovieView(View):
#     def get(self, request, id):
#         movie = Movie.objects.get(id=id)
#         return render(request, 'confirm_delete.html', {'movie': movie})
#
#     def post(self, request, id):
#         movie = get_object_or_404(Movie, id=id)
#         movie.delete()
#         return redirect('home')
