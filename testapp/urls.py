from django.contrib import admin
from django.urls import path, include
from .physics_dev import dev_questions_views
from . import views 

physics_dev_patterns = [
    path('type_dev/', dev_questions_views.type_dev, name='type_dev'),
    
] + [ eval(f"path('{module}/', dev_questions_views.{module}, name='{module}')") for module in dev_questions_views.modulesList()]

urlpatterns = [
    path('', views.home, name="test-home"),
    path('physics_dev/', dev_questions_views.auto_list_page, name='auto_list_page'),
    path('physics_dev/', include(physics_dev_patterns)),
    path('random_printable_A_question/', dev_questions_views.random_printable_A_question, name='random_printable_A_question'),
    path('random_printable_B_question/', dev_questions_views.random_printable_B_question, name='random_printable_B_question'),
    path('random_printable_A_section/', dev_questions_views.random_printable_A_section, name='random_printable_A_section'),
    path('random_printable_B_section/', dev_questions_views.random_printable_B_section, name='random_printable_B_section'),
    path('random_interactive_A_question/', dev_questions_views.random_interactive_A_question, name='random_interactive_A_question'),
    path('random_interactive_B_question/', dev_questions_views.random_interactive_B_question, name='random_interactive_B_question'),

]