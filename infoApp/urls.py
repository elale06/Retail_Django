from django.urls import path
from infoApp import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]