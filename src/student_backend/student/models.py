from flask_sqlalchemy import SQLAlchemy

from src.student_backend.utils.defaults import default_id

db = SQLAlchemy()


class Student(db.Model):
    """model for student"""
    __tablename__ = "student"

    id = db.Column(db.String(50), primary_key=True, default=default_id(), index=True)
    name = db.Column(db.String(50), nullable=False)

    class_id = db.Column(db.String(50), index=True)
    # class_tb = db.relationship9 backref="class")

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=True)


class ClassTb(db.Model):
    """model for class"""
    __tablename__ = "class"

    id = db.Column(db.String(50), primary_key=True, default=default_id(), index=True)
    name = db.Column(db.String(50), nullable=False)

    class_leader = db.Column(db.String(50), db.ForeignKey(Student.id), index=True)
    # student = db.Column(Student, backref="student")

    created_on = db.Column(db.DateTime, default=db.func.now())
    updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=True)
