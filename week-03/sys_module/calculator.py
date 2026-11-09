import sys
sys.path.append(r"C:\Users\VISHAL KUMAR\Downloads\Programmer\mad01\week-03\sys_module\helper")
import helper

if len(sys.argv) < 4:
    print("Enter valid input")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
operator = str(sys.argv[2])

if operator == "+":
    print(helper.add(a,b))

if operator == "-":
    print(helper.sub(a,b))

if operator == "*":
    print(helper.mul(a,b))

if operator == "/":
    print(helper.div(a,b))

if operator == "%":
    print(helper.mod(a,b))

