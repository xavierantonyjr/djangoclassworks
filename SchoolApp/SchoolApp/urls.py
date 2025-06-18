from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signout/', views.SignoutView.as_view(), name='signout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
