from django.urls import path
from . import views

app_name="app2"

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('addition/', views.addition, name='addition'),
    path('factorial/', views.factorial, name='factorial'),
    path('bmi/', views.bmi_calculator, name='bmi'),
]
