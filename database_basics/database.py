from app import db
from model import Teacher, Student
import names
# db.drop_all()
# db.create_all()

# passport1 = Passport(passport_uuid=12344543, birthdplace="Tbilisi")
# passport2 = Passport(passport_uuid=15344543, birthdplace="kbilisi")
# passport3 = Passport(passport_uuid=12344343, birthdplace="Lbilisi")
# db.session.add_all([passport1, passport2, passport3])
# db.session.flush()
#
# user1 = User(username="vato", age="20", passport_id=passport1.id)
# user2 = User(username="kato", age="23", passport_id=passport2.id)
# user3 = User(username="nato", age="27", passport_id=passport3.id)
#
# db.session.add_all([user1, user2, user3])
# db.session.commit()

# creat teachers and student

# teacher1 = Teacher("ana")
# teacher2 = Teacher("giorgi")
#
# db.session.add(teacher1)
# db.session.add(teacher2)
# db.session.commit()
# students123 = []
# for _ in range(10):
#     stud = Student(names.get_first_name(), teacher_id=teacher1.id)
#     db.session.add(stud)
#     db.session.flush()
#
# for _ in range(10, 20):
#     stud = Student(names.get_first_name(), teacher_id=teacher2.id)
#     db.session.add(stud)
#     db.session.commit()

db.session.commit()
# Filters
data = Student.query.get(3)
data = Student.query.filter_by(teacher_id=2).all()
data = Student.query.filter_by(teacher_id=2).limit(2).all()
# data = Student.query.filter_by(teacher_id=2).first()
data = Student.query.filter(Student.teacher_id != 2).all()

name = [i.first_name for i in data]
print(name)

