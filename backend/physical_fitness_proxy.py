import argparse
#import physical_fitness_regime

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


def get_args() -> argparse.Namespace:
    """ Upon calling get_args, a parser is created that checks the validity of the parameters passed and formats them
    into a Namespace object which can be used to retrieve the parameters

     Returns:
        args: A Namespace object with all of the parameters required to create a physical workout regime
    """
    parser = argparse.ArgumentParser(description='Generates a JSON of the physical workout regime')
    parser.add_argument('--overhead_press', required=True, type=int, help='Max single repetition of Overhead Press')
    parser.add_argument('--bench_press', required=True, type=int, help='Max single repetition of Bench Press')
    parser.add_argument('--squat', required=True, type=int, help='Max single repetition of Squat')
    parser.add_argument('--deadlift', required=True, type=int, help='Max single repetition of Deadlift')
    return parser.parse_args()


def format_args(arguments: argparse.Namespace) -> dict:
    """ Upon calling format_args, the Namespace object will be converted into a dictionary to easily allow the
    physical_fitness_regime to handle creating a JSON of the workout regime

     Args:
        arguments: A namespace object that contains the user's maximum single repetition of each core physical
        workout in this regime (overhead_press, bench_press, squat, and deadlift)

     Returns:
        dict: A dictionary with each workout in the physical regime pointing to the user's maximum single repetition
        of that workout
    """
    return {'overhead_press': int(arguments.overhead_press), 'bench_press': int(arguments.bench_press),
            'squat': int(arguments.squat), 'deadlift': int(arguments.deadlift)}


args = get_args()
request = format_args(args)
#print(physical_fitness_regime.make_month_workout_json(request))
