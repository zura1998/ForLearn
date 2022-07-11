from app import db


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=False)
#     age = db.Column(db.Integer)
#     passport_id = db.Column(db.Integer, db.ForeignKey("passport.id"))
#
#
# class Passport(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     passport_uuid = db.Column(db.Integer)
#     birthdplace = db.Column(db.String)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    students = db.relationship("Student", bakhref="teacher1")

    def __init__(self, first_name):
        self.first_name = first_name


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    teacher_id = db.Column(db.Integer,db.ForeignKey("teacher.id"))

    def __init__(self, first_name, teacher_id):
        self.first_name = first_name
        self.teacher_id = teacher_id







