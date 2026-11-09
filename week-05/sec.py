from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///study.db"
db = SQLAlchemy(app)

class Employee(db.Model):
    name = db.Column(db.String(50),nullable=False)
    i_d = db.Column(db.Integer,primary_key=True)
    salery = db.Column(db.Float,nullable=False)
    def __repr__(self):
        return f'<Employee {self.name}>'

with app.app_context():
    db.create_all()
    a = Employee(name='vishal',salery=1200.00)
    db.session.add(a)
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)


