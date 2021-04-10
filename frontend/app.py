
from flask import Flask, redirect, url_for, render_template,flash, request
from tutorialsearch import RegistrationForm, TestLinkProxy
app = Flask(__name__)

app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
def home():
    return render_template('index.html')


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


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run()
