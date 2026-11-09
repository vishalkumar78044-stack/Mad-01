# imports 
from flask import Flask
from datetime import date,datetime,timezone
from sqlalchemy.exc import IntegrityError

from flask_sqlalchemy import SQLAlchemy 
# integrates flask and sqlalchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
# app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
# db.init_app(app)

class User(db.Model):
    
    __tablename__ = 'users' #optional
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30),unique=True)
    section = db.Column(db.String(30))
    is_active = db.Column(db.Boolean,default=True)
    # created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    # updated_at = db.Column(db.DateTime, onupdate=datetime.now)
    
    __table_args__ = (db.UniqueConstraint('section','name',name='unique_section_name'),)
    
    def __repr__(self):
        return f'<User { user.email}>'
    

with app.app_context(): 
    db.drop_all()
    db.create_all()
    u1 = User(name="pallavi",email="p1@gmail.com",section="comp")
    u2 = User(name="pallavi1",email="p2@gmail.com",section="comp")
    # u3 = User(id=3,name="pallavi3",email="p3@gmail.com")
    
    # date(year,month,date)
    try:

        db.session.add(u1) # adding u1 object in the session 
        db.session.add(u2)
        # db.session.add(u3)
    
    
        user = db.session.get(User,1)
        print(user) # <User 1>
        
        db.session.commit() # commit the transaction , 
    except IntegrityError:
        print("Give unique username......")