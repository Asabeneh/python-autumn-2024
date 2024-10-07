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


# Lambda functions

square = lambda x : x ** 2
print(square(3))
print(square(10))

change_name = lambda name: 'Mr. ' + name.upper()
print(change_name('Asabeneh'))


add_nums = lambda a, b, c, d: a + b + c + d
print(add_nums(1, 2, 3, 4))

'''
a, b, c 
ax + by + c = 0
2x + 3y + 10 = 0
'''
liniear_equation = lambda x, y, c : 2 * x + 3 * y + c

# Higher Order Function: When a function has another function as a parameter
# Higher order Function: When a function return another function 

def make_square(n):
    return n * n

""" def make_cube(n):
    return n * n * n """
    
    
def make_cube(m, fn):
    return m * fn(m)

print(make_cube(3, make_square))

def do_something(n, m, fn):
    return fn(n) + 3 * n  + m

def do_math(n, m, operation):
    def add_nums():
            return n + m
    def subtract():
        return n - m 
    def multiply():
        return n * m 
    def divide():
        return n / m 
    if operation == 'add':
        return add_nums 
    elif operation == 'subtract':
        return subtract
    elif operation == 'multiply':
        return multiply
    elif operation == 'divide':
        return divide
    else:
        return add_nums


print(do_math(3, 4,'multiply')())


def do_math(n, m):
    def add_nums():
            return n + m
    def subtract():
        return n - m 
    def multiply():
        return n * m 
    def divide():
        return n / m 
    return {
        'add_nums':add_nums,
        'multiply':multiply,
        'subtract':subtract,
        'divide':divide
    }

print(do_math(3, 4)['divide']())
print(do_math(3, 4)['add_nums']())
print(do_math(3, 4)['subtract']())