# Functions and Modules

- [Functions and Modules](#functions-and-modules)
  - [Functions in Python](#functions-in-python)
    - [Basic Function Structure](#basic-function-structure)
    - [Functions with Return Values](#functions-with-return-values)
    - [Functions for Multiplication](#functions-for-multiplication)
    - [More Complex Functions](#more-complex-functions)
    - [Functions with Variable Numbers of Parameters](#functions-with-variable-numbers-of-parameters)
    - [Default Parameter Values](#default-parameter-values)
    - [Keyword Arguments](#keyword-arguments)
    - [Checking Even Numbers](#checking-even-numbers)
    - [Filtering Even Numbers](#filtering-even-numbers)
    - [Grouping with Variable Parameters](#grouping-with-variable-parameters)
    - [Function Example: Print Full Name](#function-example-print-full-name)
    - [2. **Lambda Functions**](#2-lambda-functions)
    - [3. **Higher-Order Functions**](#3-higher-order-functions)
    - [4. **Function as a Parameter**](#4-function-as-a-parameter)
    - [Function summary](#function-summary)
  - [Modules](#modules)
    - [Importing Custom Modules](#importing-custom-modules)
    - [Example of Using Custom Functions](#example-of-using-custom-functions)
    - [Working with the `math` Library](#working-with-the-math-library)
    - [Example Usage of `math` Functions](#example-usage-of-math-functions)
  - [Generating Random Values with the `random` Library](#generating-random-values-with-the-random-library)
    - [Creating a Function to Generate a Random User ID](#creating-a-function-to-generate-a-random-user-id)
    - [Example Usage of `generate_random_id`](#example-usage-of-generate_random_id)
    - [Modules summary](#modules-summary)

[<< WEEK 4](../WEEK-4/week-4.md.md) | [WEEK 6 >>](../WEEK-6/week-6.md)

## Functions in Python

In Python, functions are reusable blocks of code that perform specific tasks. They can accept input, called parameters, and return results. Let's break down some examples to understand how functions work.

### Basic Function Structure

A function is defined using the `def` keyword, followed by the function name, parentheses (which may include parameters), and a colon. The function body contains the code to execute.

Example:

```python
def do_something(something):
    print(f'I am {something}.')
```

Here, `do_something` is a function that takes a parameter (`something`) and prints it.

Usage:

```python
do_something('teaching')
do_something('learning')
```

Output:

```
I am teaching.
I am learning.
```

### Functions with Return Values

Functions can return values using the `return` statement.

Example:

```python
def add_two_nums(x, y):
    return x + y
```

Here, `add_two_nums` returns the sum of `x` and `y`.

Usage:

```python
print(add_two_nums('3', '4'))  # Concatenates strings
print(add_two_nums(-3, -97))   # Adds two integers
```

Output:

```
34
-100
```

### Functions for Multiplication

You can also perform other operations, like multiplication.

Example:

```python
def multiply_two_nums(x, y):
    return x * y
```

Usage:

```python
print(multiply_two_nums('love', 3))  # Repeats the string 'love' three times
print(multiply_two_nums(100, 30))    # Multiplies two numbers
```

Output:

```sh
lovelovelove
3000
```

### More Complex Functions

You can define functions that take multiple parameters and perform operations.

Example:

```python
def linear_equation(x, y, k):
    return 2 * x - y + k
```

This function calculates the result of the equation `2x - y + k`.

Usage:

```python
print(linear_equation(2, 4, 10))
```

Output:

```sh
10
```

### Functions with Variable Numbers of Parameters

Python functions can accept a variable number of parameters using `*args`.

Example:

```python
def sum_all_nums(*params):
    return sum(params)
```

Usage:

```python
print(sum_all_nums(1, 2, 3, 4, 5, -15))
```

Output:

```sh
0
```

### Default Parameter Values

You can assign default values to parameters. If the function is called without providing that parameter, it will use the default value.

Example:

```python
def calculate_weight(mass, gravity=9.81):
    return mass * gravity
```

Usage:

```python
print(calculate_weight(74.5))         # Uses default gravity
print(calculate_weight(74.5, 1.62))   # Custom gravity (e.g., Moon)
print(calculate_weight(74.5, 3.71))   # Custom gravity (e.g., Mars)
```

Output:

```sh
730.245
120.69000000000001
276.395
```

### Keyword Arguments

You can pass arguments by name, which allows you to specify them in any order.

Example:

```python
def do_something(name, width, height, age, color):
    return f'{name} {width} {height} {age} {color}'
```

Usage:

```python
print(do_something(age=250, width=45, height=1.72, name='Asabeneh', color='Brown'))
```

Output:

```sh
Asabeneh 45 1.72 250 Brown
```

### Checking Even Numbers

You can write simple functions to perform logical checks, like determining whether a number is even.

Example:

```python
def is_even(n):
    return n % 2 == 0
```

Usage:

```python
print(is_even(0))
print(is_even(3))
```

Output:

```sh
True
False
```

### Filtering Even Numbers

You can filter a list of numbers to get only the even ones.

Example:

```python
def filter_evens(lst):
    return [num for num in lst if num % 2 == 0]
```

Usage:

```python
nums = [-6, 0, 5, 2, 7, -4]
print(filter_evens(nums))
```

Output:

```sh
[-6, 0, 2, -4]
```

### Grouping with Variable Parameters

You can group different types of input using `*args` and `**kwargs` for variable positional and keyword arguments.

Example:

```python
def generate_groups(team, country, *args):
    print(team, args)
    for i in args:
        print(i)
```

Usage:

```python
generate_groups('Team-1', 'Finland', 'Asabeneh', 'Brook', 'David', 'Eyob')
```

Output:

```sh
Team-1 ('Asabeneh', 'Brook', 'David', 'Eyob')
Asabeneh
Brook
David
Eyob
```

### Function Example: Print Full Name

Let's create a function to print the full name by taking two parameters: `first_name` and `last_name`.

Example:

```python
def print_fullname(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    print(full_name)
```

Usage:

```python
print_fullname('Asab', 'Yeta')
```

Output:

```sh
Asab Yeta
```

### 2. **Lambda Functions**

Lambda functions are anonymous, single-line functions. They are used for short operations without needing to define a full function.

```python
square = lambda x: x ** 2
add_three_nums = lambda x, y, z: x + y + z
linear_equation = lambda a, b, c: 2 * a + 3 * b + c
```

Examples:

```python
print(square(2))  # Output: 4
print(add_three_nums(99, 1, 100))  # Output: 200
```

### 3. **Higher-Order Functions**

A higher-order function either takes a function as an argument or returns another function.

- `make_cube` is a higher-order function because it takes another function, `make_square`, as a parameter to calculate the cube of a number.

```python
def make_cube(n, make_square):
    return n * make_square(n)
```

Example:

```python
print(make_cube(3, make_square))  # Output: 27
```

- `higher_order_function` accepts a function type and returns the corresponding function based on the input, such as `square`, `cube`, or `absolute`.

```python
def higher_order_function(type):
    if type == 'square':
        return make_square
    elif type == 'cube':
        return make_cube
    elif type == 'absolute':
        return absolute
```

Example:

```python
print(higher_order_function('square')(5))  # Output: 25
print(higher_order_function('cube')(5, make_square))  # Output: 125
```

### 4. **Function as a Parameter**

The `higher_order_function` function shows how a function can be passed as an argument to another function. It’s demonstrated using `sum_numbers` and a custom higher-order function that sums a list of numbers:

```python
def higher_order_function(f, lst):
    return f(lst)
```

Example:

```python
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
```

This sums the list of numbers, returning `15`.

This code provides an overview of how to work with keyword arguments, lambda expressions, and higher-order functions in Python, illustrating their versatility and power in functional programming.


### Function summary

Functions are an essential part of programming in Python. They allow code reuse, make programs easier to understand, and help to organize logic into smaller, manageable pieces. With the examples provided, you can see various use cases for defining and using functions in Python.

## Modules

In Python, modularity is a key feature that helps organize code and improve reusability. This reading material will cover how to work with custom modules and some useful standard Python libraries, including `math` and `random`. The code examples provided below will guide you through practical implementations of these concepts.

### Importing Custom Modules

To keep code clean and manageable, you can create custom modules that contain specific functions. Below, we import a custom module `custom_modules` and another module `countries`, which contains various utility functions like `sum_all_nums`, `add_two_nums`, and `filter_country_with_land`.

```python
# Import functions from custom modules
from custom_modules import sum_all_nums, add_two_nums, multiply_two_nums, is_even, linear_equation, filter_country_with_land as filter_country, filter_evens, filter_positive_evens
from countries import countries
```

Once imported, these functions can be used directly in your script, making the code easier to read and maintain.

### Example of Using Custom Functions

```python
# Example usage of custom functions
print(sum_all_nums(2, 3, 4, 5, 6, -10))  # Sums up the numbers
print(add_two_nums(2, 3))                 # Adds two numbers
print(multiply_two_nums(6, -10))          # Multiplies two numbers
print(is_even(10))                        # Checks if the number is even
print(linear_equation(2, 3, 6))           # Solves a linear equation
print(filter_country(countries))          # Filters countries that contain the word 'land'
```

### Working with the `math` Library

The `math` library is a built-in Python module providing many mathematical functions. Below are some functions we imported from `math` and their usage:

```python
from math import pi, factorial as f, sqrt, floor, ceil

# Calculate the area of a circle
def calculate_area_circle(radius):
    return pi * radius ** 2
```

- **`pi`**: A constant representing the value of π (used in circle calculations).
- **`factorial`**: Computes the factorial of a number.
- **`sqrt`**: Returns the square root of a number.
- **`floor`**: Rounds down to the nearest integer.
- **`ceil`**: Rounds up to the nearest integer.

### Example Usage of `math` Functions

```python
print(floor(9.81))  # Output: 9
print(ceil(9.81))   # Output: 10
print(sqrt(9))      # Output: 3.0
print(sqrt(2))      # Output: 1.4142135623730951
```

## Generating Random Values with the `random` Library

Python's `random` library provides methods to generate random numbers and choices. Here's how to explore and use some common `random` functions:

```python
import random

# Display all available functions in the random module
print(dir(random))  

# Example: random.choice picks a random character from a string
print(random.choice('abcde'))  

# random.randint generates a random integer within a specified range
print(random.randint(0, 10))   
```

### Creating a Function to Generate a Random User ID

Let's create a function, `generate_random_id`, that generates random alphanumeric IDs of any length (default is 6 characters).

```python
def generate_random_id(n=6):
    characters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    random_id = ''
    for _ in range(n):
        random_id += random.choice(characters)
    return random_id
```

### Example Usage of `generate_random_id`

```python
print(generate_random_id(2))   # Generates a 2-character random ID
print(generate_random_id())    # Default 6-character ID
print(generate_random_id(7))   # Generates a 7-character ID
print(generate_random_id(24))  # Generates a 24-character ID
```

This function is useful when you need unique identifiers for users or other entities in your application.

---

### Modules summary

In this tutorial, we explored:

1. **Custom Modules**: How to import and use functions from custom modules for better code organization.
2. **`math` Library**: Various mathematical functions, such as calculating areas, square roots, and rounding numbers.
3. **`random` Library**: Generating random numbers, choosing random elements, and creating random IDs.

By modularizing your code and using built-in libraries like `math` and `random`, you can write cleaner, more efficient Python programs.

[<< WEEK 4](../WEEK-4/week-4.md.md) | [WEEK 6 >>](../WEEK-6/week-6.md)
