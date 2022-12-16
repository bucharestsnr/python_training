'''
t = 'thirty'
d = 'days'
o = 'of'
p = 'python'
space = ' '
total = t + space + d + space + o + space + p
print(total)
'''
#company = "Coding For All"
#substring = 
#print("".join(word[0] for word in company.upper().split()))

#company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
#print(company.split(","))
'''
#company = "Coding For All People"
#print(company.index("F"))
#print(company.index("C"))
#print(company.rfind("l"))

#sent = 'You cannot end a sentence with because because because is a conjunction'
#print(sent[31:54])
'''
#company = "Coding For All"
#substring = "coding"
#print(company.index(substring))

#company = '   Coding For All      '
#print(company.strip())

#company = '30DaysOfPython'
#print(company.isidentifier())

#company = 'thirty_days_of_python'
#print(company.isidentifier())

#python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
#result = " #".join(python_libraries)
#print(result)


#print("I am enjoying this challenge.\nI just wonder what is next.")

#print('Name\tAge\tCountry\tCity')
#print('Ade\t23\tNigeria\tIbadan')
'''
radius = 10
area = 3.14 * radius ** 2
formated_string = 'The area of a circle with radius {} is {} meters square.'.format(radius,area)
print(formated_string)

formatted_string = 'The area of a circle with radius %d is %.2f meters square.' %(radius, area)
print(formatted_string)

a = 8
b = 6
print('{} + {} = {}'.format(a , b , a+b))
print('{} - {} = {}'.format(a , b , a-b))
print('{} * {} = {}'.format(a , b , a*b))
print('{} / {} = {}'.format(a , b , a/b))
print('{} % {} = {}'.format(a , b , a%b))
print('{} // {} = {}'.format(a , b , a//b))
print('{} ** {} = {}'.format(a , b , a**b))
'''

a = 8
b = 6
print(f'{a} + {b} = {a+b}')
print(f'{a} - {b} = {a-b}')
print(f'{a} * {b} = {a*b}')
print(f'{a} / {b} = {a/b}')
print(f'{a} % {b} = {a%b}')
print(f'{a} // {b} = {a//b}')
print(f'{a} ** {b} = {a**b}')
