from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),

    path('signup/', views.SignupView.as_view(), name='signup'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('signout/', views.SignOutView.as_view(), name='signout'),
    path('verify/', views.VerifyView.as_view(), name='verify'),

    path('admin_home/', views.AdminHomeView.as_view(), name='admin_home'),
    path('student_home/', views.StudentHomeView.as_view(), name='student_home'),
    path('staff_home/', views.StaffHomeView.as_view(), name='staff_home'),

    path('accounts/', include('django.contrib.auth.urls')),
]
