from django.contrib import admin
from django.urls import path, include
from . import views
from a_fundementals_of_computer_programming import aa_fundementals_of_computer_programming

urlpatterns = [
    path('', views.home, name="PCAP-home"),

    path('test/', aa_fundementals_of_computer_programming.select_random_view, name="test"),
]
