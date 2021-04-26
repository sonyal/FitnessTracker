import unittest
import os
import app
from appmethods import Appmethods
from werkzeug.security import generate_password_hash, check_password_hash


class TestApp(unittest.TestCase):
    def test_home_screen(self):
        client = app.app.test_client()
        response = client.get("/")
        self.assertTrue(response is not None, True)

    def test_login(self):
        client = app.app.test_client()
        response = client.get("/login")
        self.assertTrue(response is not None, True)

    def test_CardioVascular(self):
        client = app.app.test_client()
        response = client.get("/Cardiovascular")
        self.assertTrue(response is not None, True)

    def test_flex(self):
        client = app.app.test_client()
        response = client.get("/Flexibility")
        self.assertTrue(response is not None, True)

    def test_strength(self):
        client = app.app.test_client()
        response = client.get("/Strength")
        self.assertTrue(response is not None, True)

    def test_Weightloss(self):
        client = app.app.test_client()
        response = client.get("/WeightLoss")
        self.assertTrue(response is not None, True)

    def test_tutorial(self):
        client = app.app.test_client()
        response = client.get("/tutorial")
        self.assertTrue(response is not None, True)

    def test_signup(self):
        client = app.app.test_client()
        response = client.get("/signup")
        self.assertTrue(response is not None, True)

    def test_workout(self):
        client = app.app.test_client()
        response = client.get("/WorkOut")
        self.assertTrue(response is not None, True)

    def test_login_post(self):
        client = app.app.test_client()
        response = client.get("/login")
        reponse = client.post("/login", data=dict(username='joy', password='happy'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_Weightloss(self):
        client = app.app.test_client()
        response = client.get("/tutorial")
        reponse = client.post("/tutorial", data=dict(nm='WeightLoss'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_Flexibility(self):
        client = app.app.test_client()
        response = client.get("/tutorial")
        reponse = client.post("/tutorial", data=dict(nm='Flexibility'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_Strength(self):
        client = app.app.test_client()
        response = client.get("/tutorial")
        reponse = client.post("/tutorial", data=dict(nm='Strength'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_Cardio(self):
        client = app.app.test_client()
        response = client.get("/tutorial")
        reponse = client.post("/tutorial", data=dict(nm='Cardiovascular'))
        self.assertTrue(reponse is not None, True)

    def test_tutorial_post_signup(self):
        client = app.app.test_client()
        response = client.get("/signup")
        reponse = client.post("/signup", data=dict(username='joy', password='happy'))
        self.assertTrue(reponse is not None, True)

    def test_workout_select(self):
        client = app.app.test_client()
        response = client.get("/workout_select")
        self.assertTrue(response is not None, True)

    def test_flex_data(self):
        client = app.app.test_client()
        response = client.get("/flex_data")
        self.assertTrue(response is not None, True)

    def test_flex_workout(self):
        client = app.app.test_client()
        response = client.get("/flex_workout")
        self.assertTrue(response is not None, True)

    def test_cardio_data_workout(self):
        client = app.app.test_client()
        response = client.get("/cardio_data")
        self.assertTrue(response is not None, True)

    def test_cardio_front_workout(self):
        client = app.app.test_client()
        response = client.get("/cardio_workout")
        self.assertTrue(response is not None, True)

    def test_strength_data_workout(self):
        client = app.app.test_client()
        response = client.get("/strength_data")
        self.assertTrue(response is not None, True)

    def test_strength_front_workout(self):
        client = app.test_client()
        response = client.get("/strength_workout")
        self.assertTrue(response is not None, True)

    def test_cardio_post_front_workout(self):
        client = app.app.test_client()
        response = client.get("/cardio_workout")
        reponse = client.post("/cardio_workout", data=dict(swim=100, jog=100, jumpropes=100, jumpingjacks=100))
        self.assertTrue(reponse is not None, True)

    def test_flexiblity_post_front_workout(self):
        client = app.app.test_client()
        response = client.get("/strength_workout")
        reponse = client.post("/strength_workout", data=dict(overhead_press=100, bench_press=100, squat=100,
                                                             deadlift=100))
        self.assertTrue(reponse is not None, True)

    def test_strength_post_front_workout(self):
        client = app.app.test_client()
        response = client.get("/flex_workout")
        reponse = client.post("/flex_workout", data=dict(triceptsstretch=100, sitandreach=100, NeckandShoulder=100,
                                                         upandover=100))
        self.assertTrue(reponse is not None, True)

    def test_user(self):
        client = app.app.test_client()
        response = client.get("/user")
        self.assertTrue(response is not None, True)
        reponse = client.post("/user", data=dict(new_weight=100, new_height=100))
        self.assertTrue(reponse is not None, True)

    def test_confirmPassword(self):
        methods = Appmethods()
        request = methods.confirm_password("as", "as")
        self.assertTrue(request, True)
        request = methods.confirm_password("asf", "as")
        self.assertFalse(request, False)

    def test_createflexworkout(self):
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

    def test_createStrengthworkout(self):
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

    def test_createCardioworkout(self):
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

    def test_ClassPlan(self):
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
        new_plan = app.Plan(plan=outp, user_id=1)
        self.assertTrue(new_plan, True)

    def test_User(self):
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
        new_user = app.User(username="neverused", password=generate_password_hash("hope", method='sha256'),
                        weight=100, height=100)
        self.assertTrue(new_user, True)
