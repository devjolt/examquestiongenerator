from django.urls import path, include
from . import views
from physics.a_particles_and_radiation import a_particles_and_radiation_views
from physics.d_electricity import d_electricity_views
from physics.e1_further_mechanics import e1_further_mechanics_views

a_particles_and_radiation_patterns = [
    path('particles_and_radiation_printable_A_question/', a_particles_and_radiation_views.random_printable_A_question, name='random_printable_A_question'),
    path('particles_and_radiation_printable_B_question/', a_particles_and_radiation_views.random_printable_B_question, name='random_printable_B_question'),
    path('particles_and_radiation_printable_A_section/', a_particles_and_radiation_views.random_printable_A_section, name='random_printable_A_section'),
    path('particles_and_radiation_printable_B_section/', a_particles_and_radiation_views.random_printable_B_section, name='random_printable_B_section'),
    path('particles_and_radiation_interactive_A_question/', a_particles_and_radiation_views.random_interactive_A_question, name='random_interactive_A_question'),
    path('particles_and_radiation_interactive_B_question/', a_particles_and_radiation_views.random_interactive_B_question, name='random_interactive_B_question'),
]+[ eval(f"path('{module}/', a_particles_and_radiation_views.{module}, name='{module}')") for module in a_particles_and_radiation_views.modulesList()]

d_electricity_patterns = [ 
    path('electricity_printable_A_question/', d_electricity_views.random_printable_A_question, name='random_printable_A_question'),
    path('electricity_printable_B_question/', d_electricity_views.random_printable_B_question, name='random_printable_B_question'),
    path('electricity_printable_A_section/', d_electricity_views.random_printable_A_section, name='random_printable_A_section'),
    path('electricity_printable_B_section/', d_electricity_views.random_printable_B_section, name='random_printable_B_section'),
    path('electricity_interactive_A_question/', d_electricity_views.random_interactive_A_question, name='random_interactive_A_question'),
    path('electricity_interactive_B_question/', d_electricity_views.random_interactive_B_question, name='random_interactive_B_question'),
]+[ eval(f"path('{module}/', d_electricity_views.{module}, name='{module}')") for module in d_electricity_views.modulesList()]

e1_further_mechanics_patterns = [ 
    path('further_mechanics_printable_A_question/', e1_further_mechanics_views.random_printable_A_question, name='random_printable_A_question'),
    path('further_mechanics_printable_B_question/', e1_further_mechanics_views.random_printable_B_question, name='random_printable_B_question'),
    path('further_mechanics_printable_A_section/', e1_further_mechanics_views.random_printable_A_section, name='random_printable_A_section'),
    path('further_mechanics_printable_B_section/', e1_further_mechanics_views.random_printable_B_section, name='random_printable_B_section'),
    path('further_mechanics_interactive_A_question/', e1_further_mechanics_views.random_interactive_A_question, name='random_interactive_A_question'),
    path('further_mechanics_interactive_B_question/', e1_further_mechanics_views.random_interactive_B_question, name='random_interactive_B_question'),
]+[ eval(f"path('{module}/', e1_further_mechanics_views.{module}, name='{module}')") for module in e1_further_mechanics_views.modulesList()]

urlpatterns = [
    path('', views.home, name="physics-home"),

    path('particles_and_radiation/',  a_particles_and_radiation_views.particles_and_radiation_home, name="matter-and-radiation-exam-questions"),
    path('particles_and_radiation/', include(a_particles_and_radiation_patterns)),

    path('electricity/', d_electricity_views.electricity_home, name="electricity-exam-questions"),
    path('electricity/', include(d_electricity_patterns)),

    path('further_mechanics/', e1_further_mechanics_views.further_mechanics_home, name = "e1_further_mechanics"),
    path('further_mechanics/', include(e1_further_mechanics_patterns)),

]



