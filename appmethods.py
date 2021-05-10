
import json
from backend import physical_cardio_proxy as cardio_proxy
from backend import physical_fitness_proxy as strength_proxy
from backend import physical_flex_proxy as flex_proxy
import datetime as dt
from datetime import datetime
from datetime import date

class Appmethods:
    def __init__(self):
        self.deck = {}

    def create_flex_workout(self, request: dict) -> dict:
        try:
            tricepsstretch = int(request.get("triceps stretch"))
            sitandreach = int(request.get("sit and reach"))
            neckandshoulderrelease = int(request.get("Neck-and-Shoulder Release"))
            upandover = int(request.get("up and over"))
        except ValueError:
            return {"failure": 0}

        result = {
            "triceps stretch": tricepsstretch,
            "sit and reach": sitandreach,
            "Neck-and-Shoulder Release": neckandshoulderrelease,
            "up and over": upandover
        }


        workout = json.loads(flex_proxy.check_args(result))
        workout = self.format_flex_workout(workout)
        return workout

    def format_flex_workout(self, request: dict) -> dict:
        result = {}
        for week, value1 in request.items():
            result[self.reword(week)] = {}
            for day, value2 in value1.items():
                result[self.reword(week)][day] = {}
                for location, value3 in value2.items():
                    result[self.reword(week)][day][location] = {}
                    for exercise, value4 in value3.items():
                        result[self.reword(week)][day][location][exercise] = {}
                        for thing, value5 in value4.items():
                            result[self.reword(week)][day][location][exercise][thing] = value5
        return result

    def create_workout(self, request: dict) -> dict:
        try:
            overhead_press = int(request.get("overhead_press"))
            bench_press = int(request.get("bench_press"))
            squat = int(request.get("squat"))
            deadlift = int(request.get("deadlift"))
        except ValueError:
            return {"failure": 0}

        result = {
            "overhead_press": int(overhead_press),
            "bench_press": int(bench_press),
            "squat": int(squat),
            "deadlift": int(deadlift),
        }
        workout = json.loads(strength_proxy.check_args(result))
        workout = self.format_strength_workout(workout)
        return workout

    def format_strength_workout(self, request: dict) -> dict:
        result = {}
        for week, value1 in request.items():
            result[self.reword(week)] = {}
            for day, value2 in value1.items():
                result[self.reword(week)][day] = {}
                for area, value3 in value2.items():
                    result[self.reword(week)][day][area] = {}
                    for exercise, value4 in value3.items():
                        result[self.reword(week)][day][area][self.reword(exercise)] = {}
                        for sets, value5 in value4.items():
                            result[self.reword(week)][day][area][self.reword(exercise)][self.reword(sets)] = {}
                            if value5 is dict:
                                for reps, value6 in value5.items():
                                    result[self.reword(week)][day][area][self.reword(exercise)][
                                        self.reword(sets)][
                                        self.reword(reps)] = value6
                            else:
                                result[self.reword(week)][day][area][self.reword(exercise)][
                                    self.reword(sets)] = value5

        return result

    def reword(self, word: str) -> str:
        if "set-" in word:
            return "set " + word[4]
        if "week-" in word:
            return "Week " + word[5]
        switcher = {
            "overhead_press": "overhead press",
            "bench_press": "bench press",
            "tricep_pushdown": "tricep pushdown",
            "face_pulls": "face pulls",
            "ab_wheel": "ab wheel",
            "russian_twists": "russian twists",
        }

        return switcher.get(word, word)

    def create_cardio_workout(self, request: dict) -> dict:
        try:
            swim = int(request.get("swim"))
            jog = int(request.get("jog"))
            jumpropes = int(request.get("jump ropes"))
            jumpingjacks = int(request.get("jumping jacks"))
        except ValueError:
            return {"failure": 0}
        
        result = {
            "swim": swim,
            "jog": jog,
            "jump ropes": jumpropes,
            "jumping jacks": jumpingjacks
        }
        workout = json.loads(cardio_proxy.check_args(result))
        workout = self.format_cardio_workout(workout)
        return workout

    def format_cardio_workout(self, request: dict) -> dict:
        result = {}
        for week, value1 in request.items():
            result[self.reword(week)] = {}
            for day, value2 in value1.items():
                result[self.reword(week)][day] = {}
                for location, value3 in value2.items():
                    result[self.reword(week)][day][location] = {}
                    for exercise, value4 in value3.items():
                        result[self.reword(week)][day][location][exercise] = {}
                        for thing, value5 in value4.items():
                            result[self.reword(week)][day][location][exercise][thing] = value5
        return result

    def confirm_password(self, p1, p2):
        if p1 == p2:
            return True
        else:
            return False

    def create_progress(self, workout):
        # today's date in real life
        today = date.today() - dt.timedelta(10)

        workout_date_dict = {"start_date": today.strftime('%Y-%m-%d')}
        return workout_date_dict

    # compute the progress. return a list, finished task marked as active, unfinished marked as ""
    def compute_progress_bar(self, progress):
        # start date: which is the next monday after the start date
        start_date = datetime.strptime(progress["start_date"], '%Y-%m-%d')

        # list of dates which has workouts, totally 12 days
        temp_date = start_date;
        workout_dates = []
        i = 3
        while i > 0:
            workout_dates.append(self.next_week_day(temp_date, 0))
            workout_dates.append(self.next_week_day(temp_date, 2))
            workout_dates.append(self.next_week_day(temp_date, 4))
            workout_dates.append(self.next_week_day(temp_date, 6))
            temp_date = self.next_week_day(temp_date, 0)
            i = i - 1

        today = datetime.now()

        result = []
        for x in workout_dates:
            if x < today:
                result.append({'active_string': 'active', 'day_string': x.strftime('%Y-%m-%d-%W')})
            else:
                result.append({'active_string': '', 'day_string': x.strftime('%Y-%m-%d-%W')})
        return result

    def next_week_day(self, d, x):
        days_ahead = x - d.weekday()
        days_ahead += 7
        return d + dt.timedelta(days_ahead)