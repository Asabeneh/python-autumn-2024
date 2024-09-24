
- [Python Conditional Statements](#python-conditional-statements)
  - [If and else](#if-and-else)
  - [Match case](#match-case)
- [String and String Operations](#string-and-string-operations)
  - [String Indexing](#string-indexing)
  - [String Slicing](#string-slicing)
  - [String Methods](#string-methods)
  - [String Formatting](#string-formatting)
    - [Handling Large Texts](#handling-large-texts)
    - [Conclusion](#conclusion)
- [Python Lists](#python-lists)
  - [List Characteristics](#list-characteristics)
  - [Creating an Empty List](#creating-an-empty-list)
  - [Common List Methods](#common-list-methods)
  - [Accessing List Elements](#accessing-list-elements)
  - [Modifying Lists](#modifying-lists)
  - [Adding Elements](#adding-elements)
  - [Removing Elements](#removing-elements)
  - [Inserting Elements](#inserting-elements)
  - [Counting and Reversing Elements](#counting-and-reversing-elements)
  - [Sorting Lists](#sorting-lists)
- [List Summary](#list-summary)

[<< WEEK 2](../readme.md) | [WEEK 4 >>](../WEEK-4/week-4.md)

## Python Conditional Statements

This Python code demonstrates basic conditional statements (`if`, `elif`, `else`) and introduces a newer pattern-matching approach (`match-case`) for handling specific conditions, often preferred in Python 3.10 and later.

### If and else

**Checking If a Number Is Positive, Negative, or Zero:**

```python
a = 5

if a > 0:
    print('The number is positive')
elif a < 0:
    print('The number is negative')
else:
    print('the number is zero')
```

**Explanation:**

- This block of code checks whether the variable `a` is positive, negative, or zero using `if`, `elif`, and `else` statements.
- The `if` condition checks if the number is greater than 0. If true, it prints `"The number is positive"`.
- If the number isn't positive, the `elif` condition checks if it's negative. If true, it prints `"The number is negative"`.
- If neither of the two conditions is true, the `else` statement is executed, printing `"The number is zero"`.

**Checking If It’s Raining:**

```python
is_raining = False 

if is_raining:
    print('Go out with an umbrella')
else:
    print('Go out freely it is a shinny day!')
```

**Explanation:**

- This section checks the Boolean value `is_raining`.
- If `is_raining` is `True`, it advises going out with an umbrella.
- If `is_raining` is `False`, it prints a message suggesting going out freely because it’s a sunny day.

**Weather Conditions Using `if-elif-else`:**

```python
weather = input('What is the weather today? ').lower()

if weather == 'rainy':
    print('Go with an unbrella or a raincoat')
elif weather == 'cloudy':
    print('It may rain and consider a raincoat')
elif weather == 'snowy':
    print('It may be slippery')
elif weather == 'foggy':
    print('Visiblity might be hindered')
elif weather == 'sunny':
    print('It is a great day to go to the beach')
else:
    print('No one knows about the weather')

print('test it')

```

**Explanation:**

- This commented-out section (enclosed in triple quotes) takes the user's input for the weather and performs multiple checks using `if-elif-else`.
- Based on the weather condition provided, it prints appropriate advice for going outside.

### Match case

**Weather Conditions Using `match-case`:**

```python
weather = input('What is the weather today? ').lower()
match weather:
    case 'rainy':
        print('Go with an unbrella or a raincoat')
    case 'cloudy':
        print('It may rain and consider a raincoat')
    case 'snowy':
        print('It may be slippery')
    case 'foggy':
        print('Visiblity might be hindered')
    case 'sunny':
        print('It is a great day to go to the beach')
    case _:
        print('No one knows about the weather')
```

**Explanation:**

- This block uses the `match-case` structure, introduced in Python 3.10, which provides a more efficient and readable way to handle multiple conditions, replacing a chain of `if-elif-else` statements.
- The `match` keyword checks the value of the `weather` variable and matches it against specific cases (`'rainy'`, `'cloudy'`, etc.).
- If no match is found, the default case (`case _`) is executed, printing `"No one knows about the weather"`.

**Key Takeaways**:

- **Conditional Statements (`if-elif-else`)**: Useful for checking multiple conditions and executing different blocks of code based on those conditions.
- **Pattern Matching (`match-case`)**: A more modern and efficient way to handle conditions that involve multiple specific cases, improving readability, especially for many branches.

## String and String Operations

- A string is a sequence of characters enclosed within single, double, or triple quotes.
- This documentation illustrates various string operations, slicing, methods, and formatting using Python.

**Example: Basic String Declaration and Operations**:

```python
letter = 'a'
print(type(letter), len(letter))  # Output: <class 'str'> 1

alphabets = 'abcdefghijklmnopqrstuvwxyz'
print(alphabets, len(alphabets))  # Output: 'abcdefghijklmnopqrstuvwxyz', 26
print(list(alphabets))  # Converts the string into a list of characters
```

### String Indexing

- Python strings support indexing, allowing access to individual characters by their position.

```python
lang = 'Python'
print(lang[0])  # Output: 'P'
print(lang[-1])  # Output: 'n'
```

### String Slicing

- Slicing allows for extracting a portion of the string.

```python
print(lang[0:2])  # Output: 'Py' (slices from index 0 to 2, not including index 2)
print(lang[-4:-1])  # Output: 'tho' (slices from index -4 to -1)
```

### String Methods

Python provides a variety of string methods for common tasks:

- **String Methods List**:
  - `'capitalize'`, `'upper'`, `'lower'`, `'title'`, `'strip'`, `'replace'`, `'find'`, `'split'`, `'join'`, `'startswith'`, `'endswith'` etc.

```python
txt = 'Python for everyone'
print(txt.upper())  # Output: 'PYTHON FOR EVERYONE'
print(txt.lower())  # Output: 'python for everyone'
print(txt.capitalize())  # Output: 'Python for everyone'
```

### String Formatting

- Python provides several ways to format strings:

1. **Using `+` operator**:

   ```python
   full_name = first_name + ' ' + last_name
   print(full_name)  # Concatenates strings
   ```

2. **Using `format()`**:

   ```python
   print('I am {} {}. I am {} years old.'.format(first_name, last_name, age))
   ```

3. **Using f-strings**:

   ```python
   formated_string = f'I am {first_name} {last_name}. I teach {language}.'
   print(formated_string)
   ```

**Working with DNA Sequence (String Operations)**:

- Count the occurrences of specific characters in a DNA string and calculate their frequency.

```python
dna = '''CTAGCAAACTGCTGAT...'''  # (trimmed for brevity)
total = len(dna)
a = dna.count('A')
c = dna.count('C')
t = dna.count('T')
g = dna.count('G')
print(a / total, c / total, t / total, g / total)  # Output: Frequencies of A, C, T, G
```

**Additional Examples:**

- **String Replacement**:

   ```python
   print('I love people'.replace('love', 'like'))  # Output: 'I like people'
   ```

- **String Searching**:

   ```python
   txt = 'Python for everyone'
   print(txt.find('y'))  # Output: 1 (position of first 'y')
   print(txt.index('P'))  # Output: 0
   ```

#### Handling Large Texts

- A sample speech from Donald Trump is processed by splitting it into words, converting them to lowercase, and removing punctuation.
- Then, unique words are identified using a set.

```python
donald_speech = '''Chief Justice Roberts, President...'''  # (trimmed for brevity)
words = donald_speech.lower().replace('–', ' ').replace('.', ' ').split()
unique_words = set(words)
print(len(unique_words))  # Output: Count of unique words
```

#### Conclusion

This document covers the basics of string manipulation in Python, including indexing, slicing, methods, and formatting techniques. These concepts are essential for processing text data efficiently in Python.

## Python Lists

This document explains basic operations and methods related to lists in Python, including list creation, accessing elements, and using built-in list methods.

### List Characteristics

- A list is a collection of items, which are **indexed** and **ordered**.
- Lists are **mutable**, meaning the elements can be changed after the list is created.

### Creating an Empty List

You can create an empty list using the `list()` constructor.

```python
empty_list = list()
print(len(empty_list), empty_list)  # Outputs the length and the empty list
print(type(empty_list))  # Shows the type as <class 'list'>
print(dir(empty_list))  # Lists all methods available for the list object
```

### Common List Methods

A list of some of the most common list methods in Python:

```python
lst_methods = ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

### Accessing List Elements

A list of numbers is created. You can access elements using their index.

```python
nums = [1, 2, 3, 4, 5]
print(nums, len(nums))  # Prints the list and its length
print(nums[0])  # Accesses the first element
print(nums[1])  # Accesses the second element
print(nums[4])  # Accesses the last element using its positive index

# Accessing the last element using negative indexing
print(nums[-1])

# Slicing the list
print(nums[1:4])  # Prints elements from index 1 to 3
print(nums[2:])  # Prints from index 2 to the end
print(nums[:3])  # Prints elements from the start to index 2
```

### Modifying Lists

You can modify lists by adding, inserting, or removing elements.

### Adding Elements

- **append()**: Adds an item to the end of the list.
- **extend()**: Adds multiple items to the list.
  
```python
# nums.append(6)
# nums.extend([7, 8, 9, 10])
```

### Removing Elements

- **pop()**: Removes and returns an element at the given index. If no index is provided, it removes the last element.
- **del**: Deletes an element or a slice of the list.
  
```python
# nums.pop()  # Removes the last element
# nums.pop(0)  # Removes the first element
# del nums[4]  # Deletes the element at index 4
```

### Inserting Elements

- **insert()**: Inserts an item at a given position.

```python
nums.insert(3, 333)  # Inserts 333 at index 3
nums.insert(6, 'the last item')  # Inserts a string at index 6
```

### Counting and Reversing Elements

- **count()**: Returns the count of occurrences of a value in the list.
- **reverse()**: Reverses the order of the list.

```python
countries = ['Finland', 'Finland', 'Finland', 'Denmark', 'Norway', 'Finland', 'Finland', 'Sweden']
print(countries.count('Finland'))  # Counts how many times 'Finland' appears

copy_lst = nums.copy()  # Copies the list
copy_lst.reverse()  # Reverses the copied list
print(copy_lst)
```

### Sorting Lists

Lists can be sorted in ascending or descending order.

- **sort()**: Sorts the list in place.
- **sorted()**: Returns a sorted copy of the list.

```python
new_num = [25, 20, 10, 3, 5, 0, 24]
print(sorted(new_num))  # Returns a sorted list in ascending order
print(sorted(new_num, reverse=False))  # Sorts without reversing
```

## List Summary

This document covered the following list operations:

- Creating and accessing elements in lists.
- Adding, inserting, and removing elements.
- Counting and reversing elements.
- Sorting lists using `sorted()` and `sort()`.

[<< WEEK 2](../readme.md) | [WEEK 4 >>](../WEEK-4/week-4.md)
