import argparse
from .physical_cardio_regime import make_month_workout_json


def check_args(request: dict) -> dict:
    """Upon calling get_args, a parser is created that checks the validity of the parameters passed and calls workout generator
        to return a dict with a complete month's cardio workout regime

    Args:
        request: a dictionary with 4 values
            swim: a tuple with the workout name and the maximum distance the user can do for this workout
            jog: a tuple with the workout name and the maximum distance the user can do for this workout
            jump ropes: a tuple with the workout name and the maximum reps the user can do for this workout
            jumping jacks: a tuple with the workout name and the maximum reps the user can do for this workout

     Returns:
        args: A dict with all of the parameters containing a cardio workout regime if request is valid. Else, returns single-key dict of "failure" with exit code 0
    """
    request_contains_swim = len(request) == 4 and "swim" in request.keys()
    swim_is_int = request_contains_swim and type(request["swim"]) == int
    request_contains_bench_press = swim_is_int and "jog" in request.keys()
    bench_press_is_int = request_contains_bench_press and type(request["jog"]) is int
    request_contains_squat = bench_press_is_int and "jump ropes" in request.keys()
    squat_is_int = request_contains_squat and type(request["jump ropes"]) == int
    request_contains_deadlift = squat_is_int and "jumping jacks" in request.keys()
    deadlift_is_int = (
        request_contains_deadlift and type(request["jumping jacks"]) is int
    )

    return make_month_workout_json(request) if deadlift_is_int else {"failure": 0}
