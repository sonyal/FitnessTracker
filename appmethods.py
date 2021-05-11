
import json
from backend import physical_cardio_proxy as cardio_proxy
from backend import physical_fitness_proxy as strength_proxy
from backend import physical_flex_proxy as flex_proxy


class Appmethods:
    def __init__(self):
        self.deck = {}

    def create_flex_workout(self, request: dict) -> dict:
        tricepsstretch = request.get("triceps stretch")
        sitandreach = request.get("sit and reach")
        neckandshoulderrelease = request.get("Neck-and-Shoulder Release")
        upandover = request.get("up and over")
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
        overhead_press = request.get("overhead_press")
        bench_press = request.get("bench_press")
        squat = request.get("squat")
        deadlift = request.get("deadlift")
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
        swim = request.get("swim")
        jog = request.get("jog")
        jumpropes = request.get("jump ropes")
        jumpingjacks = request.get("jumping jacks")
        result = {
            "swim": swim,
            "jog": jog,
            "jump ropes": jumpropes,
            "jumping jacks": int(jumpingjacks)
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
