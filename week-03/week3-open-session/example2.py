from jinja2 import Template
sub="MAD 2"
temp="""
      {% if "1" in sub %}
          The course has id 1
      {% elif "2" in sub %}
          The course has id 2
      {% else %}
          The course is not valid
      {% endif %}
"""

made_temp=Template(temp)
output=made_temp.render(sub=sub)
print(output)