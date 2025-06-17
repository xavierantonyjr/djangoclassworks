from django.urls import path
from . import views

app_name = 'emp'

urlpatterns = [
    path('',views.employee_list,name='employee_list'),
    path('create_employee/',views.employee_create,name='employee_create'),
    path('employee_details/<int:id>/',views.employee_details,name='employee_details'),
    path('delete_employee/<int:id>/',views.employee_delete,name='employee_delete'),
    path('update_employee/<int:id>/',views.employee_update,name='employee_update'),
]