from django.urls import path, include
from . import views
from sql.a_basics import a_basics_views, a_basics_logic

a_basics_patterns = [ eval(f"path('{module}/', a_basics_views.{module}, name='{module}')") for module in a_basics_logic.modulesList() ]

urlpatterns = [
    path('', views.home, name="sql-home"),

    path('basics/', views.home_a_basics, name="sql_basics"),
    path('basics/', include(a_basics_patterns)),

    path('work_on/', views.work_on, name="work_on")
    ]



