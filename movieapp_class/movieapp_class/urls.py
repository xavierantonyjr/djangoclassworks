from django.contrib import admin
from django.urls import path
from app2 import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MovieListView.as_view(),name='home'),
    path('addmovie', views.AddMovieView.as_view(), name='addmovie'),
    path('movie/<int:pk>/', views.MovieDetail.as_view(), name='movie_detail'),
    path('editmovie/<int:pk>/',views.EditMovieView.as_view(),name='editmovie'),
    path('delete/<int:pk>/',views.DeleteMovieView.as_view(),name='deletemovie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)