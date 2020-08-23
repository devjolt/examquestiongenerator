from django.urls import path, include
from . import views
from sql.a_basics import a_basics_views

a_basics_patterns = [
   path('test/', a_basics_views.test, name="test"),
   path('a1qa_what_is_sql/', a_basics_views.a1qa_what_is_sql, name='a1qa_what_is_sql'), 
   ]

urlpatterns = [
    path('', views.home, name="sql-home"),

    path('basics/', views.home_a_basics, name="sql_basics"),
    path('basics/', include(a_basics_patterns)),
    ]



