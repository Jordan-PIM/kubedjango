from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from .models import Entry


class HelloPageView(ListView):
    template_name = 'demoapp/hello.html'
    model = Entry
    context_object_name = 'all_entry_list'
