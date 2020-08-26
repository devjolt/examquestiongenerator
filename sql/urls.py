from django.urls import path, include
from . import views
from sql.a_basics import a_basics_views

a_basics_patterns = [
   path('test/', a_basics_views.test, name="test"),
   path('a1qa_what_is_sql/', a_basics_views.a1qa_what_is_sql, name='a1qa_what_is_sql'), 
   path("a1qb_what_sql_does/", a_basics_views.a1qb_what_sql_does, name = "a1qb_what_sql_does"),
   path("a1qc_database_brands/", a_basics_views.a1qc_database_brands, name = "a1qc_database_brands"),
   path("a1qd_database_entities/", a_basics_views.a1qd_database_entities, name = "a1qd_database_entities"),
   path("a2qa_statements/", a_basics_views.a2qa_statements, name = "a2qa_statements"),
   path("a2qb_commands_starting_statements/", a_basics_views.a2qb_commands_starting_statements, name = "a2qb_commands_starting_statements"),
   path("a2qc_create_statements/", a_basics_views.a2qc_create_statements, name = "a2qc_create_statements"),
   ]

urlpatterns = [
    path('', views.home, name="sql-home"),

    path('basics/', views.home_a_basics, name="sql_basics"),
    path('basics/', include(a_basics_patterns)),

    path('work_on/', views.work_on, name="work_on")
    ]



