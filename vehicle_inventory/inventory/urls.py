from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('vehicle_list/', views.VehicleListView.as_view(), name='vehicle_list'),
    path('vehicle/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),
    path('vehicle/new/', views.VehicleCreateView.as_view(), name='vehicle_add'),
    path('vehicle/<int:pk>/edit/', views.VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicle/<int:pk>/delete/', views.VehicleDeleteView.as_view(), name='vehicle_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
