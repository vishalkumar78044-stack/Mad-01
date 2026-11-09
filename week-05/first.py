from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DATA.db"

db = SQLAlchemy(app)

class student(db.Model):
    name = db.Column(db.String(80),nullable=False )
    classes = db.Column(db.Integer,nullable=False)
    i_d = db.Column(db.Integer,primary_key=True)
    def __repr__(self):
        return f'<student {self.name}>'

with app.app_context():
    db.create_all()
    a = student(name="vishal",classes=12)
    db.session.add(a)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)








