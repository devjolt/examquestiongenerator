from django.urls import path, include
from . import views
from pcep.a_basics import a_basics_views, a_basics_logic
'''
path('section/', e_further_mechanics_thermal_physics_views.section_generator, name="section generator"),
    path('random/', e_further_mechanics_thermal_physics_views.select_random, name="random"),
    path("e1_uniform_circular_motion_random/", e_further_mechanics_thermal_physics_views.e1_uniform_circular_motion_random, name = "e1_uniform_circular_motion_random"),

'''
basics_patterns = [
    path("a1qa_test/", a_basics_views.e1qa_test, name = "e1qa_test"),
    path("a1qa_interpreting_the_interpreter/", a_basics_views.a1qa_interpreting_the_interpreter, name = "a1qa_interpreting_the_interpreter"),
    path("a1qb_compilation_and_the_compiler/", a_basics_views.a1qb_compilation_and_the_compiler, name = "a1qb_compilation_and_the_compiler"),
    path("a1qc_machine_higher_level_natural_languages/", a_basics_views.a1qc_machine_higher_level_natural_languages, name = "a1qc_machine_higher_level_natural_languages"),
    path("a1qd_language_elements/", a_basics_views.a1qd_language_elements, name = "a1qd_language_elements"),
    path("a1qe_python/", a_basics_views.a1qe_python, name = "a1qe_python"),
    path("a1qf_python_keywords/", a_basics_views.a1qf_python_keywords, name = "a1qf_python_keywords"),
    path("a1qg_indentation_and_spacing/", a_basics_views.a1qg_indentation_and_spacing, name = "a1qg_indentation_and_spacing"),

]

urlpatterns = [
    path('', views.home, name="pcep-home"),

    path('a_basics/', views.home_basics, name="pcep_basics"),
    path('a_basics/', include(basics_patterns)),
]