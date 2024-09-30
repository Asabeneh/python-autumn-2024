def add_two_nums(x, y):
    return x + y

print(add_two_nums('3', '4'))
print(add_two_nums(-3, -97))



def multiply_two_nums(x, y):
    return x * y
print(multiply_two_nums('love', 3))
print(multiply_two_nums(100, 30))


def linear_equation(x, y, k):
    return 2 * x - y * + k

# 2x - 4y + 10
print(linear_equation(2, 4, 10))
'''
Function without a parameter
Funtion with one parameter
Function with two more more paramters
Funtions with unlimited number of parameters
'''
def sum_all_nums(*params):
    total = 0
    for num in params:
        total = total + num
    return total


print(sum_all_nums(1, 2, 3, 4, 5, -15))

def sum_all_nums(*params):
    return sum(params)


print(sum_all_nums(1, 2, 3, 4, 5, -15))
n = 1000
print('value of outsite the function:', n)
def make_square(n):
    print(n)
    return n ** 2

print(make_square(10))

# gravity = 9.81 
def calculate_weight (mass, gravity = 9.81):
    return mass * gravity 

print(calculate_weight(74.5))
print(calculate_weight(74.5, 1.62))
print(calculate_weight(74.5, 3.71))
print(calculate_weight(68))

def do_something(name, width, height, age, color):
    return f'{name} {width} {height} {age} {color}'

print(do_something(age = 250, width = 45, height=1.72, name = 'Asabeneh', color='Brown'))

def is_even (n):
    return n % 2 == 0
   


print(is_even(0))
print(is_even(2))
print(is_even(20))
print(is_even(3))

def filter_evens(lst):
    new_lst = []
    for num in lst:
        if num % 2 == 0:
            new_lst.append(num)
    return new_lst

nums = [-6, 0, 5, 2, 7, -4]
print(filter_evens(nums))


def filter_positive_evens(lst):
    new_lst = []
    for num in lst:
        if num % 2 == 0 and num < 0:
            new_lst.append(num)
    return new_lst

print(filter_positive_evens(nums))

def generate_groups (team,country,*args):
    print(team, args)
    for i in args:
        print(i)
print(generate_groups('Team-1','Finland', 'Asabeneh','Brook','David','Eyob', 'Kimmo','Lauri','Pullo'))

def xyz (x, **kwargs):
    print(x, kwargs)

xyz('xyz - ??', name ='Asab', age = 250, county = 'Finland', is_married = True, title = 'Developer')
