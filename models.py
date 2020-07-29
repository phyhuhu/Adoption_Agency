"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()

def connect_db(app):
    db.app=app
    db.init_app(app)

class Pets(db.Model):
    __tablename__='pets'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String, nullable=False)
    species=db.Column(db.String, nullable=False)
    photo_url =db.Column(db.String, nullable=True)
    age =db.Column(db.String, nullable=True)
    notes =db.Column(db.String, nullable=True)
    available =db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"<Pets: {self.id} {self.name} {self.species}>"