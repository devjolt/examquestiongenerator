from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Trying-things-out"),
    path('experiment/', views.experiment, name="Trying-things-out"),
]