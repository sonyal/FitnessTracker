import json
import math

"""
Physical workout regime is based upon the 5/3/1 Boring But Big Challenge
Further description can be found at: https://www.t-nation.com/workouts/boring-but-big-3-month-challenge
Genuine testimony of this regime can be found at:
https://www.reddit.com/r/weightroom/comments/1d54x7/my_experience_with_the_531_bbb_3month_challenge/
"""




def make_month_workout_json(request: dict) -> json:
    """ Upon calling make_month_workout_json, a workout is made using make_month_workout and is then dumped into a
    json object with pretty printing formatting

     Args:
        request: a dictionary containing the max weight the user can do in a single repetition
     Example Args:
        {'overhead_press': 100, 'bench_press': 145, 'squat': 225, 'deadlift': 285}
        Note: this should ONLY be called from physical_fitness_proxy.py as all inputs are verified

     Returns:
        json: A JSON object with a month physical workout regime
    """
    return json.dumps(make_month_workout(request), indent=4)


def make_month_workout(request: dict) -> dict:
    """ Upon calling make_month_workout, four weeks of workouts are generated by calling make_week_workout

     Args:
        request: a dictionary containing the max weight the user can do in a single repetition

     Returns:
        dict: A dictionary with the physical workout regime adjusted for the user's strength
    """
    workout = {}
    for week in range(1, 5):
        current_week = 'week-' + str(week)
        workout[current_week] = make_week_workout(request)
    return workout


def make_week_workout(request: dict) -> dict:
    """ Upon calling make_month_workout, a single weeks of workouts are generated following the Boring But Big Challenge
    descriptions of this workout regime can be found here:
        https://www.t-nation.com/workouts/boring-but-big-3-month-challenge

     Summary:
        This workout consists of rotating power/endurance workouts primarily for overhead press / bench press for
        upper body and squat / deadlift for lower body.

        Accessories are not vital to the workout regime, but offer additional ways to extend the muscle development
        thus are highly recommended and included in the workout (but in the accessory section). Typically these
        workouts focus on a single area of the body whereas the core workouts are important to overall strength
        growth

     Args:
        request: a dictionary containing the max weight the user can do in a single repetition

     Returns:
        dict: A dictionary with the physical workout regime adjusted for the user's strength
    """
    workout = {}
    monday_request = {'indoor': ('jumpingjacks', request['jumpingjacks']),
                      'outdoor': ('jog', request['jog']), 'day': ('monday', 0)}
    workout['monday'] = make_plan(monday_request)

    wednesday_request = {'indoor': ('jumpropes', request['jumpropes']),
                         'outdoor': ('jog', request['jog']), 'day': ('wednesday', 1)}
    workout['wednesday'] = make_plan(wednesday_request)

    friday_request = {'indoor': ('jumpingjacks', request['jumpingjacks']),
                      'outdoor': ('swim', request['swim']), 'day': ('friday', 2)}
    workout['friday'] = make_plan(friday_request)

    sunday_request = {'indoor': ('jumpropes', request['jumpropes']),
                      'outdoor': ('swim', request['swim']), 'day': ('sunday', 3)}
    workout['sunday'] = make_plan(sunday_request)

    return workout


def make_plan(request: dict) -> dict:
    (indoor_workout, indoor_max) = request['indoor']
    (outdoor_workout, outdoor_max) = request['outdoor']
    (date, day) = request['day']
    return {'indoor': {indoor_workout: make_indoor_workout(indoor_workout, indoor_max, day)}, 'outdoor':
        {outdoor_workout: make_outdoor_workout(outdoor_workout, outdoor_max, day)}}


def make_indoor_workout(name: str, max, day: int) -> dict:
    workout = {}
    if name == 'jumpingjacks':
        if day == 0:
            workout['number'] = int(0.5 * int(max))
        else:
            workout['number'] = int(0.9 * int(max))
    else:
        if day == 1:
            workout['minutes'] = 0.9 * float(max)
        else:
            workout['minutes'] = 0.5 * float(max)
    return workout


def make_outdoor_workout(name: str, max, day: int) -> dict:
    workout = {}
    if name == 'jog':
        if day == 0:
            workout['length'] = 0.5 * float(max)
        else:
            workout['length'] = 0.9 * float(max)
    else:
        if day == 2:
            workout['length'] = 0.8 * float(max)
        else:
            workout['length'] = 0.5 * float(max)
    return workout
