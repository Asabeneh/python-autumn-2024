
# Loops

- [Loops](#loops)
  - [Python Loops and Control Structures](#python-loops-and-control-structures)
  - [Introduction to Loops in Python](#introduction-to-loops-in-python)
    - [For loop](#for-loop)
    - [While Loop](#while-loop)
    - [Loop Control: Break and Continue](#loop-control-break-and-continue)
    - [Loops Summary](#loops-summary)
  - [Understanding Sets in Python](#understanding-sets-in-python)
    - [What is a Set?](#what-is-a-set)
    - [Adding Items to a Set](#adding-items-to-a-set)
    - [3. Set Operations](#3-set-operations)
      - [Union](#union)
      - [Intersection](#intersection)
      - [Difference](#difference)
      - [Symmetric Difference](#symmetric-difference)
      - [Membership Testing](#membership-testing)
      - [Iterating Through a Set](#iterating-through-a-set)
      - [Modifying Sets](#modifying-sets)
      - [Converting list to set](#converting-list-to-set)
      - [Combining Sets](#combining-sets)
      - [Subset and Superset Checks](#subset-and-superset-checks)
  - [Sets Summary](#sets-summary)
  - [Tuples in Python](#tuples-in-python)
    - [What is a Tuple?](#what-is-a-tuple)
    - [Working with Tuples](#working-with-tuples)
    - [Iterating Through a Tuple](#iterating-through-a-tuple)
    - [Accessing Tuple Elements](#accessing-tuple-elements)
    - [Concatenating Tuples](#concatenating-tuples)
    - [Iterating Through Combined Tuples](#iterating-through-combined-tuples)
    - [Converting Tuples to Lists](#converting-tuples-to-lists)
    - [Enumerating with a Custom Start Index](#enumerating-with-a-custom-start-index)
  - [Tuples Summary](#tuples-summary)
  - [Dictionaries in Python](#dictionaries-in-python)
    - [What is a Dictionary?](#what-is-a-dictionary)
    - [Key-Value Structure](#key-value-structure)
    - [Accessing Dictionary Items](#accessing-dictionary-items)
    - [Adding New Key-Value Pairs](#adding-new-key-value-pairs)
    - [Modifying and Appending Data](#modifying-and-appending-data)
    - [Iterating Through a Dictionary](#iterating-through-a-dictionary)
    - [Getting Keys and Values](#getting-keys-and-values)
  - [Dictionaries Summary](#dictionaries-summary)

---

[<< WEEK 2](../readme.md) | [WEEK 4 >>](../WEEK-4/week-4.md)

## Python Loops and Control Structures

This script demonstrates various looping mechanisms and control structures in Python, focusing on `for` and `while` loops. It covers iteration over sequences, condition checking, and loop controls like `break` and `continue`. Below is a detailed explanation of the key components and their functionality.

---

## Introduction to Loops in Python

Loops in Python are control structures used to repeat a block of code multiple times, either for a specified number of iterations or until a certain condition is met. Python provides two types of loops:

- **For loop**: Iterates over a sequence (like a list or a range).
- **While loop**: Repeats the block of code as long as a condition is `True`.

**Simple Repetition**:

```python
print('Hello World!')
```

This basic block prints "Hello World!" multiple times to the console. Instead of repeating the statement manually, this can be achieved more efficiently using a loop.

### For loop

**For Loop with Range**:

- For loop: Iterates over a sequence (like a list or a range).

for element in sequence:
    # code block

```python
nums = range(0, 10)
for num in nums:
    print(num, 'Hello world!')

```

- **`range(1, 6)`**: Generates numbers from 1 to 5.
- **Odd number check**: The loop prints "Hello world!" only for odd numbers (numbers not divisible by 2).

**Iterating Over Lists**:

```python
names = ['Mikko','Matti','Elena', 'Olga','Lauri','Kimm0','Mehrnaz','Jevgeni','Goodluck','Pullo','Asabeneh']
for name in names:
    if len(name) > 6:
        print(f'{name} is a long name.')
    else:
        print(f'{name} is a short name')
```

- This loop iterates over the list of `names` and checks the length of each name.
- If the length of the name is greater than 6, it categorizes it as a "long name"; otherwise, it's considered a "short name."

**Working with Country Names**:

The list `countries` holds a collection of country names. Several loops demonstrate different tasks such as:

- Finding countries containing "land":

    ```python
    countries_with_land = []
    for country in countries:
        if 'land' in country:
            countries_with_land.append(country)
    print(countries_with_land, len(countries_with_land))
    ```

- Countries ending with "ia":

    ```python
    for country in countries:
        if country.endswith('ia'):
            print(country)
    ```

- Countries starting with the letter 'B':

    ```python
    countries_starts_with_s = []
    for country in countries:
        if country.startswith('B'):
            countries_starts_with_s.append(country)
    print(countries_starts_with_s, len(countries_starts_with_s))
    ```

**Summing and Categorizing Numbers**:

This section explores how to sum numbers and categorize them into positive and negative lists.

```python
nums = [-10, 5, 0, 20, 4.5, 20, -14, 25, -3]
total = 0
for num in nums:
    total += num
print(total)
```

- A total sum of numbers is calculated.
- Numbers are further split into **positive** and **negative** categories:

    ```python
    positive_nums = []
    negative_nums = []
    for num in nums:
        if num > 0:
            positive_nums.append(num)
        else:
            negative_nums.append(num)
    print(positive_nums)
    print(negative_nums)
    ```

### While Loop

The `while` loop runs as long as the condition remains `True`. It checks the condition before executing the block of code.

**Syntax**:

```python
while condition:
    # code block
```

Example 1: Using a `while` loop to print a countdown:

```python
count = 5
while count > -1:
    print(count)
    count -= 1
```

This loop continues to print the `count` variable until it reaches 6. It demonstrates how to use a `while` loop to perform repetitive tasks until a condition is met.

Example 2: Using `while` loop with a break condition

```python
names = []
while True:
    name = input('Enter name: ')
    if name == 'quit' or name == '':
        break
    names.append(name)
print(names)
```

### Loop Control: Break and Continue

- **Skip Negative Values**:

    ```python
    for num in nums:
        if num <= 0:
            continue
        print(num)
    ```

    The `continue` statement is used to skip negative numbers and proceed with the next iteration.
  
- **Stop Looping at Zero**:

    ```python
    for num in nums:
        if num == 0:
            break
        print(num)
    ```

    The `break` statement stops the loop when the number `0` is encountered.

**Multiplication Table**:

A simple loop to print the multiplication table of numbers from 0 to 10:

```python
for i in range(11):
    print(f'{i} x {i} = {i * i}')
```

### Loops Summary

This script demonstrates several fundamental concepts in Python looping and control structures, including:

- Iterating over sequences with `for` loops.
- Repeating tasks with `while` loops.
- Using `continue` to skip certain iterations.
- Using `break` to exit a loop prematurely.
  
These concepts are crucial for understanding more advanced Python programming, especially in data processing, algorithm implementation, and automation tasks.

## Understanding Sets in Python

Sets are a powerful and versatile data structure in Python, designed to hold collections of unique items. This reading material will explore the fundamental characteristics of sets, demonstrate how to create and manipulate them, and explain their various operations.

---

### What is a Set?

A **set** is an unordered collection of items. The key features of sets include:

- **Unordered**: The items in a set do not maintain any specific order, meaning that indexing is not supported.
- **Unique Items**: Sets automatically eliminate duplicate entries, ensuring all items are unique.
- **Mutable**: You can add or remove items from a set after its creation.

Example: Creating an Empty Set

```python
# Creating an empty set
empty_set = set()

print(empty_set, len(empty_set))  # Output: set() 0
print(dir(empty_set))               # Lists available methods for the set
```

In this example, an empty set is created, and its length is printed, showing that it currently contains no items.

---

### Adding Items to a Set

You can add items to a set using the `add()` method.

Example: Adding Items

```python
empty_set.add('Milk')
empty_set.add('Coffee')
print(empty_set)  # Output: {'Milk', 'Coffee'}
```

---

### 3. Set Operations

Sets support various mathematical operations such as union, intersection, difference, and symmetric difference. Here’s how to perform these operations:

#### Union

The union of two sets combines all unique items from both sets.

```python
A = {1, 2, 3, 4, 5, 6}
B = {3, 4, 7, 8}

# Union
print(A.union(B))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(B.union(A))  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
```

#### Intersection

The intersection returns only the items present in both sets.

```python
# Intersection
print(A.intersection(B))  # Output: {3, 4}
print(B.intersection(A))  # Output: {3, 4}
```

#### Difference

The difference returns items that are in one set but not the other.

```python
# Difference
print(A.difference(B))  # Output: {1, 2, 5, 6}
print(B.difference(A))  # Output: {7, 8}
```

#### Symmetric Difference

The symmetric difference returns items that are in either set but not in both.

```python
# Symmetric Difference
print(A.symmetric_difference(B))  # Output: {1, 2, 5, 6, 7, 8}
```

---

#### Membership Testing

You can check if an item is present in a set using the `in` keyword.

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('kiwi' in fruits)   # Output: False
print('orange' in fruits)  # Output: True
```

---

#### Iterating Through a Set

You can use a loop to iterate through the items in a set:

```python
for fruit in fruits:
    print(fruit)
```

---

#### Modifying Sets

You can modify a set by adding multiple items using the `update()` method or removing items using the `remove()` and `pop()` methods.

Example: Adding and Removing Items

```python
fruits.add('guava')
fruits.add('papaya')
print(fruits)  # Output: {'banana', 'orange', 'mango', 'lemon', 'guava', 'papaya'}

# Remove an item
fruits.remove('orange')
print(fruits)  # Output: {'banana', 'mango', 'lemon', 'guava', 'papaya'}

# Clear all items
fruits.clear()
print(fruits)  # Output: set()
```

---

#### Converting list to set

You can convert a list to a set to eliminate duplicate entries:

```python
print(set(['Finland', 'Sweden', 'Denmark', 'Sweden']))  # Output: {'Finland', 'Sweden', 'Denmark'}
```

---

#### Combining Sets

You can combine multiple sets into one using the `union()` method.

```python
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
combined_items = fruits.union(vegetables)
print(combined_items)  # Combines fruits and vegetables
```

---

#### Subset and Superset Checks

Sets can also be checked for subset or superset relationships:

```python
A = {1, 2, 3, 4}
B = {1, 2, 3, 3, 4, 5, 6}

print(A.issubset(B))        # Output: True
print(A.isdisjoint(B))      # Output: False (they share common elements)
print(B.issuperset(A))      # Output: True
```

---

## Sets Summary

Sets are a powerful feature of Python, enabling the storage of unique items and providing various operations for data manipulation. Understanding how to create and work with sets is essential for effective programming in Python, especially when dealing with collections of items where uniqueness and mathematical set operations are required.

## Tuples in Python

Tuples are one of the fundamental data types in Python, offering a versatile way to store collections of items. This reading material will provide an in-depth look at tuples, their properties, operations, and usage examples.

---

### What is a Tuple?

A **tuple** is an immutable data structure that can hold a collection of items. The key characteristics of tuples include:

- **Immutable**: Once a tuple is created, its contents cannot be changed (i.e., you cannot add, remove, or modify elements).
- **Ordered**: The items in a tuple maintain the order in which they were defined.
- **Indexable**: Each item in a tuple can be accessed using an index.

Example: Creating an Empty Tuple

```python
# Creating an empty tuple
empty_tpl = tuple()  # Alternatively: empty_tpl = ()
print(type(empty_tpl))  # Output: <class 'tuple'>
```

In this example, an empty tuple is created, and its type is printed.

---

### Working with Tuples

Example: Creating a Tuple

You can create a tuple with multiple items:

```python
nums = (1, 2, 3, 4)
print(len(nums), type(nums))  # Output: 4 <class 'tuple'>
```

The `len()` function returns the number of elements in the tuple, while `type()` confirms that it is a tuple.

### Iterating Through a Tuple

You can iterate over the items in a tuple using a loop:

```python
for num in nums:
    print(num)
```

This will print each number in the `nums` tuple.

---

### Accessing Tuple Elements

You can access specific elements or slices of a tuple using indexing:

```python
fruits = ('banana', 'orange', 'mango', 'lemon')
print(fruits[1:])  # Output: ('orange', 'mango', 'lemon')
print(fruits[1:3])  # Output: ('orange', 'mango')
```

Example: Tuple Unpacking

You can unpack tuple elements into multiple variables:

```python
o, m = fruits[1:3]
print(o, m)  # Output: orange mango
```

---

### Concatenating Tuples

You can combine multiple tuples using the `+` operator:

```python
fruits = ('banana', 'orange', 'mango', 'lemon', 'orange')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegest = fruits + vegetables
print(fruits_and_vegest)
```

This concatenates the `fruits` and `vegetables` tuples into a single tuple.

Example: Counting Occurrences

You can count how many times an item appears in a tuple:

```python
print(fruits.count('lemon'))  # Output: 1
```

---

### Iterating Through Combined Tuples

You can iterate over the combined tuple just like any other iterable:

```python
for item in fruits_and_vegest:
    print(item)
```

This prints each item from the combined `fruits_and_vegest` tuple.

---

### Converting Tuples to Lists

Although tuples are immutable, you can convert them into lists if you need to modify their contents:

```python
fruits_lst = list(fruits)
print(fruits_lst)  # Output: ['banana', 'orange', 'mango', 'lemon', 'orange']
```

Example: Enumerating a List

You can also use the `enumerate()` function to get both the index and value while iterating:

```python
print(list(enumerate(fruits_lst)))  
# Output: [(0, 'banana'), (1, 'orange'), (2, 'mango'), (3, 'lemon'), (4, 'orange')]
```

---

### Enumerating with a Custom Start Index

You can specify a starting index when using `enumerate()`:

```python
for index, value in enumerate(['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']):
    print(f'{index + 1}. {value}')
```

This will output the countries with a custom starting index:

```sh
1. Finland
2. Sweden
3. Norway
4. Denmark
5. Iceland
```

---

## Tuples Summary

Tuples are a crucial data structure in Python, offering a way to store collections of items that are ordered and immutable. Understanding how to create, access, and manipulate tuples is essential for effective programming in Python, especially when working with fixed collections of data.

## Dictionaries in Python

Dictionaries are one of the fundamental data structures in Python, allowing you to store data in key-value pairs. This reading material will provide a comprehensive overview of dictionaries, including their properties, methods, and usage through examples.

---

### What is a Dictionary?

A **dictionary** is a mutable, unordered collection of items, where each item is stored as a key-value pair. This structure allows for efficient data retrieval and manipulation based on unique keys.

Example: Creating an Empty Dictionary

```python
# Creating an empty dictionary
empty_dict = {}  # Alternatively: empty_dict = dict()
print(type(empty_dict), len(empty_dict))  # Output: <class 'dict'> 0
```

In this example, an empty dictionary is created, and its type and length are printed.

---

### Key-Value Structure

Each item in a dictionary consists of a key and its associated value. You can think of it as a real-life dictionary, where each word (key) has a definition (value).

Example: Defining a Person Dictionary

```python
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'is_married': True,
    'address': {
        'country': 'Finland',
        'city': 'Espoo',
        'zipcode': '02770',
        'street': 'Space street'
    },
    'skills': ['HTML', 'CSS', 'JavaScript', 'Python', 'NumPy', 'TextBlob', 'Flask', 'MySQL'],
    'educations': [
        {
            'name': 'Helsinki Metropolia University of Applied Science',
            'qualification': 'BEng.',
            'field': 'Information Technology',
            'starting_year': 2012,
            'ending_year': 2017
        },
        {
            'name': 'Helsinki University',
            'qualification': 'MSc.',
            'field': 'Computer Science',
            'starting_year': 2017,
            'ending_year': 2017
        }
    ]
}
```

In this example, a dictionary named `person` is defined, containing various key-value pairs, including nested dictionaries and lists.

---

### Accessing Dictionary Items

You can access the values in a dictionary by using their keys:

```python
print(person)  # Prints the entire dictionary
print(len(person))  # Output: Number of key-value pairs in the dictionary
print(person['first_name'])  # Output: Asabeneh
print(person['address']['country'])  # Output: Finland
```

You can also use the `get()` method to access values. This method returns `None` if the key is not found, instead of raising an error:

```python
print(person.get('nationality'))  # Output: None
```

### Adding New Key-Value Pairs

You can add new items to the dictionary by assigning a value to a new key:

```python
person['nationality'] = 'Ethiopian'
print(person)  # Prints the updated dictionary
```

---

### Modifying and Appending Data

You can modify existing values or append new data to lists within the dictionary:

```python
print(person.get('nationality'))  # Output: Ethiopian
print(len(person))  # Output: Updated count of key-value pairs
person['hobbies'] = []  # Adding a new key with an empty list
print(person)

# Appending items to the hobbies list
person['hobbies'].append('Ice skating')
person['hobbies'].append('Running')

print(person)  # Prints the dictionary with updated hobbies
```

---

### Iterating Through a Dictionary

You can iterate through the keys and values of a dictionary using a loop:

```python
for item in person:
    print(item, person[item])
```

Example: Using the `items()` Method

The `items()` method returns a view object displaying a list of a dictionary's key-value tuple pairs:

```python
items = person.items()
print(items)

for key, value in items:
    print(key, value)  # Prints each key-value pair
```

### Getting Keys and Values

You can retrieve all the keys or values from a dictionary using the `keys()` and `values()` methods, respectively:

```python
keys = person.keys()
print(keys)  # Prints all keys in the dictionary

values = person.values()
print(values)  # Prints all values in the dictionary
```

---

## Dictionaries Summary

Dictionaries are a powerful and flexible data structure in Python, allowing for the storage of key-value pairs. Their mutability and ability to nest other data structures make them an essential tool for managing and organizing data effectively. Understanding how to create, access, and manipulate dictionaries is crucial for effective programming in Python.

[<< WEEK 3](../WEEK-3/week-3.md) | [WEEK 5 >>](../WEEK-5/week-5.md)
