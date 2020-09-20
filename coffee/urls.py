from django.urls import path
from .views import HomeView, TypeView

urlpatterns=[
    path('',HomeView.as_view(),name='coffee'),
    path('types',TypeView.as_view(),name='types')
]

