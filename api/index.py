from flask import Flask, render_template, request
from datetime import date

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

@app.route("/", methods=["GET", "POST"])
def age_calculator():
    age = None
    if request.method == "POST":
        year = int(request.form["year"])
        month = int(request.form["month"])
        day = int(request.form["day"])

        today = date.today()
        age = today.year - year
        if (today.month, today.day) < (month, day):
            age -= 1

    return render_template("index.html", age=age)

# Required for Vercel
app = app
