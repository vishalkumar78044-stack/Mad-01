from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///User.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/create_tables')
def create_tables():
    db.create_all()
    return "table created successfully"

@app.route('/')
def home():
    return "welcome to database"

@app.route('/add_user/<username>/<email>')
def add_user(username,email):
    a = User(username=username,email=email)
    db.session.add(a)
    db.session.commit()
    return f'user {username} added successfully !'

@app.route('/get_user/<username>')
def get_user(username):
    a = User.query.filter_by(username=username).first()
    if a:
        return f"user found: {a.username}, {a.email}"
    else:
        return "user not found"



@app.route('/update_user/<username>/<new_email>')
def update_user(username,new_email):
    a = User.query.filter_by(username=username).first()
    if a:
        a.email = new_email
        db.session.commit()
        return f'user {username} updated successfully ! wow'
    else:
        return "user not found"


@app.route("/delete_user/<username>")
def delete_user(username):
    a = User.query.filter_by(username=username).first()
    if a:
        db.session.delete(a)
        db.session.commit()
        return f'user {username} deleted successfully ! wow'
    else:
        return "user not found"

if __name__ == '__main__':
    app.run(debug=True)

