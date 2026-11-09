# code - 01

# from flask import Flask

# app = Flask(__name__)
# @app.route("/")

# @app.route("/home")
# def home():
#     return "vishal......"

# if __name__ == "__main__":
#     app.run(debug=True)




# code - 02

# from flask import Flask

# app = Flask(__name__)

# @app.route('/home')
# @app.route('/work')
# def my_task():
#     return "<h1>Hello! Reporting for my task</h1>"

# app.run()




# code -03

from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Mad-I welcomes you!'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context('/user?name=vishal'):
    print(request.args.get('name'))
    print(url_for('profile',username="vishal",next='courst'))
    print(request.path)

@app.route('/employee', methods = ['GET', 'POST'])
def show_details():
    det = request.args
    details = {
                'Department': det['dept'],
                'Id': det['id'],
                'Profession': det['prof']
            }
    return details

class Student:
    idnext = 0

    def __init__(self, name):
        self.name = name
        self.idnext = Student.idnext
        Student.idnext = Student.idnext + 1

s1 = Student("Rohan")
s2 = Student("Karthik")
s3 = Student("Saurav")

print(Student.idnext)

if __name__ == '__main__':
    app.run(debug=True)



