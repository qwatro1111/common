from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


student_teacher = db.Table(
    'student_teacher',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id')),
    db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
)

class School(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    students = db.relationship('Student', backref='students')
    teacher = db.relationship('Teacher', backref='teacher')

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    diary = db.relationship('Diary', backref='student', uselist=False)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    school_id = db.Column(db.Integer, db.ForeignKey('school.id'), nullable=False)
    students = db.relationship('Student', secondary=student_teacher, backref=db.backref('teachers'))


class Diary(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
