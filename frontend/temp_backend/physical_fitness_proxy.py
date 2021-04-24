import argparse
from .physical_fitness_regime import make_month_workout_json


def check_args(request: dict) -> dict:
    """ Upon calling get_args, a parser is created that checks the validity of the parameters passed and formats them
    into a Namespace object which can be used to retrieve the parameters

     Returns:
        args: A Namespace object with all of the parameters required to create a physical workout regime
    """
    request_contains_overhead_press = len(request) == 4 and "overhead_press" in request.keys()
    overhead_press_is_int = request_contains_overhead_press and type(request["overhead_press"]) == int
    request_contains_bench_press = overhead_press_is_int and "bench_press" in request.keys()
    bench_press_is_int = request_contains_bench_press and type(request["bench_press"]) is int
    request_contains_squat = bench_press_is_int and "squat" in request.keys()
    squat_is_int = request_contains_squat and type(request["squat"]) == int
    request_contains_deadlift = squat_is_int and "deadlift" in request.keys()
    deadlift_is_int = request_contains_deadlift and type(request["deadlift"]) is int
    
    return make_month_workout_json(request)


