from django.shortcuts import render
from random import randint
from . import e_geometry_and_measure_logic
import sys
from gcsemaths import gcsemaths_helper_functions as phf

def view_builder(name):
    passed = eval(f"e_geometry_and_measure_logic.{name}()")
    return phf.allArguments2(passed)

currentFuncName = lambda n=0: sys._getframe(n + 1).f_code.co_name # allows previousNext functionality to work by getting current function's name

#selects a random selection module (as below) at random from e_geometry_and_measure_logic.py 
def eselect_random(request):
    passed = e_geometry_and_measure_logic.eselect_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

def egeometry_basics_random(request):
    passed = e_geometry_and_measure_logic.egeometry_basics_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

def egeometry_parallel_random(request):
    passed = e_geometry_and_measure_logic.egeometry_basics_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

def egeometry_problems_random(request):
    passed = e_geometry_and_measure_logic.egeometry_basics_random()
    return render(request, "questionAnswerButtons2.html", phf.allArguments2(passed))

'''
def view_builder(name):
    passed = eval(f"e_geometry_and_measure_logic.{name}()")
    return phf.allArguments2(passed)

def eselect_random(request):
    passed = e_geometry_and_measure_logic.eselect_random()
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
'''

def ea1_angles_in_triangle_no_diagram(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea1_angles_in_triangle_diagram(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea1_angles_on_straight_line_diagram(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea1_angles_in_quadrilateral_diagram(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea1_angles_in_isosceles_triangle_diagram(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea1_isosceles_triangle_pair_known_diagram(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea1_isosceles_triangle_single_known_diagram(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea2_angles_around_parallel_lines(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea2_alternate_angles_parallel_lines(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea2_allied_angles_parallel_lines(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea2_corresponding_angles_parallel_lines(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea2_alternate_allied_corresponding(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea3_problem2(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea3_problem3(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea3_problem4(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea3_problem5(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea3_problem6(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea3_problem7(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea3_problem8(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea3_problem9(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ea3_problem10(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb11_polygon_attributes(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb12_polygon_intext_angles(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb13_regular_polygon_attributes(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb14_regular_polygon_exterior_angles(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb25_triangle_attributes(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb26_quadrilateral_attributes(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb31_circle_radius_tangent(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb32_circle_two_radi_isosceles(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb33_perpendicular_bisector_chord(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb34_angle_centre_twice_circumference(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb35_angle_semi_circle(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb36_angle_same_segment_equal(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb37_opposite_cyclic_quadrilateral(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb38_tangents_point_same_length(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb39_alternate_segment_theorem(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb3_circle_problem1(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def eb3_circle_problem2(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec11_congruent_similar(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec12_congruent_similar_diagrams(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec13_congruent_triangle_rules(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec14_congruent_triangle_rules_diagrams(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec21_similar_congruent(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec22_similar_congruent_diagrams(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec23_similar_triangle_rules(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec25_all_angles_match_up(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec26_all_sides_match_up(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec27_two_sides_one_angle(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec28_all_angles_match_up_proof(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec29_all_sides_match_up_proof(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec210_two_sides_one_angle_proof(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec1_prove_congruency1(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec1_prove_congruency2(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec2_prove_similarity1(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec2_use_similarity1(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ec2_use_similarity2(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed10_area_triangle_quadrilateral_formulas11(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed11_area_triangles13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
    
def ed12_area_parallelogram13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))        

def ed13_area_trapezium23(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed14_area_triangles23(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed15_area_parallelogram24(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed16_area_trapezium24(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed17_area_trapezium_problem25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed18_area_triangle_rectangle24(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed20_circumference_radius_and_diameter_12(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
    
def ed21_formulas_for_area_circumference_arcs_sectors_and_segments13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
    
def ed22_area_of_a_circle_23(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed23_circumference_of_a_circle_23(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed24_area_and_circumference_23(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed25_arcs_and_sectors_12(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed26_segments_12(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed27_segments_arcs_and_sectors13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed28_area_of_a_sector26(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed29_length_of_arc26(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed210_area_of_segments37(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed211_area_of_pacman26(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ed212_shape_problem26(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ee10_terminology13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee11_count_vertices_edges_faces13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee12_surface_area14(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee13_surface_area_formulas14(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee14_surface_area_of_a_sphere25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee15_surface_area_of_a_cylinder25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee16_surface_area_of_a_cone25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee17_use_surface_area_formula_to_find_an_unknown_value_in_a_sphere25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee18_use_surface_area_formula_to_find_an_unknown_value_in_a_cyinder25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee19_use_surface_area_formula_to_find_an_unknown_value_in_a_cone25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee110_problem_hemisphere36(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))

def ee20_identify_the_3D_shape13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee21_definitions_of_3D_shapes13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee22_volume_formulas13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee23_volume_of_a_prism_with_cross_sectional_area_known13(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee24_volume_of_a_sphere_with_radius_known25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee25_volume_of_a_pyramid_with_base_and_height_known25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee25_volume_of_a_cone_with_radius_and_height_known25(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee26_volume_of_a_frustrum_with_volume_of_original_cone_known46(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
def ee27_volume_of_a_hemisphere_with_radius_known35(request):
    return render(request, "questionAnswerButtons2.html", view_builder(currentFuncName()))
