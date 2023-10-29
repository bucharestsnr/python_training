'''
(1)
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

(2)
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

(3)
def add_two_nums(a,b):
    total = a + b
    return total
print(add_two_nums(3,5))

(4)
def area_of_circle(r):
    pi = 3.142
    area = (pi * r ** 2)
    return area
    #print(area)
print(area_of_circle(5))

(5)
def add_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(add_all_nums(10,5,9))

(6)
def convert_celsius_to_fahrenheit(C):
    F = (C * 9/5) + 32
    return F
print(convert_celsius_to_fahrenheit(50))

(7)
def check_season(month):
    if month == "March"  or month == "April" or month == "May":
        print("Spring")
    elif month == month == "June" or month == "July" or month == "August":
        print("Summer")
    elif month == "September" or month == "October" or month == "November":
        print("Autumn")
    else:
        print("Winter")
check_season("July")

(8)
def calculate_slope():
    m = int(input("Enter slope: "))
    c = int(input("Enter y-intercept: "))
    return m
print(calculate_slope())

(9a)
def solve_quadratic_eqn():
    a = int(input("Enter the coefficient of x2: "))
    b = int(input("Enter the coefficient of x: "))
    c = int(input("Enter the constant: "))
    x1 = (-b + (b**2 - 4 * a * c)**0.5) / 2 * a
    x2 = (-b - (b**2 - 4 * a * c)**0.5) / 2 * a
    return x1, x2
print(solve_quadratic_eqn())

(9b)
def solve_quadratic_eqn(a, b, c):
    x1 = (-b + (b**2 - 4 * a * c)**0.5) / 2 * a
    x2 = (-b - (b**2 - 4 * a * c)**0.5) / 2 * a
    return x1, x2
print(solve_quadratic_eqn(1, 5, 6))

(10)
def print_list(players):
    players = ['Ramsdale', 'White', 'Saliba', 'Gabriel', 'Zinchenko']
    for i in range (0, len(players)):
        print(players[i])
print_list('Ramsdale')

(11a)
def reverse_list():
    myList = [1, 2, 3, 4, 5]
    print(myList[::-1])
reverse_list()

(11b)
def reverse_list():
    myList = ['A', 'B', 'C', 'D', 'E']
    print(myList[::-1])
reverse_list()

def capitalize_list_item():
    myList = ['boy', 'cat', 'doll']
    for i in range(len(myList)):
        myList[i] = myList[i].upper()
    print(myList)
capitalize_list_item()

def add_item(*arg):
    fruits_list = ['Avocado', 'Pear', 'Mango', 'Apple']
    fruits_list.append('Banana')
    print(fruits_list)
add_item()

def remove_item(*arg):
    food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
    food_staff.remove('Tomato')
    print(food_staff)
remove_item()

#sum of all numbers in a range
def sum_of_numbers(num):
    b = sum(range(num + 1))
    return b
print(sum_of_numbers(100))

#sum of even numbers in a range
def sum_of_odd(num):
    b = sum(range(1,num + 1, 2))
    return b
print(sum_of_odd(50)) 

#sum of odd numbers in a range
def sum_of_odd(num):
    b = sum(range(0,num + 1, 2))
    return b
print(sum_of_odd(50))

def evens_and_odds(num):
    even_count = 0
    odd_count = 0
    for i in num:
        if i % 2 == 0:
            even_count += 1
    for i in num:
        if i % 2 == 1:
            odd_count += 1
print(evens_and_odds(10))
'''
#prime number
# def is_prime(num):
#     for i in range(2, num):
#         if (num % i) == 0:
#             return (num, "is not a prime number")
#     return (num, "is a prime number")
# print(is_prime(15))

