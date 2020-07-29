from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from models import db, connect_db, Pets
from app import app

db.drop_all()
db.create_all()

add_pet1=Pets(name='a', species='b', photo_url='www.google.com', age=2, notes='c', available=False)
add_pet2=Pets(name='d', species='e', photo_url='www.facebook.com', age=1, notes='f')
db.session.add(add_pet1)
db.session.add(add_pet2)
        
db.session.commit()