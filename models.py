
from sqlalchemy import Column, String, Date, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import os

database_name = "learning"
database_path = "postgres://{}:{}@{}/{}".format(
    "postgres", "rohit", "localhost:5432", database_name)

db = SQLAlchemy()

'''
setup_db(app)
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
Define Students class here

'''
class Students(db.Model):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)
    teacher_id = Column(Integer, db.ForeignKey('teachers.id'), nullable=False)

    def __init__(self, name, age, gender, teacher_id):
        self.name = name
        self.age = age
        self.gender = gender
        self.teacher_id = teacher_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'teacher_id': self.teacher_id
        }


'''
Define Teachers class here

'''
class Teachers(db.Model):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True)
    Name = Column(String)
    age = Column(Integer)
    students = db.relationship('Students', backref='teachers')

    def __init__(self, Name, age):
        self.Name = Name
        self.age = age

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'Name': self.Name,
            'age': self.age,
            'students': self.students
        }
