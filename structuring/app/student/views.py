from flask import url_for, render_template, redirect, Blueprint
from app.models import Student
from app.student.forms import Delform, LoginForm

students_blueprint = Blueprint("students", __name__, template_folder='templates/students')

@students_blueprint.route("/")
def home():
    return render_template("home.html")


@students_blueprint.route("/add", methods=["GET", "POST"])
def add():
    myform = LoginForm()
    if myform.validate_on_submit():
        name = myform.login.data
        email = myform.email.data
        password = myform.password.data
        new_stu = Student(name, email, password)
        new_stu.post_to_db()
        return redirect(url_for("stu_list"))
    return render_template("add_form.html", form=myform)


@students_blueprint.route("/stu")
def stu_list():
    students = Student.query.all()
    return render_template("stu_list.html", students=students)


@students_blueprint.route("/delete", methods=['GET', 'POST'])
def delete():

    myform = DelForm()
    print(myform.validate_on_submit())
    if myform.validate_on_submit():
        # name = myform.name.data
        id = myform.id.data
        del_stu = Student.query.get(id)
        # del_stu = Student.query.filter_by(name=name)
        print(del_stu)
        db.session.delete(del_stu)
        db.session.commit()
        return redirect(url_for("stu_list"))

    return render_template("delete.html", form=myform)
