from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(500))
    image=db.Column(db.String(500))
    price=db.Column(db.Float)

class User(db.Model, SerializerMixin):
    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(500),nullable=False)
    email=db.Column(db.String(500),nullable=False,unique=True)
    password=db.Column(db.String(500),nullable=False)