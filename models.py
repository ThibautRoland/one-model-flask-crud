from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = 'employee_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))

    def __init__(self ,name,age,position):
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}:{self.id}"
