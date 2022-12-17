
sisters = ('Lara', 'Teni')
brothers = ('Niyi', 'Bayo')
siblings = sisters + brothers
#print(len(siblings))
family_members = list(siblings)
family_members.insert(0, 'Kunle')
family_members.insert(1, 'Bola')
family_members = tuple(family_members)
#print(family_members)


#Exercise 2
father, mother, sibling1, sibling2, sibling3, sibling4 = family_members
#print(sibling4)

fruits = ('banana', 'apple', 'lemon', 'orange')
vegetables = ('lettuce', 'spinach', 'jute')
animal_products = ('fertilizer', 'rum',)
food_stuff_tp = fruits + vegetables + animal_products
#print(food_stuff_tp)
food_stuff_tp = list(food_stuff_tp)
#print(len(food_stuff_tp))
#print(food_stuff_tp[4])
#print(food_stuff_tp[6:9])
del food_stuff_tp
#print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
print('Nigeria' in nordic_countries)
