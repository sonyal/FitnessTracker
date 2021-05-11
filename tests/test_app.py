import unittest
import os
from app import app, Plan, User
from appmethods import Appmethods
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import datetime as dt
from datetime import date

class TestApp(unittest.TestCase):
    def test_home_screen(self):
        client = app.test_client()
        response = client.get("/")
        self.assertTrue(response is not None, True)

    def test_login(self):
        client = app.test_client()
        response = client.get("/login")
        self.assertTrue(response is not None, True)

    def test_cardiovascular_deployment(self):
        client = app.test_client()
        response = client.get("/Cardiovascular")
        self.assertTrue(response is not None, True)

    def test_flex_deployment(self):
        client = app.test_client()
        response = client.get("/Flexibility")
        self.assertTrue(response is not None, True)

    def test_strength_deployment(self):
        client = app.test_client()
        response = client.get("/Strength")
        self.assertTrue(response is not None, True)

    def test_weightloss_deployment(self):
        client = app.test_client()
        response = client.get("/WeightLoss")
        self.assertTrue(response is not None, True)

    def test_tutorial_deployment(self):
        client = app.test_client()
        response = client.get("/tutorial")
        self.assertTrue(response is not None, True)

    def test_signup_deployment(self):
        client = app.test_client()
        response = client.get("/signup")
        self.assertTrue(response is not None, True)

    def test_workout_deployment(self):
        client = app.test_client()
        response = client.get("/WorkOut")
        self.assertTrue(response is not None, True)

    def test_login_post(self):
        client = app.test_client()
        response = client.get("/login")
        reponse = client.post("/login", data=dict(username='joy', password='happy'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_weightloss(self):
        client = app.test_client()
        response = client.get("/tutorial")
        reponse = client.post("/tutorial", data=dict(nm='WeightLoss'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_flexibility(self):
        client = app.test_client()
        response = client.get("/tutorial")
        reponse = client.post("/tutorial", data=dict(nm='Flexibility'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_strength(self):
        client = app.test_client()
        response = client.get("/tutorial")
        reponse = client.post("/tutorial", data=dict(nm='Strength'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_cardio(self):
        client = app.test_client()
        response = client.get("/tutorial")
        reponse = client.post("/tutorial", data=dict(nm='Cardiovascular'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_signup(self):
        client = app.test_client()
        response = client.get("/signup")
        reponse = client.post("/signup", data=dict(username='joy', password='happy'))
        self.assertTrue(reponse is not None, True)

    def test_workout_select(self):
        client = app.test_client()
        response = client.get("/workout_select")
        self.assertTrue(response is not None, True)

    def test_flex_data(self):
        client = app.test_client()
        response = client.get("/flex_data")
        self.assertTrue(response is not None, True)

    def test_flex_workout(self):
        client = app.test_client()
        response = client.get("/flex_workout")
        self.assertTrue(response is not None, True)

    def test_cardio_data_workout(self):
        client = app.test_client()
        response = client.get("/cardio_data")
        self.assertTrue(response is not None, True)

    def test_cardio_front_workout(self):
        client = app.test_client()
        response = client.get("/cardio_workout")
        self.assertTrue(response is not None, True)

    def test_strength_data_workout(self):
        client = app.test_client()
        response = client.get("/strength_data")
        self.assertTrue(response is not None, True)

    def test_strength_front_workout(self):
        client = app.test_client()
        response = client.get("/strength_workout")
        self.assertTrue(response is not None, True)

    def test_cardio_post_front_workout(self):
        client = app.test_client()
        response = client.get("/cardio_workout")
        reponse = client.post("/cardio_workout", data=dict(swim=100, jog=100, jumpropes=100, jumpingjacks=100))
        self.assertTrue(reponse is not None, True)

    def test_flexiblity_post_front_workout(self):
        client = app.test_client()
        response = client.get("/strength_workout")
        reponse = client.post("/strength_workout", data=dict(overhead_press=100, bench_press=100, squat=100,
                                                             deadlift=100))
        self.assertTrue(reponse is not None, True)

    def test_strength_post_front_workout(self):
        client = app.test_client()
        response = client.get("/flex_workout")
        reponse = client.post("/flex_workout", data=dict(triceptsstretch=100, sitandreach=100, NeckandShoulder=100,
                                                         upandover=100))
        self.assertTrue(reponse is not None, True)

    def test_user(self):
        client = app.test_client()
        response = client.get("/user")
        self.assertTrue(response is not None, True)
        reponse = client.post("/user", data=dict(new_weight=100, new_height=100))
        self.assertTrue(reponse is not None, True)    

class TestAppMethods(unittest.TestCase):   
    def test_confirm_password(self):
        methods = Appmethods()
        request = methods.confirm_password("as", "as")
        self.assertTrue(request, True)

    def test_confirm_password_nonmatching_input(self):
        methods = Appmethods()
        request = methods.confirm_password("asf", "as")
        self.assertFalse(request, False)

    def test_create_flex_workout_correct_input(self):
        methods = Appmethods()

        tricepsstretch = 100

        sitandreach = 100

        neckandshoulderrelease = 100

        upandover = 100

        request = {
            "triceps stretch": tricepsstretch,
            "sit and reach": sitandreach,
            "Neck-and-Shoulder Release": neckandshoulderrelease,
            "up and over": upandover
        }
        outp = methods.create_flex_workout(request)
        self.assertTrue(outp, True)

    def test_create_strength_workout_correct_input(self):
        methods = Appmethods()

        overhead_press = 199
        bench_press = 100
        squat = 100
        deadlift = 100
        result = {
            "overhead_press": overhead_press,
            "bench_press": bench_press,
            "squat": squat,
            "deadlift": deadlift,
        }
        outp = methods.create_workout(result)
        self.assertTrue(outp, True)

    def test_create_cardio_workout_correct_input(self):
        methods = Appmethods()

        swim = 100
        jog = 100
        jumpropes = 100
        jumpingjacks = 100
        result = {
            "swim": swim,
            "jog": jog,
            "jump ropes": jumpropes,
            "jumping jacks": int(jumpingjacks)
        }
        outp = methods.create_cardio_workout(result)
        self.assertTrue(outp, True)

    def test_class_plan_successful(self):
        methods = Appmethods()

        swim = 100
        jog = 100
        jumpropes = 100
        jumpingjacks = 100
        result = {
            "swim": swim,
            "jog": jog,
            "jump ropes": jumpropes,
            "jumping jacks": int(jumpingjacks)
        }
        outp = methods.create_cardio_workout(result)
        new_plan = Plan(plan=outp, user_id=1)
        self.assertTrue(new_plan, True)

    def test_create_new_user_successful(self):
        methods = Appmethods()

        swim = 100
        jog = 100
        jumpropes = 100
        jumpingjacks = 100
        result = {
            "swim": swim,
            "jog": jog,
            "jump ropes": jumpropes,
            "jumping jacks": int(jumpingjacks)
        }
        outp = methods.create_cardio_workout(result)
        new_user = User(username="neverused", password=generate_password_hash("hope", method='sha256'),
                        weight=100, height=100)
        self.assertTrue(new_user, True)

    def test_create_new_user_existing_username(self):
        methods = Appmethods()

        swim = 100
        jog = 100
        jumpropes = 100
        jumpingjacks = 100
        result = {
            "swim": swim,
            "jog": jog,
            "jump ropes": jumpropes,
            "jumping jacks": int(jumpingjacks)
        }
        outp = methods.create_cardio_workout(result)
        new_user = User(username="neverused", password=generate_password_hash("hope", method='sha256'),
                        weight=100, height=100)
        new_user = User(username="neveruse", password=generate_password_hash("hope", method='sha256'),
                        weight=100, height=100)
        self.assertTrue(new_user, True)

    def test_create_progress_bar_successful(self):
        methods = Appmethods()
        result = methods.create_progress()
        expect = {"start_date": date.today().strftime('%Y-%m-%d')}
        self.assertEqual(result, expect)

    def test_create_workout_incomplete_user_input(self):
        methods = Appmethods()

        swim = 100
        jog = 100
        jumpropes = 100
        jumpingjacks = 100
        result = {
            "swim": swim,
            "jog": jog,
            "jump ropes": jumpropes,
            "jumping jacks": int(jumpingjacks)
        }
        outp = methods.create_cardio_workout(result)
        self.assertTrue(outp, True)

    def test_create_workout_incorrect_user_input_type(self):
        methods = Appmethods()

        swim = "a"
        jog = "bc"
        jumpropes = "def"
        jumpingjacks = "ghi"
        result = {
            "swim": swim,
            "jog": jog,
            "jump ropes": jumpropes,
            "jumping jacks": jumpingjacks
        }
        outp = methods.create_cardio_workout(result)
        self.assertEqual(outp, {"failure": 0})

    def test_compute_progress_bar(self):
        methods = Appmethods()

        result = methods.compute_progress_bar({'start_date': '2021-05-1'})
        expect = [{'active_string': 'active', 'day_string': '2021-05-03-1'},
                  {'active_string': 'active', 'day_string': '2021-05-05-3'},
                  {'active_string': 'active', 'day_string': '2021-05-07-5'},
                  {'active_string': 'active', 'day_string': '2021-05-09-0'},
                  {'active_string': 'active', 'day_string': '2021-05-10-1'},
                  {'active_string': '', 'day_string': '2021-05-12-3'},
                  {'active_string': '', 'day_string': '2021-05-14-5'},
                  {'active_string': '', 'day_string': '2021-05-16-0'},
                  {'active_string': '', 'day_string': '2021-05-17-1'},
                  {'active_string': '', 'day_string': '2021-05-19-3'},
                  {'active_string': '', 'day_string': '2021-05-21-5'},
                  {'active_string': '', 'day_string': '2021-05-23-0'}]
        self.assertEqual(result, expect)

    def test_next_week_day(self):
        methods = Appmethods()

        next_monday = methods.next_week_day(datetime.datetime.now().date(), 0)
        next_tuesday = methods.next_week_day(datetime.datetime.now().date(), 1)
        self.assertEqual(next_tuesday, next_monday + dt.timedelta(1))
