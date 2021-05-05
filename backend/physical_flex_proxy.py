import argparse
from .physical_flex_regime import make_month_workout_json

def check_args(request: dict) -> dict:
    """" Upon calling get_args, a parser is created that checks the validity of the parameters passed and calls workout generator
        to return a dict with a complete month's flexibility workout regime 

    Args:
        request: a dictionary with 4 values
            triceps stretch: a tuple with the workout name and the maximum reps the user can do for this workout
            Neck-and-Shoulder Release: a tuple with the workout name and the maximum reps the user can do for this workout
            sit and reach: a tuple with the workout name and the maximum reps the user can do for this workout
            up and over: a tuple with the workout name and the maximum reps the user can do for this workout
        
     Returns:
        args: A dict with all of the parameters containing a flexibility workout regime
    """
    request_contains_triceps = len(request) == 4 and "triceps stretch" in request.keys()
    triceps_is_int = request_contains_triceps and type(request["triceps stretch"]) == int
    request_contains_bench_press = triceps_is_int and "Neck-and-Shoulder Release" in request.keys()
    bench_press_is_int = request_contains_bench_press and type(request["Neck-and-Shoulder Release"]) is int
    request_contains_squat = bench_press_is_int and "sit and reach" in request.keys()
    squat_is_int = request_contains_squat and type(request["sit and reach"]) == int
    request_contains_deadlift = squat_is_int and "up and over" in request.keys()
    deadlift_is_int = request_contains_deadlift and type(request["up and over"]) is int

    return make_month_workout_json(request)
