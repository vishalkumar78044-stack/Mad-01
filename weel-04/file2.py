from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def Home():
    return "hello vishal"

@app.route("/greet")
def greet():
    name = request.args.get("name")
    return f"kyaa hall {name}"



if __name__ == "__main__":
    app.run(debug = True)