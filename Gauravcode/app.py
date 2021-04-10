
from flask import Flask, redirect, url_for, render_template,flash
from tutorialsearch import RegistrationForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route("/")
def hello():
    return render_template('template.html')

#@app.route("/home")
#def home():
#    return render_template('home.html', posts=posts)


#@app.route("/about")
#def about():
#    return render_template('about.html', title='About')


@app.route("/tutorial", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    #if form.validate_on_submit():
    #    flash(f'Account created for {form.username.data}!', 'success')
    #    return redirect(url_for('about'))
    return render_template('tutorialsearch.html', title='Tutorial', form=form)


#@app.route("/login", methods=['GET', 'POST'])
#def login():
#    form = LoginForm()
#    if form.validate_on_submit():
#        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
#            flash('You have been logged in!', 'success')
#            return redirect(url_for('home'))
#        else:
#            flash('Login Unsuccessful. Please check username and password', 'danger')
#    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)


#@app.route("/<name>")
#def user(name):
#    return f"Hello {name}!"

#@app.route("/admin")
#def admin():
#    return redirect(url_for("user", name = "Admin!"))


if __name__ == "__main__":
    app.run()
