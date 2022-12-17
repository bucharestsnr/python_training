dog = {'name': 'Bruno' , 'color':'brown', 'leg':4, 'age': 3}
#print(dog)

student = {
'first_name':'Ade',
'last_name':'Adenrele',
'gender': 'M',
'age':24 ,
'marital_status':'married',
'skills':['HTML', 'CSS', 'Java', 'JS'],
'country':'Nigeria',
'city':'Ibadan',
'address' : 'Akobo'
}
#print(len(student))
#print(type(student.get('skills')))
student['skills'].append('Python')
student['skills'].append('Node')
#print(student)
keys = student.keys()
#print(keys)
values = student.values()
#print(values)
#print(student.items())
del student['address']
#print(student)

del dog
print(dog)
