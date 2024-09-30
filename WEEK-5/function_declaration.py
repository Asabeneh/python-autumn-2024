# Function: a block of code that allow us to perform a certain task

def do_something(something):
    print(f'I am {something}.')


do_something('teaching')
do_something('learning')
do_something('Playing football')

'''

Declare a function which name is print_fullname and it should take two 
parameters

Function => make_square 
It takes n as a parameter and it will return a square of a number


'''

def print_fullname (first_name, last_name):
    full_name = f'{first_name} {last_name}'
    print(full_name)

print_fullname('Asab','Yeta')
print_fullname('John','Doe')
print_fullname(123, 435)
print_fullname('Donald','Trump')

def make_square (n):
    print(n ** 2)

make_square(10)
make_square(8)