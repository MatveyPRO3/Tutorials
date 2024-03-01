from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import re

HEX_color_format = r"^#(?:[0-9a-fA-F]{3}){1,2}$"


app = Flask(__name__)
app.secret_key = "password_:D"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=5)


db = SQLAlchemy(app)


class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    color = db.Column(db.String(100))

    def __init__(self, name, email, color) -> None:
        self.email = email
        self.name = name
        self.color = color


@app.route("/")
def home():
    if "color" in session:
        color = session["color"]
    else:
        color = "#f8f9fa"
    return render_template("home.html", color=color)


@app.route("/view")
def view():
    if "color" in session:
        color = session["color"]
    else:
        color = "#f8f9fa"
    if "user" in session:
        user = session["user"]
    else:
        user = None
    return render_template("view.html", values=users.query.all(), you=user, color=color)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        if "email" in session:
            session.pop("email", None)
        if "color" in session:
            session.pop("color", None)

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["email"] = found_user.email
            session["color"] = found_user.color
        else:
            usr = users(user, "None", "#f8f9fa")
            db.session.add(usr)
            db.session.commit()

        flash("You have been logged in successfully!", "info")
        return redirect(url_for("user"))
    else:
        if "color" in session:
            color = session["color"]
        else:
            color = "#f8f9fa"
        return render_template("login.html", color=color)


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        if request.method == "POST":
            flash("Email was saved!", "info")
            email = request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email = email
            db.session.commit()
        else:
            if "email" in session:
                email = session["email"]
        if "color" in session:
            color = session["color"]
        else:
            color = "#f8f9fa"
        return render_template("user.html", name=session["user"], email=email, color=color)
    else:
        flash("You are not logged in!", "error")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "user" in session:
        session.pop("user", None)
        session.pop("email", None)
        session.pop("color", None)
        flash("You have been logged out successfully!", "info")
        return redirect(url_for("login"))
    else:
        flash("You are not logged in!", "error")

    return redirect(url_for("login"))


@app.route("/remove_user")
def remove_user():

    if not "user" in session:
        flash("You are not logged in!", "error")
        return redirect(url_for("login"))
    else:
        user = session["user"]
        flash(f"User {user} was successfully removed from database!", "info")

        # removing user
        users.query.filter_by(name=user).delete()
        db.session.commit()
        session.pop("user", None)
        session.pop("email", None)
        session.pop("color", None)

        return redirect(url_for("view"))


@app.route("/test")
def test():
    if "color" in session:
        color = session["color"]
    else:
        color = "#f8f9fa"
    return render_template("test.html", color=color)


@app.route("/test2")
def test2():
    return render_template("test2.html")


@app.route("/cup")
def cup():
    if "color" in session:
        color = session["color"]
    else:
        color = "#f8f9fa"
    return render_template("cup.html", color=color)


@app.route("/cube")
def cube():
    if "color" in session:
        color = session["color"]
    else:
        color = "#f8f9fa"
    return render_template("cube.html", color=color)


@app.route("/changecolor", methods=["POST"])
def changecolor():
    if "user" not in session:
        flash("You are not logged in!", "error")
        return redirect(url_for("login"))
    else:
        user = session["user"]
    color = request.form["color"]
    match = re.search(HEX_color_format, color)
    if match:
        flash("Color has been updated!", "info")
        session["color"] = color
        found_user = users.query.filter_by(name=user).first()
        found_user.color = color
        db.session.commit()
    else:
        flash("Color format is invalid!", "error")
    return redirect(url_for("user"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
