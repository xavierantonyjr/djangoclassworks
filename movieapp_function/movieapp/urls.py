from django.contrib import admin
from django.urls import path
from app1 import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('addmovie',views.addmovie,name='addmovie'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
    path('delete/<int:id>/',views.deletemovie,name='deletemovie'),
    path('editmovie/<int:id>/',views.editmovie,name='editmovie'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)