from typing import Sequence
from django.shortcuts            import render
from django.views.generic.list   import ListView
from django.views.generic.edit   import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models                     import photo
class PhotoList(ListView):
    model = photo
    template_name_suffix = '_list'

class PhotoCreate(CreateView):
    model = photo
    fields = ['text','image']
    template_name_suffix = '_create'
    success_url = '/'

class PhotoUpdate(UpdateView):
    model = photo
    fields = ['text','image']
    template_name_suffix = '_update'
    success_url = '/'

class PhotoDelete(DeleteView):
    model = photo
    fields = ['text','image']
    template_name_suffix = '_delete'
    success_url = '/'

class PhotoDetail(DetailView):
    model = photo
    fields = ['text','image']
    template_name_suffix = '_detail'
    success_url = '/'