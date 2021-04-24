from flask import Flask, redirect, url_for, render_template, flash, request
from .tutorialsearch import RegistrationForm, TestLinkProxy
from .forms import SignUpForm, WorkOutForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from os import path

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness_database.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))


@app.route("/")
def home():
    return render_template('index.html')


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
                print("Login successfully!")
            else:
                print("failed!")

    return render_template('login.html', form=form)


@app.route("/Cardiovascular", methods=['GET', 'POST'])
def cardiovascular():
    return render_template('cardio.html')


@app.route("/Flexibility", methods=['GET', 'POST'])
def flexibility():
    return render_template('flex.html')


@app.route("/Strength", methods=['GET', 'POST'])
def strength():
    return render_template('Strength.html')


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
        if test_results == 3:
            return redirect(url_for("weightloss"))
        return render_template('tutorialsearch.html')
    else:
        return render_template('tutorialsearch.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        username = result.get('username')
        password = result.get('password')

        try:
            new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
        except:
            print("User existed!")
            return render_template('signup.html', form=form)

        print("User:" + username + " with password:" + password + " is created!")

        return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route('/WorkOut', methods=['GET', 'POST'])
def workout():
    form = WorkOutForm()
    if form.is_submitted():
        result = request.form
    return render_template('WorkOut.html', form=form)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
