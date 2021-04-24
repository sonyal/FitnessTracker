import unittest
import os
from frontend import app


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
