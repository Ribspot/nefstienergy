from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

#id,name,email,phone,message,datasent
class User(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    fullname = db.Column(db.String(255), nullable=False)
    username= db.Column(db.String(100), nullable=False)
    phone_number= db.Column(db.String(100), nullable=True)
    email= db.Column(db.String(255), nullable=False)
    user_pwd=db.Column(db.String(120),nullable=True)
    address=db.Column(db.String(120),nullable=True)
    user_pix=db.Column(db.String(120),nullable=True) 

    datesent= db.Column(db.DateTime(), default=datetime.utcnow)
class Contact(db.Model):
    user_id = db.Column(db.Integer(), primary_key=True,autoincrement=True)
    firstname = db.Column(db.String(255), nullable=False)
    lastname= db.Column(db.String(100), nullable=False)
    phone= db.Column(db.String(100), nullable=True)
    email= db.Column(db.String(255), nullable=False)
  
    address=db.Column(db.String(120),nullable=True)
    services=db.Column(db.String(120),nullable=True)
    state=db.Column(db.String(120),nullable=True)
    city=db.Column(db.String(120),nullable=True)

    datesent= db.Column(db.DateTime(), default=datetime.utcnow)
class State(db.Model):
    state_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    state_name = db.Column(db.String(255), nullable=False)
class Service(db.Model):
    service_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    service_name = db.Column(db.String(255), nullable=False)