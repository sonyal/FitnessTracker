import argparse
from .physical_fitness_regime import make_month_workout_json


def check_args(request: dict) -> dict:
    """Upon calling get_args, a parser is created that checks the validity of the parameters passed and calls workout
        generator to return a dict with a complete month's physical workout regime

    Args:
        request: a dictionary with 4 values
            overhead_press: a tuple with the workout name and the maximum weight the user can do for this workout
            bench_press: a tuple with the workout name and the maximum weight the user can do for this workout
            squat: a tuple with the workout name and the maximum weight the user can do for this workout
            deadlift: a tuple with the workout name and the maximum weight the user can do for this workout

     Returns:
        args: A dict with all of the parameters containing a physical workout regime if request is valid. Else,
        returns single-key dict of "failure" with exit code 0
    """
    request_contains_overhead_press = (
        len(request) == 4 and "overhead_press" in request.keys()
    )
    overhead_press_is_int = (
        request_contains_overhead_press and type(request["overhead_press"]) == int
    )
    request_contains_bench_press = (
        overhead_press_is_int and "bench_press" in request.keys()
    )
    bench_press_is_int = (
        request_contains_bench_press and type(request["bench_press"]) is int
    )
    request_contains_squat = bench_press_is_int and "squat" in request.keys()
    squat_is_int = request_contains_squat and type(request["squat"]) == int
    request_contains_deadlift = squat_is_int and "deadlift" in request.keys()
    deadlift_is_int = request_contains_deadlift and type(request["deadlift"]) is int

    return make_month_workout_json(request) if deadlift_is_int else {"failure": 0}
