from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=["GET","POST"])
def form():
    
    if request.method == "POST":
        name = request.form.get("name")
        clas = request.args.get("class")
        print(clas)
        Email = request.form.get("Email")
        message = request.form.get("message")
        return render_template("greet.html",name = name,clas = clas,Email=Email,message=message)
    else:
        return render_template("form.html")

@app.route("/search")
def search():
    name = request.args.get("query")
    return f"you search for : {name}"

if __name__ == "__main__":
    app.run(debug = True)