from django.contrib import admin
from django.urls import path, include
from . import views
from gcsemaths.exam_questions import exam_non_calc
from gcsemaths.a_number import aa_ordering_and_comparative, ab_ops_with_int_frac_dec, number_random
from gcsemaths.b_algebra import algebra_random, algebra_views
from gcsemaths.e_geometry_and_measure import e_geometry_and_measure_views



number_patterns = [

    path('ordering_numbers/', aa_ordering_and_comparative.ordering_numbers, name="ordering_numbers"),
    path('ordering_decimals/', aa_ordering_and_comparative.ordering_decimals, name="ordering_decimals"),
    path('ordering_fractions/', aa_ordering_and_comparative.ordering_fractions, name="ordering_fractions"),
    path('ordering_fractions_and_decimals/', aa_ordering_and_comparative.ordering_fractions_and_decimals, name="ordering_fractions_and_decimals"),

    path('comparative_operators_with_integers/', aa_ordering_and_comparative.comparative_operators_with_integers, name="comparative_operators_with_integers"),
    path('comparative_operators_with_fractions/', aa_ordering_and_comparative.comparative_operators_with_fractions, name="comparative_operators_with_fractions"),
    path('comparative_operators_with_fractions_and_decimals/', aa_ordering_and_comparative.comparative_operators_with_fractions_and_decimals, name="comparative_operators_with_fractions_and_decimals")

] + [ eval(f"path('{module}/', ab_ops_with_int_frac_dec.{module}, name='{module}')") for module in ab_ops_with_int_frac_dec.modulesList() ]

