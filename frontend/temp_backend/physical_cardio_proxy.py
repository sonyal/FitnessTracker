import argparse
from .physical_cardio_regime import make_month_workout_json
"""
Required Arguments to physical_fitness_proxy:
    --overhead_press: The maximum the user can do a single rep of overhead press
    --bench_press: The maximum the user can do a single rep of bench press
    --squat: The maximum the user can do a single rep of squat
    --deadlift: The maximum the user can do a single rep of deadlift
    
Example usage:

Correct Script Call:
    python3 physical_fitness_proxy.py --overhead_press 100 --bench_press 145 --squat 225 --deadlift 285
        After reaching format_args, would return a dictionary like:
            {'overhead_press': 100, 'bench_press': 145, 'squat': 225, 'deadlift': 285}
            
Incorrect Script Call:
    python3 physical_fitness_proxy.py --overhead_press 100 --bench_press 145 --squat 225
        Output Message:
        usage: physical_fitness_proxy.py [-h] --overhead_press OVERHEAD_PRESS --bench_press BENCH_PRESS --squat SQUAT
                                 --deadlift DEADLIFT
        physical_fitness_proxy.py: error: the following arguments are required: --deadlift
"""


def check_args(request: dict) -> dict:
    """ Upon calling get_args, a parser is created that checks the validity of the parameters passed and formats them
    into a Namespace object which can be used to retrieve the parameters

     Returns:
        args: A Namespace object with all of the parameters required to create a physical workout regime
    """
    request_contains_overhead_press = len(request) == 4 and "swim" in request.keys()
    overhead_press_is_int = request_contains_overhead_press and type(request["swim"]) == int
    request_contains_bench_press = overhead_press_is_int and "jog" in request.keys()
    bench_press_is_int = request_contains_bench_press and type(request["jog"]) is int
    request_contains_squat = bench_press_is_int and "jump ropes" in request.keys()
    squat_is_int = request_contains_squat and type(request["jump ropes"]) == int
    request_contains_deadlift = squat_is_int and "jumping jacks" in request.keys()
    deadlift_is_int = request_contains_deadlift and type(request["jumping jacks"]) is int
    
    return make_month_workout_json(request)
