it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#it_companies2 = {'Multisonic', 'Nimbles', 'Solarlink'}

#print(len(it_companies))
#it_companies.add('Twitter')
#print(it_companies)
#it_companies.update(it_companies2)
#print(it_companies)

it_companies.remove('Google')
#print(it_companies)

#Exercise 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#print(A.union(B))
#A.update(B)
#print(A)
#print(A.intersection(B))
#print(A.issubset(B))
#print(A.isdisjoint(B))
#print(A.union(B))
#print(B.union(A))
#print(A.symmetric_difference(B))
#print(B.difference(A))
#del A
#del B
#print(A)

#Exercise 3
#age = set(age)
#print(len(set(age)) == len(list(age)))

word = "I am a teacher and I love to inspire and teach people"
print(set(word.split()))
