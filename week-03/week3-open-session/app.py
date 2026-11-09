from jinja2 import Template
Products = [
  {'product_id':'101', 'prod_name':'Legion', 'type':'Laptop', 'producer':'Lenovo'},
  {'product_id':'102', 'prod_name':'S21pro', 'type':'Cellphone', 'producer':'Samsung'},
  {'product_id':'104', 'prod_name':'TabA7', 'type':'Tablet', 'producer':'Samsung'},
  {'product_id':'105', 'prod_name':'Ideapad', 'type':'Laptop', 'producer':'Lenovo'},
  {'product_id':'106', 'prod_name':'iPad', 'type':'Tablet', 'producer':'Apple'},
  {'product_id':'103', 'prod_name':'iPhone13', 'type':'Cellphone', 'producer':'Apple'},
  {'product_id':'107', 'prod_name':'NoteA7', 'type':'Cellphone', 'producer':'Xiaomi'},
  {'product_id':'108', 'prod_name':'Tab4', 'type':'Tablet', 'producer':'Lenovo'},
  {'product_id':'109', 'prod_name':'Macbook', 'type':'Laptop', 'producer':'Apple'},
  {'product_id':'110', 'prod_name':'miNotebook', 'type':'Laptop', 'producer':'Xiaomi'},
  {'product_id':'111', 'prod_name':'M21', 'type':'Cellphone', 'producer':'Samsung'},
  {'product_id':'112', 'prod_name':'A7000', 'type':'Cellphone', 'producer':'Lenovo'}  
]

# {"Anu","Mumbai"}
# {"Ayush","Mumbai"}
# {"Harsh","Delhi"}
# {"Bhumika","Delhi"}

#step 1
File = open('base.html','r')#reading the base.html file
temp = File.read()#reading/storing the content of base.html file
File.close()
print(temp)

#step2
made_temp= Template(temp)#creating a template object

#step3
output = made_temp.render(Products=Products) #rendering the template with the data
#x=8
# print(output)

#step4
File = open("output.html","w")#writing the output to output.html file
File.write(output)
File.close()

     
      



