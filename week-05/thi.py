from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///std.db"
db = SQLAlchemy(app)

class Student2(db.Model):
    name = db.Column(db.String(50),nullable=False)
    i_d = db.Column(db.Integer,nullable=False,primary_key=True)
    def __repr__(self):
        return f"<Student2 {self.name}>"

with app.app_context():
    db.create_all()
    temp = Student2.query.filter_by(name='vishal').all()

    if temp == 0:
        a = Student2(name="vishal")
        db.session.add(a)
        db.session.commit()
    else:
        print(temp)
  

if __name__ == "__main__":
    app.run(debug=True)