algebra_patterns = [
    path("algebra_basics_random/", algebra_views.algebra_basics_random, name = "algebra_basics_random"),
    path("algebra_brackets_random/", algebra_views.algebra_brackets_random, name = "algebra_brackets_random"),
    path("algebra_powers_random/", algebra_views.algebra_powers_random, name = "algebra_powers_random"),
    path("algebra_surds_random/", algebra_views.algebra_surds_random, name = "algebra_surds_random"),
    path("algebra_solve_random/", algebra_views.algebra_solve_random, name = "algebra_solve_random"),
    path("algebra_factorising_random/", algebra_views.algebra_factorising_random, name="algebra_factorising_random"),
    path("basics_negative_numbers/", algebra_views.basics_negative_numbers, name = "basics_negative_numbers"),
    path("basics_multiplying_letters/", algebra_views.basics_multiplying_letters, name = "basics_multiplying_letters"),
    path("basics_collecting_like_terms/", algebra_views.basics_collecting_like_terms, name = "basics_collecting_like_terms"),
    path("expand_brackets_three_letters/", algebra_views.expand_brackets_three_letters, name = "expand_brackets_three_letters"),
    path("expand_brackets_numbers_letters/", algebra_views.expand_brackets_numbers_letters, name = "expand_brackets_numbers_letters"),
    path("expand_brackets_double/", algebra_views.expand_brackets_double, name = "expand_brackets_double"),
    path("power_of_zero/", algebra_views.power_of_zero, name = "power_of_zero"),
    path("power_of_one/", algebra_views.power_of_one, name = "power_of_one"),
    path("power_one_to_the_power_of/", algebra_views.power_one_to_the_power_of, name = "power_one_to_the_power_of"),
    path("power_multiplying_powers/", algebra_views.power_multiplying_powers, name = "power_multiplying_powers"),
    path("power_dividing/", algebra_views.power_dividing, name = "power_dividing"),
    path("power_raising_to/", algebra_views.power_raising_to, name = "power_raising_to"),
    path("power_raising_two_powers_to/", algebra_views.power_raising_two_powers_to, name = "power_raising_two_powers_to"),
    path("power_with_fractions/", algebra_views.power_with_fractions, name = "power_with_fractions"),
    path("power_with_fractions_letters/", algebra_views.power_with_fractions_letters, name = "power_with_fractions_letters"),
    path("power_negative/", algebra_views.power_negative, name = "power_negative"),
    path("power_negative_letters/", algebra_views.power_negative_letters, name = "power_negative_letters"),
    path("power_fractional/", algebra_views.power_fractional, name = "power_fractional"),
    path("surd_rule_17/", algebra_views.surd_rule_17, name = "surd_rule_17"),
    path("surd_rule_3a7/", algebra_views.surd_rule_3a7, name = "surd_rule_3a7"),
    path("surd_rule_3b7/", algebra_views.surd_rule_3b7, name = "surd_rule_3b7"),
    path("surd_rule_3c7/", algebra_views.surd_rule_3c7, name = "surd_rule_3c7"),
    path("surd_rule_4a7/", algebra_views.surd_rule_4a7, name = "surd_rule_4a7"),
    path("surd_rule_4b7/", algebra_views.surd_rule_4b7, name = "surd_rule_4b7"),
    path("surd_rule_5a7/", algebra_views.surd_rule_5a7, name = "surd_rule_5a7"),
    path("surd_rule_5b7/", algebra_views.surd_rule_5b7, name = "surd_rule_5b7"),
    path("surd_rule_6a7/", algebra_views.surd_rule_6a7, name = "surd_rule_6a7"),
    path("surd_rule_6b7/", algebra_views.surd_rule_6b7, name = "surd_rule_6b7"),

    path("surd_simplify_addition_a8/", algebra_views.surd_simplify_addition_a8, name = "surd_simplify_addition_a8"),
    path("surd_simplify_addition_b8/", algebra_views.surd_simplify_addition_b8, name = "surd_simplify_addition_b8"),
    path("surd_simplify_addition_c8/", algebra_views.surd_simplify_addition_c8, name = "surd_simplify_addition_c8"),
    path("surd_simplify_area8/", algebra_views.surd_simplify_area8, name = "surd_simplify_area8"),
    path("surd_in_the_form9/", algebra_views.surd_in_the_form9, name = "surd_in_the_form9"),
    path("factorising_two_letters/", algebra_views.factorising_two_letters, name = "factorising_two_letters"),
    path("factorising_more_letters/", algebra_views.factorising_more_letters, name = "factorising_more_letters"),
    path("solve_divide/", algebra_views.solve_divide, name = "solve_divide"),
    path("solve_collectint_divide/", algebra_views.solve_collectint_divide, name = "solve_collectint_divide"),
    path("solve_collectx_collectint_divide/", algebra_views.solve_collectx_collectint_divide, name = "solve_collectx_collectint_divide"),
    path("solve_collectx_collectint_divide_brackets/", algebra_views.solve_collectx_collectint_divide_brackets, name = "solve_collectx_collectint_divide_brackets"),
    path("solve_collectx_collectint_divide_brackets_double/", algebra_views.solve_collectx_collectint_divide_brackets_double, name = "solve_collectx_collectint_divide_brackets_double"),
    path("solve_posneg_collectx_collectint_divide_brackets/", algebra_views.solve_posneg_collectx_collectint_divide_brackets, name = "solve_posneg_collectx_collectint_divide_brackets"),
    path("solve_posneg_collectx_collectint_divide_brackets_fractions/", algebra_views.solve_posneg_collectx_collectint_divide_brackets_fractions, name = "solve_posneg_collectx_collectint_divide_brackets_fractions"),
    path("solve_posneg_collectx_collectint_divide_brackets_first_fraction/", algebra_views.solve_posneg_collectx_collectint_divide_brackets_first_fraction, name = "solve_posneg_collectx_collectint_divide_brackets_first_fraction"),
    path("solve_posneg_collectx_collectint_divide_brackets_second_fraction/", algebra_views.solve_posneg_collectx_collectint_divide_brackets_second_fraction, name = "solve_posneg_collectx_collectint_divide_brackets_second_fraction")
    
]


