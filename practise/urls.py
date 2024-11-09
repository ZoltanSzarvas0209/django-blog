from . import views
from django.urls import path

urlpatterns = [
    path('', views.practise_one, name='practise'),
]