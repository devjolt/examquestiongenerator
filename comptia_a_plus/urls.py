from django.contrib import admin
from django.urls import path, include
from . import views
from comptia_a_plus.a_core_1_220_1001 import aa_mobile_devices_views, ab_networking_technology_views, ac_hardware_views, ad_virtualisation_cloud_computing_views, ae_troubleshooting_views

aa_mobile_devices = [ eval(f"path('{module}/', aa_mobile_devices_views.{module}, name='{module}')") for module in aa_mobile_devices_views.modulesList()]
ab_networking_technology = [ eval(f"path('{module}/', ab_networking_technology_views.{module}, name='{module}')") for module in ab_networking_technology_views.modulesList()]
ac_hardware = [ eval(f"path('{module}/', ac_hardware_views.{module}, name='{module}')") for module in ac_hardware_views.modulesList()]
ad_virtualisation_cloud_computing = [ eval(f"path('{module}/', ad_virtualisation_cloud_computing_views.{module}, name='{module}')") for module in ad_virtualisation_cloud_computing_views.modulesList()]
ae_troubleshooting = [ eval(f"path('{module}/', ae_troubleshooting_views.{module}, name='{module}')") for module in ae_troubleshooting_views.modulesList()]

core_1_220_1001_patterns = [
    path('random/', views.core_1_220_1001_random, name = 'core_1_220_1001_random'),
    path('test/', aa_mobile_devices_views.test, name='test'),
    #path('test_drag/', aa_mobile_devices_views.test_drag, name='test_drag'),
    #path('test_double_drag/', aa_mobile_devices_views.test_double_drag, name='test_double_drag')
] + aa_mobile_devices + ab_networking_technology + ac_hardware + ae_troubleshooting + ad_virtualisation_cloud_computing

urlpatterns = [
    path('', views.home, name="a_plus_home"),

    path('core_1_220_1001/', views.core_1_220_1001, name="220_1001"),
    path('core_1_220_1001/', include(core_1_220_1001_patterns)),

    path('core_2_220_1002/', views.core_2_220_1002, name="220_1002"),
] 