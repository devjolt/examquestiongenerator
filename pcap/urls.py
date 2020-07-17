from django.urls import path, include
from . import views
from pcap.pcap_views import *

urlpatterns = [
    path('', views.home, name="pcap-home"),

    #path('random_pcap/', all_modules.random_pcap, name="random-pcap"),
]

