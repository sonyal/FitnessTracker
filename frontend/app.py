from flask import Flask, redirect, url_for, render_template, flash, request
from tutorialsearch import RegistrationForm, TestLinkProxy
from forms import SignUpForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from os import path
from temp_backend import physical_cardio_proxy as cardio_proxy
from temp_backend import physical_fitness_proxy as strength_proxy
from  temp_backend import physical_flex_proxy as flex_proxy
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness_database.db'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# Model for plan which belongs to User
# One User can have multi Plan
class Plan(db.Model):
    id = db.Column(db.Integer, primary_key = True)\
    # plan = db.Column(db.JSON)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# User Model which stores all the User information
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50))
    weight = db.Column(db.String(30))
    height = db.Column(db.String(30))
    plans = db.relationship('Plan')
    
@app.route("/")
def home():
    return render_template('index.html', user=current_user)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted():
        result = request.form
        username = result.get('username')
        password = result.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=False)
                return redirect(url_for('user_page'))
            else:
                flash('Your Login Information is incorrect, please try again!', category='error')
        else:
            flash('Your Login Information is incorrect, please try again!', category='error')

    return render_template('login.html', form=form, user=current_user)

@app.route('/logout')
@login_required
def log_out():
    logout_user()
    return redirect(url_for('login'))

@app.route("/user", methods=['GET', 'POST'])
@login_required
def user_page():
    if request.method == 'POST':
        if request.form.get('new_weight'):
            new_weight = request.form.get('new_weight')
            current_user.weight = new_weight
            db.session.commit()
        else:
            new_height = request.form.get('new_height')
            current_user.height = new_height
            db.session.commit()
    
    return render_template('user_page.html', user=current_user)

@app.route("/Cardiovascular", methods=["GET", "POST"])
def cardiovascular():
    return render_template("cardio.html")


@app.route("/Flexibility", methods=['GET', 'POST'])
def flexibility():
    return render_template("flex.html")


@app.route("/Strength", methods=["GET", "POST"])
def strength():
    return render_template("Strength.html")


@app.route("/WeightLoss", methods=['GET', 'POST'])
def weightloss():
    return render_template('weightloss.html')


@app.route("/tutorial", methods=['GET', 'POST'])
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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if not path.exists('frontend/fitness_database.db'):
        db.create_all(app=app)

    form = SignUpForm()

    if form.is_submitted():
        result = request.form
        username = result.get('username')
        password1 = result.get('password')
        password2 = result.get('confirm_password')
        weight = result.get('weight')
        height = result.get('height')
    
        if not confirm_password(password1, password2):
            flash('Two passwords are not matched', category='error')
        elif len(username) < 4:
            flash('Username must be at least 4 characters', category='error')
        elif len(password1)< 12:
            flash('Password must be at least 12 characters', category='error')
        else:
            try:
                new_user = User(username=username, password=generate_password_hash(password1, method='sha256'), weight=weight, height=height)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('login'))
            except:
                flash('User Creation Failed, please try another username!', category='error')

    return render_template('signup.html', form=form, user=current_user)

def confirm_password(p1, p2):
    if p1 == p2:
        return True
    else:
        return False

@app.route("/workout_select")
@login_required
def workout_select():
    return render_template("workout_selector.html", user=current_user)

@app.route("/flex_data")
@login_required
def flex_data():
    return render_template("flex_data_input.html", user=current_user)

@app.route("/flex_workout", methods=["GET", "POST"])
@login_required
def flex_workout():
    if request.method == "POST":
        workout = create_flex_workout(request.form)
        if workout:
            new_plan = Plan(plan=workout, user_id=current_user.id)
            db.session.add(new_plan)
            db.session.commit()

    return render_template("generated_flex_workout.html", result=workout, user=current_user)

def create_flex_workout(request: dict) -> dict:
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
    workout = format_flex_workout(workout)
    return workout

def format_flex_workout(request: dict) -> dict:
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
    return result

@app.route("/cardio_data")
@login_required
def cardio_data():
    return render_template("cardio_data_input.html", user=current_user)

@app.route("/cardio_workout", methods=["GET", "POST"])
@login_required
def cardio_workout():
    if request.method == "POST":
        workout = create_cardio_workout(request.form)
        if workout:
            new_plan = Plan(plan=workout, user_id=current_user.id)
            db.session.add(new_plan)
            db.session.commit()
        return render_template("generated_cardio_workout.html", result=workout, user=current_user)

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
    return result

@app.route("/strength_data")
@login_required
def strength_data():
    return render_template("strength_data_input.html", user=current_user)


@app.route("/strength_workout", methods=["GET", "POST"])
@login_required
def strength_workout():
    if request.method == "POST":
        workout = create_workout(request.form)
        if workout:
            new_plan = Plan(plan=workout, user_id=current_user.id)
            db.session.add(new_plan)
            db.session.commit()
        return render_template("generated_strength_workout.html", result=workout, user=current_user)

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
