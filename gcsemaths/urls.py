from django.contrib import admin
from django.urls import path, include
from . import views
from gcsemaths.exam_questions import exam_non_calc
from gcsemaths.a_number import aa_ordering_and_comparative_views, ab_ops_with_int_frac_dec_views
from gcsemaths.b_algebra import algebra_views
from gcsemaths.e_geometry_and_measure import e_geometry_and_measure_views

exam_non_calc_patterns = [ eval(f"path('{module}/', exam_non_calc.{module}, name='{module}')") for module in exam_non_calc.modulesList() ]

a_number_patterns = [ eval(f"path('{module}/', aa_ordering_and_comparative_views.{module}, name='{module}')") for module in aa_ordering_and_comparative_views.modulesList() ]
a_number_patterns += [ eval(f"path('{module}/', ab_ops_with_int_frac_dec_views.{module}, name='{module}')") for module in ab_ops_with_int_frac_dec_views.modulesList() ] 

b_algebra_patterns = [ eval(f"path('{module}/', algebra_views.{module}, name='{module}')") for module in algebra_views.modulesList() ]

e_geometry_patterns = [ eval(f"path('{module}/', e_geometry_and_measure_views.{module}, name='{module}')") for module in e_geometry_and_measure_views.modulesList() ]

urlpatterns = [
    path('', views.home, name="gcsemaths-home"),

    path('exam_non_calc/', views.home_exam_non_calc, name="exam_non_calc"),
    path('exam_non_calc/', include(exam_non_calc_patterns)),

    path('a_number/', views.home_number, name="number_exam_questions"),
    path('a_number/', include(a_number_patterns)),

    path('b_algebra/', views.home_algebra, name="algebra_exam_questions"),
    path('b_algebra/', include(b_algebra_patterns)),
    #path('algebra_rand/', algebra_views.select_random, name="random-algebra"),

    path('e_geometry/', views.home_geometry, name="algebra_exam_questions"),
    path('e_geometry/', include(e_geometry_patterns))
    
]
