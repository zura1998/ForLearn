from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(124))
    age = db.Column(db.Integer, default=0)

    def create(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def delete_from_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def get_by_name(self, name):
        return self.query.filter_by(name=name)






