from django.contrib import admin
from django.urls import path, include
from . import views
from alevelmaths.e_trigonometry import e_trigonometry_views
#from gcsemaths.a_number import aa_ordering_and_comparative_views, ab_ops_with_int_frac_dec_views

e_trigonometry_patterns = [ eval(f"path('{module}/', e_trigonometry_views.{module}, name='{module}')") for module in e_trigonometry_views.modulesList() ]

#a_number_patterns = [ eval(f"path('{module}/', aa_ordering_and_comparative_views.{module}, name='{module}')") for module in aa_ordering_and_comparative_views.modulesList() ]

urlpatterns = [
    path('', views.home, name="gcsemaths-home"),


    path('trigonometry/', views.trigonometry_home, name="trigonometry"),
    path('trigonometry/', include(e_trigonometry_patterns)),

    #path('a_number/', views.home_number, name="number_exam_questions"),
    #path('a_number/', include(a_number_patterns)), 
]
