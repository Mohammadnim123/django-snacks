from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    template_name = 'snacks-home.html' #for home

class AboutView(TemplateView):
    template_name = 'snacks-about.html'
