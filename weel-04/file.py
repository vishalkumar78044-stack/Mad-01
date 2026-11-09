# from flask import Flask

# app = Flask(__name__)

# @app.route("/")

# def Home():
#     return "hello inhimanal fighter"

# @app.route("/about")
# def about():
#     return "this is about page"

# @app.route("/users")
# def users():
#     return "this is all about user datas"

# @app.route("/user/<int:a>/<int:b>")
# def user(a,b):
#     return f"hello {a+b}"

# @app.route("/student/<name>/<course>")
# def student(name,course):
#     return f"{name} is learning {course}"

# @app.route("/data/<float:a>/<float:b>")
# def data(a,b):
#     return f"{a+b}"

# if __name__ == "__main__":
#     app.run(debug = True)


from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def Home():
    return "hello vishal"

@app.route("/greet")
def greet():
    name = request.args.get("name","Guest")
    course = request.args.get("course","para_cali")
    return f"kyaa hall {name} kaisa chal raha hai {course}"



if __name__ == "__main__":
    app.run(debug = True)