from flask import Flask ,render_template ,request ,redirect ,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logins.db'
db = SQLAlchemy(app)

class logins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80),unique=False,nullable=False)

@app.route("/",methods=["POST","GET"])
def home():
    db.create_all()
    if request.method == "POST":
        info = request.form.get("info")
        if info == "signin":
            return redirect(url_for('signin'))
        if info == "login":
            return redirect(url_for('login'))  
    

    return render_template("wel.html")


    

@app.route("/signin",methods=["POST","GET"])
def signin():
    print(request.method)
    if request.method == "POST":
        print(request.method)
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        a = logins(name=name,email=email,password=password)
        db.session.add(a)
        db.session.commit()
        return render_template("greet.html",name=name,email=email)
    else:
        return render_template("signin.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        print("helllllo vis")
        print(request.method)
        password = request.form.get("password")
        email = request.form.get("email")
        user = logins.query.filter_by(email = email).first()
        if password == user.password:
            return render_template("greet.html",name=user.name)
        else:
            return f'incorrect password'
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)