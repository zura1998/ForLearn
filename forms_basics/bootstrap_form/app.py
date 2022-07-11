from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

dirpath = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(dirpath, "stu.sqlite")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/add")
def add():
    return render_template("add_form.html")


@app.route("/stu")
def stu_list():
    return render_template("stu_list.html")


if __name__ == "__main__":
    app.run(debug=True)