geometry_patterns = [
    path("eselect_random/", e_geometry_and_measure_views.eselect_random, name = "eselect_random"),
    path("egeometry_basics_random/", e_geometry_and_measure_views.egeometry_basics_random, name = "egeometry_basics_random"),
    path("egeometry_parallel_random/", e_geometry_and_measure_views.egeometry_parallel_random, name = "egeometry_parallel_random"),
    path("ea1_angles_in_triangle_no_diagram/", e_geometry_and_measure_views.ea1_angles_in_triangle_no_diagram, name = "ea1_angles_in_triangle_no_diagram"),
    path("ea1_angles_in_triangle_diagram/", e_geometry_and_measure_views.ea1_angles_in_triangle_diagram, name = "ea1_angles_in_triangle_diagram"),
    path("ea1_angles_on_straight_line_diagram/", e_geometry_and_measure_views.ea1_angles_on_straight_line_diagram, name = "ea1_angles_on_straight_line_diagram"),
    path("ea1_angles_in_quadrilateral_diagram/", e_geometry_and_measure_views.ea1_angles_in_quadrilateral_diagram, name = "ea1_angles_in_quadrilateral_diagram"),
    path("ea1_angles_in_isosceles_triangle_diagram/", e_geometry_and_measure_views.ea1_angles_in_isosceles_triangle_diagram, name = "ea1_angles_in_isosceles_triangle_diagram"),
    path("ea1_isosceles_triangle_pair_known_diagram/", e_geometry_and_measure_views.ea1_isosceles_triangle_pair_known_diagram, name = "ea1_isosceles_triangle_pair_known_diagram"),
    path("ea1_isosceles_triangle_single_known_diagram/", e_geometry_and_measure_views.ea1_isosceles_triangle_single_known_diagram, name = "ea1_isosceles_triangle_single_known_diagram"),
    
    path("ea2_angles_around_parallel_lines/", e_geometry_and_measure_views.ea2_angles_around_parallel_lines, name = "ea2_angles_around_parallel_lines"),
    path("ea2_alternate_angles_parallel_lines/", e_geometry_and_measure_views.ea2_alternate_angles_parallel_lines, name = "ea2_alternate_angles_parallel_lines"),
    path("ea2_allied_angles_parallel_lines/", e_geometry_and_measure_views.ea2_allied_angles_parallel_lines, name = "ea2_allied_angles_parallel_lines"),
    path("ea2_corresponding_angles_parallel_lines/", e_geometry_and_measure_views.ea2_corresponding_angles_parallel_lines, name = "ea2_corresponding_angles_parallel_lines"),
    path("ea2_alternate_allied_corresponding/", e_geometry_and_measure_views.ea2_alternate_allied_corresponding, name = "ea2_alternate_allied_corresponding"),

    path("ea3_problem2/", e_geometry_and_measure_views.ea3_problem2, name = "ea3_problem2"),
    path("ea3_problem3/", e_geometry_and_measure_views.ea3_problem3, name = "ea3_problem3"),
    path("ea3_problem4/", e_geometry_and_measure_views.ea3_problem4, name = "ea3_problem4"),
    path("ea3_problem5/", e_geometry_and_measure_views.ea3_problem5, name = "ea3_problem5"),
    path("ea3_problem6/", e_geometry_and_measure_views.ea3_problem6, name = "ea3_problem6"),
    path("ea3_problem7/", e_geometry_and_measure_views.ea3_problem7, name = "ea3_problem7"),
    path("ea3_problem8/", e_geometry_and_measure_views.ea3_problem8, name = "ea3_problem8"),
    path("ea3_problem9/", e_geometry_and_measure_views.ea3_problem9, name = "ea3_problem9"),
    path("ea3_problem10/", e_geometry_and_measure_views.ea3_problem10, name = "ea3_problem10"),

    path("eb11_polygon_attributes/", e_geometry_and_measure_views.eb11_polygon_attributes, name = "eb11_polygon_attributes"),
    path("eb12_polygon_intext_angles/", e_geometry_and_measure_views.eb12_polygon_intext_angles, name = "eb12_polygon_intext_angles"),
    path("eb13_regular_polygon_attributes/", e_geometry_and_measure_views.eb13_regular_polygon_attributes, name = "eb13_regular_polygon_attributes"),
    path("eb14_regular_polygon_exterior_angles/", e_geometry_and_measure_views.eb14_regular_polygon_exterior_angles, name = "eb14_regular_polygon_exterior_angles"),
    path("eb25_triangle_attributes/", e_geometry_and_measure_views.eb25_triangle_attributes, name = "eb25_triangle_attributes"),
    path("eb26_quadrilateral_attributes/", e_geometry_and_measure_views.eb26_quadrilateral_attributes, name = "eb26_quadrilateral_attributes"),
    
    path("eb31_circle_radius_tangent/", e_geometry_and_measure_views.eb31_circle_radius_tangent, name = "eb31_circle_radius_tangent"),
    path("eb32_circle_two_radi_isosceles/", e_geometry_and_measure_views.eb32_circle_two_radi_isosceles, name = "eb32_circle_two_radi_isosceles"),
    path("eb33_perpendicular_bisector_chord/", e_geometry_and_measure_views.eb33_perpendicular_bisector_chord, name = "eb33_perpendicular_bisector_chord"),
    path("eb34_angle_centre_twice_circumference/", e_geometry_and_measure_views.eb34_angle_centre_twice_circumference, name = "eb34_angle_centre_twice_circumference"),
    path("eb35_angle_semi_circle/", e_geometry_and_measure_views.eb35_angle_semi_circle, name = "eb35_angle_semi_circle"),
    path("eb36_angle_same_segment_equal/", e_geometry_and_measure_views.eb36_angle_same_segment_equal, name = "eb36_angle_same_segment_equal"),
    path("eb37_opposite_cyclic_quadrilateral/", e_geometry_and_measure_views.eb37_opposite_cyclic_quadrilateral, name = "eb37_opposite_cyclic_quadrilateral"),
    path("eb38_tangents_point_same_length/", e_geometry_and_measure_views.eb38_tangents_point_same_length, name = "eb38_tangents_point_same_length"),
    path("eb39_alternate_segment_theorem/", e_geometry_and_measure_views.eb39_alternate_segment_theorem, name = "eb39_alternate_segment_theorem"),
    path("eb3_circle_problem1/", e_geometry_and_measure_views.eb3_circle_problem1, name = "eb3_circle_problem1"),
    path("eb3_circle_problem2/", e_geometry_and_measure_views.eb3_circle_problem2, name = "eb3_circle_problem2"),

    path("ec11_congruent_similar/", e_geometry_and_measure_views.ec11_congruent_similar, name = "ec11_congruent_similar"),
    path("ec12_congruent_similar_diagrams/", e_geometry_and_measure_views.ec12_congruent_similar_diagrams, name = "ec12_congruent_similar_diagrams"),
    path("ec13_congruent_triangle_rules/", e_geometry_and_measure_views.ec13_congruent_triangle_rules, name = "ec13_congruent_triangle_rules"),
    path("ec14_congruent_triangle_rules_diagrams/", e_geometry_and_measure_views.ec14_congruent_triangle_rules_diagrams, name = "ec14_congruent_triangle_rules_diagrams"),

    path("ec21_similar_congruent/", e_geometry_and_measure_views.ec21_similar_congruent, name = "ec21_similar_congruent"),
    path("ec22_similar_congruent_diagrams/", e_geometry_and_measure_views.ec22_similar_congruent_diagrams, name = "ec22_similar_congruent_diagrams"),
    path("ec23_similar_triangle_rules/", e_geometry_and_measure_views.ec23_similar_triangle_rules, name = "ec23_similar_triangle_rules"),
    path("ec25_all_angles_match_up/", e_geometry_and_measure_views.ec25_all_angles_match_up, name = "ec25_all_angles_match_up"),
    path("ec26_all_sides_match_up/", e_geometry_and_measure_views.ec26_all_sides_match_up, name = "ec26_all_sides_match_up"),
    path("ec27_two_sides_one_angle/", e_geometry_and_measure_views.ec27_two_sides_one_angle, name = "ec27_two_sides_one_angle"),
    path("ec28_all_angles_match_up_proof/", e_geometry_and_measure_views.ec28_all_angles_match_up_proof, name = "ec28_all_angles_match_up_proof"),
    path("ec29_all_sides_match_up_proof/", e_geometry_and_measure_views.ec29_all_sides_match_up_proof, name = "ec29_all_sides_match_up_proof"),
    path("ec210_two_sides_one_angle_proof/", e_geometry_and_measure_views.ec210_two_sides_one_angle_proof, name = "ec210_two_sides_one_angle_proof"),

    path("ec1_prove_congruency1/", e_geometry_and_measure_views.ec1_prove_congruency1, name = "ec1_prove_congruency1"),
    path("ec1_prove_congruency2/", e_geometry_and_measure_views.ec1_prove_congruency2, name = "ec1_prove_congruency2"),
    path("ec2_prove_similarity1/", e_geometry_and_measure_views.ec2_prove_similarity1, name = "ec2_prove_similarity1"),
    path("ec2_use_similarity1/", e_geometry_and_measure_views.ec2_use_similarity1, name = "ec2_use_similarity1"),
    path("ec2_use_similarity2/", e_geometry_and_measure_views.ec2_use_similarity2, name = "ec2_use_similarity2"),

    path("ed10_area_triangle_quadrilateral_formulas11/", e_geometry_and_measure_views.ed10_area_triangle_quadrilateral_formulas11, name = "ed10_area_triangle_quadrilateral_formulas11"),
    path("ed11_area_triangles13/", e_geometry_and_measure_views.ed11_area_triangles13, name = "ed11_area_triangles13"),
    path("ed12_area_parallelogram13/", e_geometry_and_measure_views.ed12_area_parallelogram13, name = "ed12_area_parallelogram13"),
    path("ed13_area_trapezium23/", e_geometry_and_measure_views.ed13_area_trapezium23, name = "ed13_area_trapezium23"),
    path("ed14_area_triangles23/", e_geometry_and_measure_views.ed14_area_triangles23, name = "ed14_area_triangles23"),
    path("ed15_area_parallelogram24/", e_geometry_and_measure_views.ed15_area_parallelogram24, name = "ed15_area_parallelogram24"),
    path("ed16_area_trapezium24/", e_geometry_and_measure_views.ed16_area_trapezium24, name = "ed16_area_trapezium24"),
    path("ed17_area_trapezium_problem25/", e_geometry_and_measure_views.ed17_area_trapezium_problem25, name = "ed17_area_trapezium_problem25"),
    path("ed18_area_triangle_rectangle24/", e_geometry_and_measure_views.ed18_area_triangle_rectangle24, name = "ed18_area_triangle_rectangle24"),

    path("ed20_circumference_radius_and_diameter_12/", e_geometry_and_measure_views.ed20_circumference_radius_and_diameter_12, name = "ed20_circumference_radius_and_diameter_12"),
    path("ed21_formulas_for_area_circumference_arcs_sectors_and_segments13/", e_geometry_and_measure_views.ed21_formulas_for_area_circumference_arcs_sectors_and_segments13, name = "ed21_formulas_for_area_circumference_arcs_sectors_and_segments13"),
    path("ed22_area_of_a_circle_23/", e_geometry_and_measure_views.ed22_area_of_a_circle_23, name = "ed22_area_of_a_circle_23"),
    path("ed23_circumference_of_a_circle_23/", e_geometry_and_measure_views.ed23_circumference_of_a_circle_23, name = "ed23_circumference_of_a_circle_23"),
    path("ed24_area_and_circumference_23/", e_geometry_and_measure_views.ed24_area_and_circumference_23, name = "ed24_area_and_circumference_23"),
    path("ed25_arcs_and_sectors_12/", e_geometry_and_measure_views.ed25_arcs_and_sectors_12, name = "ed25_arcs_and_sectors_12"),
    path("ed26_segments_12/", e_geometry_and_measure_views.ed26_segments_12, name = "ed26_segments_12"),
    path("ed27_segments_arcs_and_sectors13/", e_geometry_and_measure_views.ed27_segments_arcs_and_sectors13, name = "ed27_segments_arcs_and_sectors13"),
    path("ed28_area_of_a_sector26/", e_geometry_and_measure_views.ed28_area_of_a_sector26, name = "ed28_area_of_a_sector26"),
    path("ed29_length_of_arc26/", e_geometry_and_measure_views.ed29_length_of_arc26, name = "ed29_length_of_arc26"),
    path("ed210_area_of_segments37/", e_geometry_and_measure_views.ed210_area_of_segments37, name = "ed210_area_of_segments37"),
    path("ed211_area_of_pacman26/", e_geometry_and_measure_views.ed211_area_of_pacman26, name = "ed211_area_of_pacman26"),
    path("ed212_shape_problem26/", e_geometry_and_measure_views.ed212_shape_problem26, name = "ed212_shape_problem26"),

    path("ee10_terminology13/", e_geometry_and_measure_views.ee10_terminology13, name = "ee10_terminology13"),
    path("ee11_count_vertices_edges_faces13/", e_geometry_and_measure_views.ee11_count_vertices_edges_faces13, name = "ee11_count_vertices_edges_faces13"),
    path("ee12_surface_area14/", e_geometry_and_measure_views.ee12_surface_area14, name = "ee12_surface_area14"),
    path("ee13_surface_area_formulas14/", e_geometry_and_measure_views.ee13_surface_area_formulas14, name = "ee13_surface_area_formulas14"),
    path("ee14_surface_area_of_a_sphere25/", e_geometry_and_measure_views.ee14_surface_area_of_a_sphere25, name = "ee14_surface_area_of_a_sphere25"),
    path("ee15_surface_area_of_a_cylinder25/", e_geometry_and_measure_views.ee15_surface_area_of_a_cylinder25, name = "ee15_surface_area_of_a_cylinder25"),
    path("ee16_surface_area_of_a_cone25/", e_geometry_and_measure_views.ee16_surface_area_of_a_cone25, name = "ee16_surface_area_of_a_cone25"),
    path("ee17_use_surface_area_formula_to_find_an_unknown_value_in_a_sphere25/", e_geometry_and_measure_views.ee17_use_surface_area_formula_to_find_an_unknown_value_in_a_sphere25, name = "ee17_use_surface_area_formula_to_find_an_unknown_value_in_a_sphere25"),
    path("ee18_use_surface_area_formula_to_find_an_unknown_value_in_a_cyinder25/", e_geometry_and_measure_views.ee18_use_surface_area_formula_to_find_an_unknown_value_in_a_cyinder25, name = "ee18_use_surface_area_formula_to_find_an_unknown_value_in_a_cyinder25"),
    path("ee19_use_surface_area_formula_to_find_an_unknown_value_in_a_cone25/", e_geometry_and_measure_views.ee19_use_surface_area_formula_to_find_an_unknown_value_in_a_cone25, name = "ee19_use_surface_area_formula_to_find_an_unknown_value_in_a_cone25"),
    path("ee110_problem_hemisphere36/", e_geometry_and_measure_views.ee110_problem_hemisphere36, name = "ee110_problem_hemisphere36"),
 
    path("ee20_identify_the_3D_shape13/", e_geometry_and_measure_views.ee20_identify_the_3D_shape13, name = "ee20_identify_the_3D_shape13"),
    path("ee21_definitions_of_3D_shapes13/", e_geometry_and_measure_views.ee21_definitions_of_3D_shapes13, name = "ee21_definitions_of_3D_shapes13"),
    path("ee22_volume_formulas13/", e_geometry_and_measure_views.ee22_volume_formulas13, name = "ee22_volume_formulas13"),
    path("ee23_volume_of_a_prism_with_cross_sectional_area_known13/", e_geometry_and_measure_views.ee23_volume_of_a_prism_with_cross_sectional_area_known13, name = "ee23_volume_of_a_prism_with_cross_sectional_area_known13"),
    path("ee24_volume_of_a_sphere_with_radius_known25/", e_geometry_and_measure_views.ee24_volume_of_a_sphere_with_radius_known25, name = "ee24_volume_of_a_sphere_with_radius_known25"),
    path("ee25_volume_of_a_pyramid_with_base_and_height_known25/", e_geometry_and_measure_views.ee25_volume_of_a_pyramid_with_base_and_height_known25, name = "ee25_volume_of_a_pyramid_with_base_and_height_known25"),
    path("ee25_volume_of_a_cone_with_radius_and_height_known25/", e_geometry_and_measure_views.ee25_volume_of_a_cone_with_radius_and_height_known25, name = "ee25_volume_of_a_cone_with_radius_and_height_known25"),
    path("ee26_volume_of_a_frustrum_with_volume_of_original_cone_known46/", e_geometry_and_measure_views.ee26_volume_of_a_frustrum_with_volume_of_original_cone_known46, name = "ee26_volume_of_a_frustrum_with_volume_of_original_cone_known46"),
    path("ee27_volume_of_a_hemisphere_with_radius_known35/", e_geometry_and_measure_views.ee27_volume_of_a_hemisphere_with_radius_known35, name = "ee27_volume_of_a_hemisphere_with_radius_known35"),
]

exam_non_calc_patterns = [
    path('p1f_18n_9_fraction_half_way3/', exam_non_calc.p1f_18n_9_fraction_half_way3, name = 'p1f_18n_9_fraction_half_way3/')
]


urlpatterns = [
    path('', views.home, name="gcsemaths-home"),

    path('exam_non_calc/', views.home_exam_non_calc, name="exam_non_calc"),
    path('exam_non_calc/', include(exam_non_calc_patterns)),

    path('number/', views.home_number, name="number_exam_questions"),
    path('number/', include(number_patterns)),
    path('number_rand/',number_random.select_random, name="random-number"),

    path('algebra/', views.home_algebra, name="algebra_exam_questions"),
    path('algebra/', include(algebra_patterns)),
    path('algebra_rand/', algebra_views.select_random, name="random-algebra"),

    path('geometry/', views.home_geometry, name="algebra_exam_questions"),
    path('geometry/', include(geometry_patterns))
    
]
