from jinja2 import Template
name="Shivani"  #products.txt
place="Mumbai"
#step1

#base.html
temp= """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>Document</title>
        </head>
        <body>
            <h2>My name is {{name}}</h2>
            <h2>I live in {{place}}</h2>
        </body>
        </html>
        """  

#step2
made_temp= Template(temp)

#step3
out= made_temp.render(name=name,place=place)#x=8
print(out)
#output.html