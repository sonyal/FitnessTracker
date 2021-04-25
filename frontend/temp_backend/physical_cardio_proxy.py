import argparse
from .physical_cardio_regime import make_month_workout_json

"""
Required Arguments to physical_fitness_proxy:
    --overhead_press: The maximum the user can do a single rep of overhead press
    --bench_press: The maximum the user can do a single rep of bench press
    --squat: The maximum the user can do a single rep of squat
    --deadlift: The maximum the user can do a single rep of deadlift
"""
def check_args(request: dict) -> dict:
    request_contains_swim = len(request) == 4 and "swim" in request.keys()
    swim_is_int = (request_contains_swim and type(request["swim"]) == int)
    request_contains_bench_press = swim_is_int and "jog" in request.keys()
    bench_press_is_int = request_contains_bench_press and type(request["jog"]) is int
    request_contains_squat = bench_press_is_int and "jump ropes" in request.keys()
    squat_is_int = request_contains_squat and type(request["jump ropes"]) == int
    request_contains_deadlift = squat_is_int and "jumping jacks" in request.keys()
    deadlift_is_int = (request_contains_deadlift and type(request["jumping jacks"]) is int)

    return make_month_workout_json(request)
