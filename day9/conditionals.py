'''
#1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive")
elif (18-age) == 1:
    print("Please wait for one more year")
else:
    print("Please wait for ", str(18-age), "more years")


#2
# my_age = int(input("How old are you: "))
your_age = int(input("How old are you: "))
if my_age > your_age:
    print("I am ", str(my_age - your_age), "years older than you")
elif my_age == your_age:
    print("No one is older between us")
else:
    print("You are ", str(your_age - my_age), " year older than me")


#3
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
if a > b:
    print(str(a), "is greater than", str(b))
elif a == b:
    print(str(a), "is equal to", str(b))
else:
    print(str(a), "is less than", str(b))


#4
grade = int(input("Enter your score: "))
if grade >= 80 and grade <= 100:
    print("Congratulations! You have A")
elif grade >= 70 and grade <= 79:
    print("Congratulations! You have B")
elif grade >= 60 and grade <= 69:
    print("Congratulations! You have C")
elif grade >= 50 and grade <= 59:
    print("Congratulations! You have D")
else:
    print("Congratulations! You have F")


#5
season = input("Enter a month: ")
if season == 'September' or season == 'October' or season == 'November':
    print(season, "is a autumn season")
elif season == 'December' or season == 'January' or season == 'February':
    print(season, "is a winter season")
elif season == 'March' or season == 'April' or season == 'May':
    print(season, "is a spring season")
else:
    print(season, "is a summer season")


#6
fruits = ['banana', 'orange', 'mango', 'lemon']
check = input('Enter a fruit name: ')
if check in fruits:
    print(check, "already exists in the list")
else:
    fruits.append(check)
    print(fruits)
'''

person = {
'first_name': 'Asabeneh',
'last_name': 'Yetayeh',
'age': 250,
'country': 'Finland',
'is_married': True,
'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
'address': {'street': 'Space street','zipcode': '02210'}
}

#if "skills" in person.keys():
    #print(person["skills"][2])


if "skills" in person.keys():
    if "Python" in person["skills"]:
        print("Python")

""" if person['skills'][0] == 'JavaScript' and person['skills'][1] == 'React':
    print('He is a front end developer')

elif person['skills'][2] == 'Node' and person['skills'][3] == 'MongoDB' and person['skills'][4] == 'Python':
    print('He is a backend developer')

elif person['skills'][1] == 'React' and person['skills'][2] == 'Node' and person['skills'][3] == 'MongoDB':
    print('He is a fullstack developer')

else:
    print('Unknown title')"""

#, 'Node', 'MongoDB', 'Python'