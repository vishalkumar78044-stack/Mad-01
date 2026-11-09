from jinja2 import Template

# lis = ["anushka","janhvi","anshika","ahole mkd"]

tem = Template("""my lovers list is here:
        <ul>
            <li>
            {%for i in ll%}
                {{i}}
            {%endfor%}
            </li>
        </ul>}""")

ren = tem.render(ll = ["anushka","janhvi","anshika","ahole mkd","jira"])
print(ren)

data = {
    "student_name": "  alice smith  ",
    "is_enrolled": True,
    "courses": [
        {"code": "BT1010", "name": "Life Sciences", "marks": 78},
        {"code": "MA1020", "name": "Calculus", "marks": 35},
        {"code": "EE1001", "name": "Electrical Engg", "marks": 43},
        {"code": "EE1001", "name": "Electrical Engg", "marks": 43}  # Duplicate entry
    ],
    "raw_bio": "<b>Enthusiastic</b> student & programmer.",
    "gpa": 3.678,
    "empty_notes": None
}
#mvc
