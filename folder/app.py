from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import names

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    students = db.relationship("Student", backref="subject", lazy=True)
    teacher = db.relationship("Teacher", backref="subject", lazy=True, uselist=False)

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return f" {self.title} created"


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)

    def __init__(self, first_name, last_name, subject_id):
        self.first_name = first_name
        self.last_name = last_name
        self.subject_id = subject_id


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey("subject.id"), nullable=False)

    def __init__(self, first_name, last_name, subject_id):
        self.first_name = first_name
        self.last_name = last_name
        self.subject_id = subject_id


if not os.path.isfile("../database.db"):
    # Created a database if it does not exist and added records
    db.create_all()

students = []
# Subjects
subject1 = Subject("History")
subject2 = Subject("Math")
db.session.add(subject2)
db.session.add(subject1)
db.session.commit()
# History teacher
teacher1 = Teacher("ana", "nikoleishvili", 1)
#  Math teacher
teacher2 = Teacher("giorgi", "lemonjava", 2)
db.session.add(teacher1)
db.session.add(teacher2)
db.session.commit()
for i in range(4):
    student = Student(names.get_first_name(), names.get_last_name(), 1)
    db.session.add(student)
    db.session.commit()
    students.append(student)
for i in range(4, 10):
    student = Student(names.get_first_name(), names.get_last_name(), 2)
    db.session.add(student)
    db.session.commit()
    students.append(student)

print(students)
students_names = [i.first_name + " " + i.last_name for i in students]
print(students_names)


@app.route("/", methods=["GET"])
def data():
    data = Subject.query.all()
    data_dict = {"subjects":
        [
            {"title": data[0].title,
             "teacher": data[0].teacher.first_name + " " + data[0].teacher.last_name,
             "students": students_names[:4]
             },

            {"title": data[1].title,
             "teacher": data[1].teacher.first_name + " " + data[1].teacher.last_name,
             "students": students_names[4:]
             },
        ]
    }
    return data_dict


# ,methods=["GET", "POST"]
data_one = Subject.query.all()
# print(data[0].students)
# print(data[1].students)
print(data_one)

if __name__ == "__main__":
    app.run(debug=True)
