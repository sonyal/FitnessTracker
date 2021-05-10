from flask import Flask, redirect, url_for, render_template, flash, request
from tutorialsearch import RegistrationForm, TempLinkProxy
from forms import SignUpForm, LoginForm
from models import db, User, Plan
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from os import path
from appmethods import Appmethods
from backend import physical_cardio_proxy as cardio_proxy
from backend import physical_fitness_proxy as strength_proxy
from backend import physical_flex_proxy as flex_proxy
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fitness_database.db'
db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    if not path.exists('fitness_database.db'):
        db.create_all(app=app)
    return User.query.get(int(id))


@app.route("/")
def home():
    """
        Renders our home screen and checks if the user is logged in
    Returns:
        template of the home page
    """
    return render_template('index.html', user=current_user)


@app.route("/login", methods=['GET', 'POST'])
def login():
    """
        Checks log in for application. If the user signals a "get" we return the template of the page for the user to
        login into. If the user posts their username and password we log them in by checking the database for their
        information. If we find it we redirect them to the home page. Otherwise we signal to the user to try again
    Returns:
        Get- template of the login page
        Post and True - returns user to user page
    """
    if not path.exists('fitness_database.db'):
        db.create_all(app=app)
    form = LoginForm()
    if form.is_submitted():
        result = request.form
        username = result.get('username')
        password = result.get('password')
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('user_page'))
            else:
                flash('Your Login Information is incorrect, please try again!', category='error')
        else:
            flash('Your Login Information is incorrect, please try again!', category='error')

    return render_template('login.html', form=form, user=current_user)


@app.route('/logout')
@login_required
def log_out():
    """
        user is logged out of account and redirected to login page
    Returns:
        template for login page
    """
    logout_user()
    return redirect(url_for('login'))


@app.route('/delete')
@login_required
def delete_account():
    """
        user is deleted from the database and is then logged out
    Returns:
        template for login page
    """
    user = User.query.filter_by(username=current_user.username).first()
    logout_user()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('login'))


@app.route('/reset', methods=['GET', 'POST'])
def reset_password():
    """
    If the user signals a "get" we return the template of the page for the user to update their reset page.
    If the user posts their password we match the password with the confirm password. If it matches we update the
    password in the database. Otherwise we signal to the user that passwords don't match.
    Returns:
        get - template for password change
        post- template for password change if passwords fail otherwise return user page

    """
    if request.method == 'POST':
        origin_password = request.form.get('origin')
        new_password1 = request.form.get('new_password1')
        new_password2 = request.form.get('new_password2')
        if check_password_hash(current_user.password, origin_password):
            if new_password1 == new_password2:
                current_user.password = generate_password_hash(new_password1, method='sha256')
                db.session.commit()
                flash('Password is reset!', category='succeed')
                return redirect(url_for('user_page'))
            else:
                flash('Two passwords are not matched, please try again!', category='error')
                
        else:
            flash('Origin password is wrong, please try again!', category='error')
    return render_template('change_password.html', user=current_user)


@app.route("/user", methods=['GET', 'POST'])
@login_required
def user_page():
    """
    If the user signals a "get" we return the template of the page for the user to update their user page.
    If the user posts their weight and height we update the values in the database with their new information
    Returns:
        get- template for user page
        post- template for user page with updated user values
    """
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
    """
        Renders our cardiovascular screen and checks if the user is logged in
    Returns:
        template of the cardiovascular page
    """
    return render_template("cardio.html", user=current_user)


@app.route("/Flexibility", methods=['GET', 'POST'])
def flexibility():
    """
        Renders our flexibility screen and checks if the user is logged in
    Returns:
        template of the flexibility page
    """
    return render_template("flex.html", user=current_user)


@app.route("/Strength", methods=["GET", "POST"])
def strength():
    """
        Renders our strength age and checks if the user is logged in
    Returns:
        template of our strength page
    """
    return render_template("Strength.html", user=current_user)


@app.route("/WeightLoss", methods=['GET', 'POST'])
def weightloss():
    """
        Renders our weightloss page and checks if the user is logged in
    Returns:
        template of our weightloss page
    """
    return render_template('weightloss.html', user=current_user)


