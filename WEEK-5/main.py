# import custom_modules 
import custom_modules
from custom_modules import sum_all_nums, add_two_nums, multiply_two_nums, is_even, linear_equation, filter_country_with_land as filter_country, filter_evens
from utils import utils
""" 
print(sum_all_nums(2, 3, 4, 5,6, -10))
print(add_two_nums(2, 3))
print(multiply_two_nums(6, -10))
print(is_even(10))
print(linear_equation(2, 3, 6))
print(filter_country(countries)) """

# ['acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


from math import pi, factorial as f, sqrt, floor,ceil

def calculate_area_circle(radius):
    return pi * radius ** 2

""" print(floor(9.81))
print(ceil(9.81))
print(ceil(3.14))
print(sqrt(9))
print(sqrt(2)) """

'''
Name of function: generate_user_id
by default it will generate 6 character length id otherwise it should generate any length
'''
import random
print(dir(random))
print(random.choice('abcde'))
print(random.randint(0, 10))

""" for i in range(10):
    num = random.randint(0, 10)
    print(num) """



def generate_random_id (n = 6):
    numbers_alphabets = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    random_id = ''
    for _ in range(0, n):
        rand_value = random.choice(numbers_alphabets)
        random_id = random_id + rand_value
    return random_id

print(generate_random_id(2))
print(generate_random_id())
print(generate_random_id(7))
print(generate_random_id(24))

print(utils.alpha_numberic)
print(utils.generate_hexa_color())
print(dir(custom_modules))


