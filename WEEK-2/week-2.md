- [Section Introduction](#section-introduction)
- [Python Operators](#python-operators)
  - [Arithmetic Operators](#arithmetic-operators)
  - [Assignment Operators](#assignment-operators)
- [Comparison (Relational) Operators](#comparison-relational-operators)
  - [Logical Operators](#logical-operators)
  - [Bitwise Operators](#bitwise-operators)
  - [Membership Operators](#membership-operators)
  - [Identity Operators](#identity-operators)
  - [Ternary Operator (Conditional Expression)](#ternary-operator-conditional-expression)
  - [Special Operators](#special-operators)
  - [`del` Operator](#del-operator)
  - [`pass` Operator](#pass-operator)
- [Variables](#variables)
  - [Understanding Variables and Basic Operations](#understanding-variables-and-basic-operations)
  - [What is Variable?](#what-is-variable)
  - [Conclusion](#conclusion)
- [Python Data Types](#python-data-types)
  - [Numbers](#numbers)
  - [Booleans](#booleans)
  - [Strings](#strings)
  - [Lists](#lists)
  - [Tuples](#tuples)
  - [Sets](#sets)
  - [Dictionaries](#dictionaries)

---

[<< WEEK 1](../readme.md) | [WEEK 3 >>](../WEEK-3/week-3.md)

## Section Introduction

This section introduces essential Python concepts through practical examples. It covers operators, variables, data types, and built-in functions, making it a great resource for both beginners and intermediate learners. Each example is accompanied by explanations to ensure clarity and understanding.

## Python Operators

In Python, operators are special symbols or keywords used to perform operations on values and variables. Operators can manipulate data, compare values, and control the flow of execution in a program. Below is an in-depth guide to all the different types of Python operators:

---

### Arithmetic Operators

Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication, etc.

| Operator | Description                | Example     | Output  |
|----------|----------------------------|-------------|---------|
| `+`      | Addition                    | `3 + 2`     | `5`     |
| `-`      | Subtraction                 | `5 - 2`     | `3`     |
| `*`      | Multiplication              | `4 * 3`     | `12`    |
| `/`      | Division (float)            | `10 / 4`    | `2.5`   |
| `%`      | Modulus (remainder)         | `10 % 3`    | `1`     |
| `**`     | Exponentiation (power)      | `2 ** 3`    | `8`     |
| `//`     | Floor division (integer div)| `10 // 3`   | `3`     |

**Examples:**

```python
# Addition
print(3 + 4)  # Output: 7

# Exponentiation
print(2 ** 3)  # Output: 8

# Floor division
print(10 // 4)  # Output: 2
```

---

### Assignment Operators

Assignment operators are used to assign values to variables. Python provides various forms of assignment operators to simplify variable manipulations.

| Operator  | Description                    | Example    | Equivalent |
|-----------|--------------------------------|------------|------------|
| `=`       | Assign value                   | `a = 5`    | -          |
| `+=`      | Add and assign                 | `a += 3`   | `a = a + 3`|
| `-=`      | Subtract and assign            | `a -= 3`   | `a = a - 3`|
| `*=`      | Multiply and assign            | `a *= 2`   | `a = a * 2`|
| `/=`      | Divide and assign (float)      | `a /= 2`   | `a = a / 2`|
| `%=`      | Modulus and assign             | `a %= 3`   | `a = a % 3`|
| `**=`     | Exponentiation and assign      | `a **= 2`  | `a = a ** 2`|
| `//=`     | Floor divide and assign        | `a //= 2`  | `a = a // 2`|

**Examples:**

```python
a = 10
a += 5  # a = a + 5
print(a)  # Output: 15

b = 20
b //= 3  # b = b // 3
print(b)  # Output: 6
```

---

## Comparison (Relational) Operators

Comparison operators are used to compare two values or variables, returning a boolean (`True` or `False`).

| Operator | Description             | Example     | Output   |
|----------|-------------------------|-------------|----------|
| `==`     | Equal to                 | `5 == 5`    | `True`   |
| `!=`     | Not equal to             | `5 != 4`    | `True`   |
| `>`      | Greater than             | `7 > 5`     | `True`   |
| `<`      | Less than                | `5 < 10`    | `True`   |
| `>=`     | Greater than or equal to | `7 >= 7`    | `True`   |
| `<=`     | Less than or equal to    | `4 <= 5`    | `True`   |

**Examples:**

```python
print(5 == 5)  # Output: True
print(3 != 2)  # Output: True
print(7 < 6)   # Output: False
```

---

### Logical Operators

Logical operators are used to combine conditional statements and return boolean results.

| Operator | Description                  | Example            | Output  |
|----------|------------------------------|--------------------|---------|
| `and`    | Returns `True` if both conditions are true | `True and True`  | `True`  |
| `or`     | Returns `True` if at least one condition is true | `True or False` | `True`  |
| `not`    | Reverses the result (returns `False` if the result is `True`) | `not True` | `False` |

**Examples:**

```python
print(5 > 3 and 8 > 6)  # Output: True
print(5 > 3 or 2 > 6)   # Output: True
print(not 5 == 5)       # Output: False
```

---

### Bitwise Operators

Bitwise operators work at the binary level (i.e., on bits) and are mainly used in low-level programming or when manipulating individual bits.

| Operator | Description                          | Example  | Output |
|----------|--------------------------------------|----------|--------|
| `&`      | Bitwise AND                          | `5 & 3`  | `1`    |
| `|`      | Bitwise OR                           | `5 | 3`  | `7`    |
| `^`      | Bitwise XOR                          | `5 ^ 3`  | `6`    |
| `~`      | Bitwise NOT                          | `~5`     | `-6`   |
| `<<`     | Bitwise left shift                   | `5 << 1` | `10`   |
| `>>`     | Bitwise right shift                  | `5 >> 1` | `2`    |

**Examples:**

```python
# Bitwise AND
print(5 & 3)  # Output: 1

# Bitwise left shift
print(5 << 1)  # Output: 10
```

---

### Membership Operators

Membership operators are used to test if a value is present in a sequence (e.g., a string, list, tuple, or set).

| Operator | Description                   | Example          | Output |
|----------|-------------------------------|------------------|--------|
| `in`     | Returns `True` if the value is present | `'a' in 'apple'` | `True`  |
| `not in` | Returns `True` if the value is not present | `'b' not in 'apple'` | `True`  |

**Examples:**

```python
print('p' in 'apple')  # Output: True
print(2 not in [1, 3, 5])  # Output: True
```

---

### Identity Operators

Identity operators check if two variables refer to the same object in memory.

| Operator | Description                       | Example         | Output |
|----------|-----------------------------------|-----------------|--------|
| `is`     | Returns `True` if two variables point to the same object | `a is b` | `True`  |
| `is not` | Returns `True` if two variables point to different objects | `a is not b` | `True`  |

**Examples:**

```python
a = [1, 2, 3]
b = a
print(a is b)  # Output: True (b refers to the same object as a)

c = [1, 2, 3]
print(a is not c)  # Output: True (c is a different object even though it contains the same values)
```

---

### Ternary Operator (Conditional Expression)

The ternary operator is used to evaluate a condition in a single line of code and return one of two values based on the condition.

**Syntax:**  
`[on_true] if [condition] else [on_false]`

**Example:**

```python
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

---

### Special Operators

### `del` Operator

The `del` operator is used to delete objects or variables.

```python
a = 5
del a  # a is deleted and no longer accessible
```

### `pass` Operator

The `pass` operator is a null operation; it is used as a placeholder for future code.

```python
def func():
    pass  # No code yet
```

---

Understanding Python operators is essential for writing efficient and concise code. From basic arithmetic to advanced bitwise manipulation, operators allow you to perform a wide variety of tasks in Python programs.

## Variables

In Python, variables store data of different types such as integers, floats, strings, and booleans.

### Understanding Variables and Basic Operations

In Python, variables serve as containers that store data values. They can hold various data types, including numbers, strings, lists, tuples, and sets. This reading material explores how to create and use variables, perform arithmetic operations, manage personal information, demonstrate different data structures, and perform calculations.

---

### What is Variable?

Variables are fundamental components of programming that allow you to store and manipulate data. In Python, you can assign a value to a variable using the assignment operator (=). To make your code more readable and maintainable, it is important to use descriptive variable names that convey the purpose of the variable clearly.

Descriptive Variable Names
A descriptive variable name should:

- Be clear and convey meaning about the data it holds.
- Use lowercase letters, separating words with underscores (snake_case) for better readability.
- Avoid using single-letter variable names unless in a very small scope (e.g., loop counters).

Variables are fundamental components of programming that allow you to store and manipulate data. In Python, you can assign a value to a variable using the assignment operator (`=`). Here's an example:

```python
# Arithmetic Operations
a = 3
b = 4
c = a + b
```

In this snippet:

- `a` and `b` are variables assigned the values `3` and `4`, respectively.
- `c` stores the sum of `a` and `b`.

**Output of Variable Values:**

You can print the values of these variables using the `print()` function:

```python
print('Value of a:', a)                   # Output: Value of a: 3
print('Sum of a and b:', c)               # Output: Sum of a and b: 7
print('Sum of a and b is', a + b)         # Output: Sum of a and b is 7
print('Difference of a and b is', a - b)  # Output: Difference of a and b is -1
print('Product of a and b is', a * b)     # Output: Product of a and b is 12
print('Division of a and b is', a / b)    # Output: Division of a and b is 0.75
```

Explanation of Arithmetic Operations:

- **Addition (`+`)**: Adds two values.
- **Subtraction (`-`)**: Subtracts the second value from the first.
- **Multiplication (`*`)**: Multiplies two values.
- **Division (`/`)**: Divides the first value by the second.

---

**Personal Information:**

You can also use variables to store personal information:

```python
# Personal Information
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
```

**Explanation of Personal Information Variables:**

- `first_name`, `last_name`, `country`, `city`: Variables holding string values representing personal information.
- `age`: An integer variable representing the person's age.
- `is_married`: A boolean variable indicating marital status.

---

**Demonstrating Different Data Structures:**

Python provides various data structures to store collections of data. Here are examples of a list, tuple, and set:

```python
# Skills: Demonstrating different data structures
skills_list = ['HTML', 'CSS', 'JavaScript', 'Python']  # List - mutable and ordered
skills_tuple = ('HTML', 'CSS', 'JavaScript', 'Python')  # Tuple - immutable and ordered
skills_set = {'HTML', 'CSS', 'JavaScript', 'Python'}    # Set - unordered and unique
```

**Explanation of Data Structures:**

- **List**: A mutable and ordered collection. You can modify its elements after creation.
- **Tuple**: An immutable and ordered collection. Once created, you cannot change its elements.
- **Set**: An unordered collection of unique items. It automatically removes duplicates.

---

**Weight Calculation:**

You can also perform calculations using variables to derive new values. For example, calculating weight based on mass and gravitational acceleration:

```python
# Weight Calculation
gravity = 9.81  # Acceleration due to gravity (m/s^2)
mass = 75       # Mass (kg)
weight = mass * gravity

print('Weight:', round(weight, 1))  # Output: Weight: 735.8
```

**Explanation of Weight Calculation:**

- **Gravity**: A constant representing the gravitational force.
- **Mass**: The mass of the object.
- **Weight**: Calculated as the product of mass and gravity.

---

**Current Year:**

You can store the current year in a variable:

```python
# Current Year
current_year = 2024
```

**Explanation:**

- The variable `current_year` holds the integer value representing the current year.

---

### Conclusion

This reading material covers the essential aspects of variables and basic operations in Python. Using descriptive variable names enhances code readability and maintainability. Understanding how to create and manipulate variables, perform arithmetic operations, and utilize different data structures is fundamental to effective programming. With these concepts, you can begin to build more complex programs and data management solutions in Python.

## Python Data Types

Python is a dynamically typed language, meaning that the type of a variable is determined at runtime. Understanding data types is crucial for effective programming in Python, as it allows for proper data manipulation and handling. This guide covers the main data types in Python, providing examples and expected outputs for each.

Python supports several fundamental data types:

- **Numbers**: `int`, `float`, `complex`
- **Booleans**: `True`, `False`
- **Strings**: Text enclosed in single, double, or triple quotes
- **Lists**: Ordered collections of elements
- **Tuples**: Immutable collections
- **Sets**: Unordered collections of unique elements
- **Dictionaries**: Key-value pairs

---

### Numbers

In Python, numbers come in several types:

```python
# Numbers
print("Numbers:")
print(type(10))  # int
# Output: <class 'int'>

print(type('10'))  # str
# Output: <class 'str'>

print(type(9.81))  # float
# Output: <class 'float'>

print(type(1 + 2j))  # complex
# Output: <class 'complex'>
```

**Explanation:**

- **Integer (`int`)**: Represents whole numbers.
- **String (`str`)**: A sequence of characters; here, it’s the representation of a number.
- **Float (`float`)**: Represents decimal numbers.
- **Complex (`complex`)**: Represents complex numbers, denoted by `a + bj`, where `a` is the real part and `b` is the imaginary part.

---

### Booleans

Booleans represent truth values: `True` or `False`.

```python
print("\nBooleans:")
print(type(True))  # bool
# Output: <class 'bool'>

print(type(False))  # bool
# Output: <class 'bool'>

print(type(0 < 1))  # bool
# Output: <class 'bool'>

print(len('cat') == len('car'))  # False
# Output: False

print('cat' == 'cat')  # True
# Output: True
```

**Explanation:**

- **Boolean (`bool`)**: Represents truth values, often used in conditions and comparisons.

---

### Strings

Strings are sequences of characters enclosed in single, double, or triple quotes.

```python
print("\nStrings:")
print('a')  # Single character string
# Output: a

print('I love Python programming')  # String sentence
# Output: I love Python programming

print('I love Python programming'.lower())  # Convert to lowercase
# Output: i love python programming

print('I love Python programming'.upper())  # Convert to uppercase
# Output: I LOVE PYTHON PROGRAMMING

print('I love Python programming'.title())  # Title case
# Output: I Love Python Programming

print('I love Python programming'.swapcase())  # Swap case
# Output: i LOVE pYTHON PROGRAMMING

print('I love Python programming'.split())  # Split into a list of words
# Output: ['I', 'love', 'Python', 'programming']

print('I love Python programming'.startswith('I love'))  # Check if it starts with 'I love'
# Output: True

print('I love Python programming'.endswith('ing'))  # Check if it ends with 'ing'
# Output: True

# Explore string methods
print(dir('example_string'))  # Show available string methods
# Output: List of string methods
```

**Explanation:**

- Strings can be manipulated using various methods for formatting, case conversion, and more.

---

### Lists

Lists are ordered, mutable collections of items.

```python
print("\nLists:")
print([1, 2, 3, 4, 5])  # List of numbers
# Output: [1, 2, 3, 4, 5]

print(['potatoes', 'tomatoes', 'milk', 'coffee', 'honey'])  # List of strings
# Output: ['potatoes', 'tomatoes', 'milk', 'coffee', 'honey']

print(len(['potatoes', 'tomatoes', 'milk', 'coffee', 'honey']))  # List length
# Output: 5

print(['potatoes', 'tomatoes', 'milk', 'coffee', 'honey'][0])  # Accessing the first item
# Output: potatoes
```

**Explanation:**

- **List**: A collection that can hold a variety of items, allows duplication and is mutable (can be changed).

---

### Tuples

Tuples are ordered, indexed, and immutable collections.

```python
print("\nTuples:")
print((1, 2, 3, 4, 5))  # Tuple of numbers
# Output: (1, 2, 3, 4, 5)

print(len((1, 2, 3, 4, 5)))  # Tuple length
# Output: 5

print(type((1, 2, 3, 4, 5)))  # Type check
# Output: <class 'tuple'>

print((1, 2, 3, 4, 5)[0])  # Accessing the first item
# Output: 1
```

**Explanation:**

- **Tuple**: Similar to a list but cannot be changed (immutable). Used when the data should not be modified.

---

### Sets

Sets are unordered collections of unique items, meaning no duplicates are allowed.

```python
print("\nSets:")
print({1, 2, 3, 7, 8, 4, 5})  # Set of numbers
# Output: {1, 2, 3, 4, 5, 7, 8}

print(len({1, 2, 3, 3, 3, 4, 5}))  # Set length (duplicates removed)
# Output: 5

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Finland', 'Sweden', 'Finland']
print(len(countries))  # Length of original list
# Output: 7

print(list(set(countries)))  # Convert to set to remove duplicates and back to list
# Output: ['Denmark', 'Norway', 'Sweden', 'Finland']
```

**Explanation:**

- **Set**: A collection that automatically removes duplicates and does not maintain order.

---

### Dictionaries

Dictionaries are collections of key-value pairs.

```python
print("\nDictionaries:")
fin_eng_dict = {
    'auto': 'car',
    'talo': 'house',
    'tuoli': 'chair',
    'tietokone': 'computer'
}
print(fin_eng_dict)  # Dictionary of fin_eng_dict
# Output: {'auto': 'car', 'talo': 'house', 'tuoli': 'chair', 'tietokone': 'computer'}

person = {
    'first_name': 'Asab',
    'last_name': 'Yeta',
    'country': 'Finland',
    'city': 'Helsinki',
    'age': 250,
    'is_married': True,
    'skills': ['JavaScript', 'Python', 'SQL']
}
print(person)  # Person dictionary
# Output: {'first_name': 'Asab', 'last_name': 'Yeta', 'country': 'Finland', 'city': 'Helsinki', 'age': 250, 'is_married': True, 'skills': ['JavaScript', 'Python', 'SQL']}

print(len(person))  # Dictionary length
# Output: 7

print(type(person))  # Type check
# Output: <class 'dict'>
```

**Explanation:**

- **Dictionary**: A collection of key-value pairs where keys are unique, allowing fast access to values.

---

Understanding these fundamental data types will enhance your programming skills in Python and help you choose the right type for your data needs. Each data type serves its purpose and can be manipulated using a variety of built-in methods and operations.

[<< WEEK 1](../readme.md) | [WEEK 3 >>](../WEEK-3/week-3.md)
