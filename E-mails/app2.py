from flask import Flask ,render_template ,request ,redirect ,url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
db = SQLAlchemy(app)

class employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/')
def home():
    db.create_all()
    datas = employee.query.all()

    if datas :
        return render_template("home.html",datas = datas)
    else :
        return render_template("add.html")

@app.route("/add",methods=["POST","GET"])
def add():
    if request.method == "POST":
        print(request.method)
        name = request.form.get("name")
        email = request.form.get("email")
        a = employee(name=name,email=email)
        db.session.add(a)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("add.html")

@app.route("/edit/<int:id>",methods=["POST","GET"])
def edit(id):
    datas = employee.query.get(id)
    print(request.method)
    if request.method == "POST":
        datas.name = request.form.get("name")
        datas.email = request.form.get("email")
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("edit.html",datas=datas)

@app.route("/delete/<int:id>",methods=["POST","GET"])
def delete(id):
    datas = employee.query.get(id)
    if request.method == "POST":
        
        btn = request.form.get('act')
        if btn == "cancle":
            return redirect(url_for('home'))
        if btn == "delete":
            db.session.delete(datas)
            db.session.commit()
            return redirect(url_for('home'))
    else:
        return render_template("delete.html",datas=datas)

            






if __name__ == "__main__":
    app.run(debug=True)

