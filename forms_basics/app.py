from flask import Flask, render_template, session, redirect, url_for, flash
import os
from forms import LoginForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"


@app.route("/")
def home():
    return "<h1> Holla </h1>"


@app.route("/sign", methods=['GET', 'POST'])
def login():
    myform = LoginForm()

    if myform.validate_on_submit():
        login = myform.login.data
        password = myform.password.data
        email = myform.email.data
        gender = myform.gender.data
        print(login, password, email, gender)
        session['gender'] = gender
        flash("SUCCEs")
        myform.fileupload.data.save("uploads/file.png")
        return redirect(url_for("success"))
    # myform.fileupload.save("../uploads/file.png")

    # errors = [myform.login.errors, myform.confirmpassword.errors]
    # if errors:
    #     for error in errors:
    #         flash(error)

    return render_template("home.html", form=myform)


@app.route("/success")
def success():
    print("gaa")
    return render_template("success.html")



if __name__ == "__main__":
    app.run(debug=True)