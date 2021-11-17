from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy


# Create your views here.


class SnackListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = 'object_list'


class SnackDetailView(DetailView):
    template_name = "snacks/snack_detail.html"
    model = Snack


class SnackCreateView(CreateView):
    template_name = "snacks/create.html"
    model = Snack
    fields = ['title', 'description', 'purchaser']
    context_object_name = 'object_create'


class SnackUpdateView(UpdateView):
    template_name = "snacks/update.html"
    model = Snack
    fields = ['title', 'description', 'purchaser']
    context_object_name = 'object_update'


class SnackDeleteView(DeleteView):
    template_name = "snacks/delete.html"
    model = Snack
    success_url = reverse_lazy('snack_list')
    context_object_name = 'object_delete'