from django.urls import path
from one_app import views

urlpatterns = [
    path('', views.index),
    ]