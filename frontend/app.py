from flask import Flask, redirect, url_for, render_template, flash, request
from tutorialsearch import RegistrationForm, TestLinkProxy
from forms import SignUpForm, WorkOutForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
from temp_backend import physical_cardio_proxy as cardio_proxy
import temp_backend.physical_fitness_proxy as strength_proxy
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = "5791628bb0b13ce0c676dfde280ba245"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///fitness_database.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.is_submitted():
        result = request.form
        username = result.get("username")
        password = result.get("password")
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                print("Login successfully!")
            else:
                print("failed!")

    return render_template("login.html", form=form)


@app.route("/Cardiovascular", methods=["GET", "POST"])
def cardiovascular():
    return render_template("cardio.html")


@app.route("/Flexibility", methods=["GET", "POST"])
def flexibility():
    return render_template("flex.html")


@app.route("/Strength", methods=["GET", "POST"])
def strength():
    return render_template("Strength.html")

@app.route("/WeightLoss", methods=['GET', 'POST'])
def weightloss():
    return render_template('weightloss.html')

@app.route("/tutorial", methods=["GET", "POST"])
def tutorial():
    if request.method == "POST":
        user = request.form["nm"]
        test_link = TestLinkProxy()
        test_results = test_link.test_link(user)
        if test_results == -1:
            flash("Not a valid Workout Plan", "danger")
        if test_results == 0:
            return redirect(url_for("cardiovascular"))
        if test_results == 1:
            return redirect(url_for("flexibility"))
        if test_results == 2:
            return redirect(url_for("strength"))
        return render_template("tutorialsearch.html")
    else:
        return render_template("tutorialsearch.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        username = result.get("username")
        password = result.get("password")

        try:
            new_user = User(
                username=username,
                password=generate_password_hash(password, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
        except:
            print("User existed!")
            return render_template("signup.html", form=form)

        print("User:" + username + " with password:" + password + " is created!")

        return redirect(url_for("login"))

    return render_template("signup.html", form=form)


@app.route("/cardio_data")
def cardio_data():
    return render_template("cardio_data_input.html")


@app.route("/cardio_workout", methods=["GET", "POST"])
def cardio_workout():
    if request.method == "POST":
        workout = create_cardio_workout(request.form)
        return render_template("generated_cardio_workout.html", result=workout)




def create_cardio_workout(request: dict) -> dict:
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
    workout = format_cardio_workout(workout)
    return workout

def format_cardio_workout(request: dict) -> dict:
    result = {}
    for week, value1 in request.items():
        result[reword(week)] = {}
        for day, value2 in value1.items():
            result[reword(week)][day] = {}
            for location, value3 in value2.items():
                result[reword(week)][day][location] = {}
                for exercise, value4 in value3.items():
                    result[reword(week)][day][location][exercise] = {}
                    for thing, value5 in value4.items():
                        result[reword(week)][day][location][exercise][thing] = value5
                #for exercise, value4 in value3.items():
                #    result[reword(week)][day][area][reword(exercise)] = {}
                #    for sets, value5 in value4.items():
                #        result[reword(week)][day][area][reword(exercise)][reword(sets)] = {}
                #        if value5 is dict:
                #            for reps, value6 in value5.items():
                #                result[reword(week)][day][area][reword(exercise)][reword(sets)][reword(reps)] = value6
                #        else:
                #            result[reword(week)][day][area][reword(exercise)][reword(sets)] = value5

    return result


@app.route("/WorkOut", methods=["GET", "POST"])
def workout():
    form = WorkOutForm()
    if form.is_submitted():
        result = request.form
    return render_template("WorkOut.html", form=form)


@app.route("/strength_data")
def strength_data():
    return render_template("strength_data_input.html")


@app.route("/strength_workout", methods=["GET", "POST"])
def strength_workout():
    if request.method == "POST":
        workout = create_workout(request.form)
        return render_template("generated_strength_workout.html", result=workout)


def create_workout(request: dict) -> dict:
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
    workout = format_strength_workout(workout)
    return workout


def format_strength_workout(request: dict) -> dict:
    result = {}
    for week, value1 in request.items():
        result[reword(week)] = {}
        for day, value2 in value1.items():
            result[reword(week)][day] = {}
            for area, value3 in value2.items():
                result[reword(week)][day][area] = {}
                for exercise, value4 in value3.items():
                    result[reword(week)][day][area][reword(exercise)] = {}
                    for sets, value5 in value4.items():
                        result[reword(week)][day][area][reword(exercise)][reword(sets)] = {}
                        if value5 is dict:
                            for reps, value6 in value5.items():
                                result[reword(week)][day][area][reword(exercise)][reword(sets)][reword(reps)] = value6
                        else:
                            result[reword(week)][day][area][reword(exercise)][reword(sets)] = value5

    return result


def reword(word: str) -> str:
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


if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    app.run()
