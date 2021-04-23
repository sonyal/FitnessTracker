
from flask import Flask, redirect, url_for, render_template,flash, request
from tutorialsearch import RegistrationForm, TestLinkProxy
from forms import SignUpForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from os import path

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

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(50))
    weight = db.Column(db.String(30))
    height = db.Column(db.String(30))
    
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

@app.route("/Cardiovascular", methods=['GET', 'POST'])
def cardiovascular():
    return render_template('cardio.html')

@app.route("/Flexibility", methods=['GET', 'POST'])
def flexibility():
    return render_template('flex.html')


@app.route("/Strength", methods=['GET', 'POST'])
def strength():
    return render_template('Strength.html')


@app.route("/tutorial", methods=['GET', 'POST'])
def tutorial():
    if request.method == "POST":
        user = request.form["nm"]
        test_link = TestLinkProxy()
        test_results = test_link.test_link(user)
        if test_results == -1 :
            flash("Not a valid Workout Plan", "danger")
        if test_results == 0:
            return redirect(url_for("cardiovascular"))
        if test_results == 1:
            return redirect(url_for("flexibility"))
        if test_results == 2:
            return redirect(url_for("strength"))
        return render_template('tutorialsearch.html')
    else:
        return render_template('tutorialsearch.html')


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

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run()
