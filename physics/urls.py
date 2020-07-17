from django.urls import path, include
from . import views
from physics.a_particles_and_radiation import matterAndRadiation
from physics.d_electricity import daa_currentAndCharge, dab_pd_and_power, dac_resistance, dad_components_and_their_characteristics, dba_circuit_rules, dbb_more_about_resistance, dbc_emf_and_internal_resistance
from physics.e_further_mechanics_thermal_physics import e_random_further_mechanics_thermal_physics, e_further_mechanics_thermal_physics_views

from physics.e_further_mechanics_thermal_physics import e_further_mechanics_thermal_physics_logic

matter_and_radiation_patterns = [

    path('nucleus/', matterAndRadiation.nucleus, name="nucleus"),
    path('namepartoftheatom/', matterAndRadiation.namepartoftheatom, name="namepartoftheatom"),
    path('ionised/', matterAndRadiation.ionised, name="ionised"),
]

electricity_patterns = [
    path('chargeCurrentTime/', daa_currentAndCharge.chargeCurrentTime, name="chargeCurrentTime"),
    path('electronsCurrentTime/', daa_currentAndCharge.electronsCurrentTime, name="electronsCurrentTime"),
    path('electronBeamExperiment/', daa_currentAndCharge.electronBeamExperiment, name="electronBeamExperiment"),
    path('rechargableBattery/', daa_currentAndCharge.rechargableBattery, name="rechargableBattery"),
    path('workPdCurrent/', daa_currentAndCharge.workPdCurrent, name="workPdCurrent"),

    path('work_pd_current/', dab_pd_and_power.work_pd_current, name="work_pd_current"),
    path('power_pd_current/', dab_pd_and_power.power_pd_current, name="power_pd_current"),
    path('pd_charge_energy_power_time/', dab_pd_and_power.pd_charge_energy_power_time, name="pd_charge_energy_power_time"),

    path('resistance_pd_current/', dac_resistance.resistance_pd_current, name="resistance_pd_current"),
    path('resistivity_uniform_wire/', dac_resistance.resistivity_uniform_wire, name="resistivity_uniform_wire"),
    path('resistivity_rectangular_wire/', dac_resistance.resistivity_rectangular_wire, name="resistivity_rectangular_wire"),
    path('two_part_resistivity/', dac_resistance.two_part_resistivity, name="two_part_resistivity"),

    path('temperature_of_a_fillament/', dad_components_and_their_characteristics.temperature_of_a_fillament, name="temperature_of_a_fillament"),
    path('temperature_of_a_thermistor/', dad_components_and_their_characteristics.temperature_of_a_thermistor, name="temperature_of_a_thermistor"),
    path('variable_temperature_resistance/', dad_components_and_their_characteristics.variable_temperature_resistance, name="variable_temperature_resistance"),

    path('two_components_parallel/', dba_circuit_rules.two_components_parallel, name="two_components_parallel"),
    path('two_components_series/', dba_circuit_rules.two_components_series, name="two_components_series"),
    path('two_components_series2/', dba_circuit_rules.two_components_series2, name="two_components_series2"),

    path('seriesParallelChoice/', dbb_more_about_resistance.seriesParallelChoice, name="seriesParallelChoice"),
    path('oneSeriesTwoParallel/', dbb_more_about_resistance.oneSeriesTwoParallel, name="oneSeriesTwoParallel"),
    path('oneSeriesTwoParallelSecond/', dbb_more_about_resistance.oneSeriesTwoParallelSecond, name="oneSeriesTwoParallelSecond"),
    path('element/', dbb_more_about_resistance.element, name="element"),

    path('emf_internal_reistance_random/', dbc_emf_and_internal_resistance.select_random, name="random_emf_internal_resistance_question" )
]

further_mechanics_and_thermal_physics_patterns = [
    path('section/', e_further_mechanics_thermal_physics_views.section_generator, name="section generator"),

    path('random/', e_further_mechanics_thermal_physics_views.select_random, name="random"),
    path("e1_uniform_circular_motion_random/", e_further_mechanics_thermal_physics_views.e1_uniform_circular_motion_random, name = "e1_uniform_circular_motion_random"),
    path("e2_centripetal_acceleration_random/", e_further_mechanics_thermal_physics_views.e2_centripetal_acceleration_random, name = "e2_centripetal_acceleration_random"),
    path("e3_on_the_road_random/", e_further_mechanics_thermal_physics_views.e3_on_the_road_random, name = "e3_on_the_road_random"),
    path("e4_at_the_fairground_random/", e_further_mechanics_thermal_physics_views.e4_at_the_fairground_random, name = "e4_at_the_fairground_random"),
    
    path("e1qa_minute_hand_of_clock/", e_further_mechanics_thermal_physics_views.e1qa_minute_hand_of_clock, name = "e1qa_minute_hand_of_clock"),
    path("e1qb_time_pweriod_angle_electric_motor/", e_further_mechanics_thermal_physics_views.e1qb_time_pweriod_angle_electric_motor, name = "e1qb_time_pweriod_angle_electric_motor"),
    path("e1qc_planet_rotation/", e_further_mechanics_thermal_physics_views.e1qc_planet_rotation, name = "e1qc_planet_rotation"),
    path("e1qd_satalite_orbit/", e_further_mechanics_thermal_physics_views.e1qd_satalite_orbit, name = "e1qd_satalite_orbit"), 
    
    path("e2qa_the_wheel_of/", e_further_mechanics_thermal_physics_views.e2qa_the_wheel_of, name = "e2qa_the_wheel_of"),
    path("e2qb_object_circular_path/", e_further_mechanics_thermal_physics_views.e2qb_object_circular_path, name = "e2qb_object_circular_path"),
    path("e2qc_earth_around_sun/", e_further_mechanics_thermal_physics_views.e2qc_earth_around_sun, name = "e2qc_earth_around_sun"),
    path("e2qd_hammer_thrower/", e_further_mechanics_thermal_physics_views.e2qd_hammer_thrower, name = "e2qd_hammer_thrower"),
    
    path("e3qa_bridge/", e_further_mechanics_thermal_physics_views.e3qa_bridge, name = "e3qa_bridge"),
    path("e3qb_roundabout/", e_further_mechanics_thermal_physics_views.e3qb_roundabout, name = "e3qb_roundabout"),
    path("e3qc_racingtrack/", e_further_mechanics_thermal_physics_views.e3qc_racingtrack, name = "e3qc_racingtrack"),
    
    path("e4qa_rollercoaster/", e_further_mechanics_thermal_physics_views.e4qa_rollercoaster, name = "e4qa_rollercoaster"),
    path("e4qb_swing/", e_further_mechanics_thermal_physics_views.e4qb_swing, name = "e4qb_swing"),
    path("e4qc_wheel/", e_further_mechanics_thermal_physics_views.e4qc_wheel, name = "e4qc_wheel")
]

urlpatterns = [
    path('', views.home, name="physics-home"),

    path('electricity/', views.home_d_electricity, name="electricity-exam-questions"),
    path('electricity/', include(electricity_patterns)),

    path('matter_and_radiation/', views.home_a_matter_and_radiation, name="matter-and-radiation-exam-questions"),
    path('matter_and_radiation/', include(matter_and_radiation_patterns)),

    path('further_mechanics_and_thermal_physics/', views.home_e_further_mechanics_and_thermal_physics, name = "further_mechanics_and_thermal_physics"),
    path('further_mechanics_and_thermal_physics/', include(further_mechanics_and_thermal_physics_patterns)),
]



