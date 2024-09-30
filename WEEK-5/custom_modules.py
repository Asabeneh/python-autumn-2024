def do_something(something):
    print(f'I am {something}.')

def add_two_nums(x, y):
    return x + y


def multiply_two_nums(x, y):
    return x * y

def linear_equation(x, y, k):
    return 2 * x - y * + k

def sum_all_nums(*params):
    return sum(params)

def calculate_weight (mass, gravity = 9.81):
    return round(mass * gravity, 2)

def is_even (n):
    return n % 2 == 0


def filter_positive_evens(lst):
    new_lst = []
    for num in lst:
        if num % 2 == 0 and num < 0:
            new_lst.append(num)
    return new_lst

def filter_evens(lst):
    new_lst = []
    for num in lst:
        if num % 2 == 0:
            new_lst.append(num)
    return new_lst

def filter_country_with_land(lst):
    new_lst = []
    for country in lst:
        if 'land' in country:
            new_lst.append(country)
    return new_lst

# module: is a collection of functions
# NumPy, Pandas, Matplotlib
