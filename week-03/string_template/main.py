from string import Template

names = ["vishal","anushka","rahul","sindhu"]

for name in names:
    a = "my name is $name"
    template = Template(a)
    print(template.substitute(name=name))