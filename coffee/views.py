from django.shortcuts import render 
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'coffee-home.html'

class TypeView(TemplateView):
    template_name = 'coffee-type.html'