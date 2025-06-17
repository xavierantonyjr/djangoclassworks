from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Vehicle
from .forms import VehicleForm

class IndexView(TemplateView):
    template_name = 'inventory/index.html'

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'inventory/vehicle_list.html'
    context_object_name = 'vehicles'

class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = 'inventory/vehicle_detail.html'
    context_object_name = 'vehicle'

class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'inventory/vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleUpdateView(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'inventory/vehicle_form.html'
    success_url = reverse_lazy('vehicle_list')

class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'inventory/vehicle_confirm_delete.html'
    success_url = reverse_lazy('vehicle_list')