@app.route("/tutorial", methods=['GET', 'POST'])
def tutorial():
    """
        gets the tutorial search template
        If the user posted cardio, flexibility or strength, the user will be redirected to the tutorial page
    Returns:
        get- template of our tutorial search page
        post - returns page of cardio, flexibility or strength page if successful
        otherwise returns tutorial search page
    """
    if request.method == "POST":
        user = request.form["nm"]
        test_link = TempLinkProxy()
        test_results = test_link.test_link(user)
        if test_results == -1:
            flash("Not a valid Workout Plan", "danger")
        if test_results == 0:
            return redirect(url_for("cardiovascular"))
        if test_results == 1:
            return redirect(url_for("flexibility"))
        if test_results == 2:
            return redirect(url_for("strength"))
        return render_template("tutorialsearch.html", user=current_user)
    else:
        return render_template("tutorialsearch.html", user=current_user)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
        if the user signals a "get" we return the template of the sign up page.
        If the user posts their info to signup correcty we add their information to the database and redirect them
        to the user page. Otherwise we return the sign up page with the error message.
    Returns:
        get - template of the sign up page
        post - template of user page
    """
    if not path.exists('fitness_database.db'):
        db.create_all(app=app)
    form = SignUpForm()
    if form.is_submitted():
        result = request.form
        username = result.get('username')
        password1 = result.get('password')
        password2 = result.get('confirm_password')
        weight = result.get('weight')
        height = result.get('height')

        methods = Appmethods()

        if not methods.confirm_password(password1, password2):
            flash('Two passwords are not matched', category='error')
        elif len(username) < 4:
            flash('Username must be at least 4 characters', category='error')
        elif len(password1) < 12:
            flash('Password must be at least 12 characters', category='error')
        else:
            try:
                new_user = User(username=username, password=generate_password_hash(password1, method='sha256'),
                                weight=weight, height=height)
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                return redirect(url_for('user_page'))
            except Exception:
                flash('User Creation Failed, please try another username!', category='error')

    return render_template('signup.html', form=form, user=current_user)


@app.route("/workout_select")
@login_required
def workout_select():
    """
        Renders our workout select page and checks if the user is logged in
    Returns:
        template of workout selector
    """
    return render_template("workout_selector.html", user=current_user)


@app.route("/flex_data")
@login_required
def flex_data():
    """
        Renders our flex data input page and checks if the user is logged in
    Returns:
        template of flex data input page
    """
    return render_template("flex_data_input.html", user=current_user)


@app.route("/flex_workout", methods=["GET", "POST"])
@login_required
def flex_workout():
    """
        if the user signals a "get" we return the template of the generated flex page.
        If the user posts workout correctly we put their workout into the database
    Returns:
        template for generated flex workout
    """
    plan_type = "flex"
    if request.method == "POST":
        methods = Appmethods()
        workout = methods.create_flex_workout(request.form)
        if workout:
            plan = Plan.query.filter_by(plan_type=plan_type).first()
            if plan:
                plan.plan = workout
                db.session.commit()
            else:
                new_plan = Plan(plan_type=plan_type, plan=workout, user_id=current_user.id)
                db.session.add(new_plan)
                db.session.commit()

    return render_template("generated_flex_workout.html", result=workout, user=current_user)


@app.route("/cardio_data")
@login_required
def cardio_data():
    """
        Renders our cardio data page and checks if the user is logged in
    Returns:
        returns template of the cardio data input
    """
    return render_template("cardio_data_input.html", user=current_user)


@app.route("/cardio_workout", methods=["GET", "POST"])
@login_required
def cardio_workout():
    """
        if the user signals a "get" we return the template of the generated cardio page.
        If the user posts workout correctly we put their workout into the database
    Returns:
        template for generated cardio workout
    """
    plan_type = "cardio"
    if request.method == "POST":
        methods = Appmethods()
        workout = methods.create_cardio_workout(request.form)
        if workout:
            plan = Plan.query.filter_by(plan_type=plan_type).first()
            if plan:
                plan.plan = workout
                db.session.commit()
            else:
                new_plan = Plan(plan_type=plan_type, plan=workout, user_id=current_user.id)
                db.session.add(new_plan)
                db.session.commit()
        return render_template("generated_cardio_workout.html", result=workout, user=current_user)


@app.route("/strength_data")
@login_required
def strength_data():
    """
        Renders our strength data page and checks if the user is logged in
    Returns:
        returns template for strength data input
    """
    return render_template("strength_data_input.html", user=current_user)


@app.route("/strength_workout", methods=["GET", "POST"])
@login_required
def strength_workout():
    """
        if the user signals a "get" we return the template of the generated cardio page.
        If the user posts workout correctly we put their workout into the database
    Returns:
        template for generated strength workout
    """
    plan_type = "strength"
    if request.method == "POST":
        methods = Appmethods()
        workout = methods.create_workout(request.form)
        if workout:
            plan = Plan.query.filter_by(plan_type=plan_type).first()
            if plan:
                plan.plan = workout
                db.session.commit()
            else:
                new_plan = Plan(plan_type=plan_type, plan=workout, user_id=current_user.id)
                db.session.add(new_plan)
                db.session.commit()
        return render_template("generated_strength_workout.html", result=workout, user=current_user)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
