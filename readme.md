# Python Programming

- [Python Programming](#python-programming)
  - [Introduction to Python Programming](#introduction-to-python-programming)
    - [Installing Python](#installing-python)
    - [Interactive Python Shell](#interactive-python-shell)
    - [Installing Visual Studio Code](#installing-visual-studio-code)
    - [Setting Up Python in Visual Studio Code](#setting-up-python-in-visual-studio-code)
    - [Writing Your First Python Program in VS Code](#writing-your-first-python-program-in-vs-code)
    - [Python Comments](#python-comments)
      - [Single-Line Comments](#single-line-comments)
      - [Multiline Comments (Docstrings)](#multiline-comments-docstrings)
    - [Summary](#summary)
  - [Python Built-in Functions](#python-built-in-functions)
    - [The `print()` Function](#the-print-function)
    - [The `len()` Function](#the-len-function)
    - [The `type()` Function](#the-type-function)
    - [The `input()` Function](#the-input-function)
    - [The `range()` Function](#the-range-function)
    - [Built-in Functions](#built-in-functions)
    - [The `abs()`, `min()`, `max()`, and `sum()` Functions](#the-abs-min-max-and-sum-functions)
    - [The `enumerate()` Function](#the-enumerate-function)
    - [The `dir()` Function](#the-dir-function)
    - [Builtin Functions Summary](#builtin-functions-summary)

[WEEK 2 >>](./WEEK-2/week-2.md)

## Introduction to Python Programming

Python is a versatile and beginner-friendly programming language known for its simplicity and readability. It's widely used in various fields, such as web development, data science, automation, and artificial intelligence. This guide will walk you through setting up Python, running an interactive shell, installing Visual Studio Code (VS Code), and writing your first Python program: `"Hello World!"`.

### Installing Python

Before writing any Python code, you need to install Python on your computer. Follow these steps:

- **Step 1:** Go to the [official Python website](https://www.python.org/).
- **Step 2:** Click on the **Downloads** section and choose the version for your operating system (Windows, macOS, or Linux).
- **Step 3:** Run the downloaded installer.
  - For Windows users, during installation, make sure to check the box labeled **"Add Python to PATH"**. This makes running Python from the command line easier.
- **Step 4:** Verify the installation by opening a terminal (Command Prompt for Windows, or Terminal for macOS/Linux) and typing:

  ```bash
  python --version
  ```

  You should see the installed Python version printed.

### Interactive Python Shell

Python comes with an interactive shell that allows you to run Python commands immediately. Here's how to open it:

- **Step 1:** Open your terminal or command prompt.
- **Step 2:** Type `python` (or `python3` on some systems) and hit **Enter**. This will start the Python shell.
  
You’ll see a prompt like this:

```python
Python 3.x.x (default, Mar 18 2021, 13:41:09)
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

This is the Python interactive shell, where you can run Python commands directly. Try typing:

```python
print('Hello World!')
```

It should print:

```python
Hello World!
```

You’ve just written your first Python program in the interactive shell!

### Installing Visual Studio Code

To write more complex Python programs, you’ll want to use a code editor like Visual Studio Code (VS Code). Follow these steps to install and set up VS Code:

- **Step 1:** Go to the [Visual Studio Code website](https://code.visualstudio.com/).
- **Step 2:** Download the appropriate version for your operating system (Windows, macOS, or Linux).
- **Step 3:** Run the installer and follow the setup instructions.
- **Step 4:** Once installed, open VS Code.

### Setting Up Python in Visual Studio Code

Now, let's set up Python in VS Code.

- **Step 1:** Install the Python extension for VS Code:
  - Open VS Code and click on the **Extensions** icon (on the left-hand toolbar).
  - Search for "Python" and install the official Python extension by Microsoft.

- **Step 2:** Ensure VS Code is using the correct Python interpreter:
  - Press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (macOS) to open the Command Palette.
  - Type `Python: Select Interpreter` and choose the Python version you installed.

### Writing Your First Python Program in VS Code

Let’s write the same `"Hello World!"` program in VS Code.

- **Step 1:** Create a new file in VS Code by selecting **File > New File**.
- **Step 2:** Save the file with a `.py` extension (e.g., `hello.py`).
- **Step 3:** Write the following code in the file:

  ```python
  print('Hello World!')
  ```

- **Step 4:** Run the Python code:
  - You can run it directly within VS Code by pressing `Ctrl+F5` (Windows) or `Cmd+F5` (macOS).
  - Alternatively, open the terminal within VS Code (`Ctrl+` `) and type:

      ```bash
      python hello.py
      ```

You should see the output:

```bash
Hello World!
```

Congratulations! You've successfully set up Python, learned how to use the interactive shell, installed VS Code, and written your first Python program. This is just the beginning of your Python journey!

---

### Python Comments

In Python, comments are an essential part of writing clean and understandable code. Comments help both the programmer and others understand what the code is doing. Python supports two types of comments: **single-line comments** and **multiline comments**. In this section, we will explain these comment types and the `print()` function.

#### Single-Line Comments

A **single-line comment** in Python begins with a hash symbol (`#`). Everything following the hash on that line is considered a comment and is ignored by the Python interpreter.

**Single Line Comment Example:**

```python
# A hash symbol is a single line comment
# The purpose of a comment is to make our code readable and maintainable
```

In this example, both lines are comments and will not be executed. They exist to describe the purpose of the code that follows, helping the programmer understand what’s happening.

```python
# The `print()` function is used to display output on the screen. It can take one or more arguments and print them, separated by spaces.
print('Hello', 'World', 2024, 'Data Analysis with Python - Autumn 2024')
```

**Explanation:**

- This line of code prints four separate items: `'Hello'`, `'World'`, `2024`, and `'Data Analysis with Python - Autumn 2024'`.
- The `print()` function separates each of these inputs by a space and displays them in a single line:
  
```sh
  Hello World 2024 Data Analysis with Python - Autumn 2024
```

You can pass any combination of data types (strings, integers, etc.) to `print()`, and it will display them on the console.

#### Multiline Comments (Docstrings)

In Python, you can create **multiline comments** by enclosing the comment text within triple quotes (`'''` or `"""`). These are often used for longer explanations or documentation. Multiline comments are sometimes referred to as **docstrings**, especially when used inside functions or classes to document their purpose.

**Multiline Comment Example**:

```python
'''
A multiline comment allows us to write a comment
on several lines and
sometimes it can be used as good documentation
'''
```

or

```python
"""
A multiline comment allows us to write a comment
on several lines and
sometimes it can be used as good documentation
"""
```

**Explanation:**

- Both single quotes (`'''`) and double quotes (`"""`) can be used to write multiline comments. The choice between them is a matter of preference and style.
- These multiline comments are helpful for providing detailed explanations of code or for documenting larger sections.

### Summary

- **Single-line comments** (`#`) are useful for short, concise comments.
- **Multiline comments** (`'''` or `"""`) are helpful for more extensive explanations or documentation.
- The `print()` function is a fundamental tool for displaying outputs, allowing multiple arguments separated by spaces to be printed in a single line.

By using comments effectively, you can make your code more readable and maintainable, while the `print()` function provides an easy way to output text and other data types during the execution of your Python programs.

---

## Python Built-in Functions

In Python, functions are a key tool for writing reusable and modular code. There are two main types of functions in Python: **built-in functions** and **custom functions**.

- **Built-in Functions**: Predefined functions that are available in Python without the need to import any external modules.
- **Custom Functions**: Functions defined by the user to solve specific problems or perform specific tasks.

This document focuses on various **built-in functions** in Python, including how to use them and what they do.

---

###  The `print()` Function

The `print()` function is one of the most commonly used built-in functions in Python. It displays the output of any data type (integers, strings, lists, etc.) on the screen.

```python
print(10, type(10))
print(9.81, type(9.81))
print('Asabeneh Yetayeh', 'Finland', 'Helsinki', 250, ['HTML', 'CSS', 'JS'], sep=', ')
```

**Explanation**:

- `print()` takes any number of arguments and prints them, separated by spaces by default. You can customize the separator using the `sep` parameter.
- `type()` shows the type of the data passed to it, like integer, float, string, etc.

Output:

```sh
10 <class 'int'>
9.81 <class 'float'>
Asabeneh Yetayeh, Finland, Helsinki, 250, ['HTML', 'CSS', 'JS']
```

---

### The `len()` Function

The `len()` function returns the number of items in a sequence (like strings, lists, etc.).

```python
print(len('cat'))
print(len('Finland'))
```

**Explanation**:

- `len()` works on any sequence type such as strings, lists, tuples, etc., and returns the length.

Output:

```sh
3
7
```

---

### The `type()` Function

The `type()` function returns the type of a given object.

```python
print(10, type(10))
print(1 + 4j, type(1 + 4j))
```

**Explanation**:

- `type()` shows the data type of any object, whether it's an integer, float, complex number, string, etc.

---

### The `input()` Function

The `input()` function is used to take input from the user.

```python
name = input('Enter your name: ')
print('Hello, ' + name)
```

**Explanation**:

- `input()` takes a string as a prompt and waits for the user to input text. The input is always returned as a string.

---

### The `range()` Function

The `range()` function generates a sequence of numbers, which can be converted into a list or iterated through.

```python
print(list(range(0, 10)))
print(list(range(0, 101, 2)))
```

**Explanation**:

- `range(start, end, step)` generates a sequence of numbers from `start` to `end-1`, with a step increment of `step`.
- You can convert a range object into a list using `list()`.

---

### Built-in Functions

Python provides various built-in functions for working with data types like **lists**, **sets**, **dictionaries**, and **tuples**.

```python
print(set(['English', 'French', 'Finnish', 'Swedish', 'Finnish']))
print(dict(name='Asab', age=250))
```

**Explanation**:

- `set()` creates a set, removing duplicates.
- `dict()` creates a dictionary with key-value pairs.

---

### The `abs()`, `min()`, `max()`, and `sum()` Functions

These built-in functions perform basic mathematical operations.

```python
print(abs(-5))
print(min(-2, 10, 5, 20))
print(max(-2, 10, 5, 20))
print(sum([1, 2, 3, 4, 5]))
```

**Explanation**:

- `abs()` returns the absolute value.
- `min()` and `max()` return the smallest and largest values, respectively.
- `sum()` adds up all elements in a list.

---

### The `enumerate()` Function

The `enumerate()` function adds a counter to an iterable (like a list) and returns it as an enumerate object.

```python
countries = ['Finland', 'Sweden', 'Norway']
print(list(enumerate(countries)))
```

**Explanation**:

- `enumerate()` is useful when you need to iterate over a list while keeping track of the index.

---

### The `dir()` Function

The `dir()` function returns a list of all attributes and methods available for an object.

```python
print(dir('hello'))
```

**Explanation**:

- `dir()` helps you explore the methods associated with a particular object, such as a string, list, or function.

---

### Builtin Functions Summary

- Python's built-in functions like `print()`, `len()`, `input()`, and `range()` are powerful tools for solving common problems and tasks.
- Functions like `abs()`, `min()`, `max()`, `sum()`, and `enumerate()` are useful for working with numbers and sequences.
- Python's data types—lists, sets, dictionaries, and tuples—can be manipulated easily using functions like `list()`, `set()`, `dict()`, etc.

Understanding and effectively using these built-in functions is a fundamental part of programming in Python

---

[WEEK 2 >>](./WEEK-2/week-2.md)
