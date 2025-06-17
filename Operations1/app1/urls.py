from django.urls import path
from . import views

app_name="app2"

urlpatterns = [
    path('', views.addition, name='addition'),
    path('factorial/', views.factorial, name='factorial'),
    path('bmi/', views.bmi_calculator, name='bmi'),
    path('signup/',views.signup,name='signup'),
    path('calorie/',views.calorie,name='dailycalorie'),
]
