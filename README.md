# Basic Python Programs - Comprehensive Guide

A collection of fundamental Python programs with detailed explanations, suitable for beginners learning Python basics.

---

## Table of Contents
1. [Hello World & Basic Output](#1-hello-world--basic-output)
2. [Variables and Data Types](#2-variables-and-data-types)
3. [User Input](#3-user-input)
4. [Arithmetic Operations](#4-arithmetic-operations)
5. [String Operations](#5-string-operations)
6. [Conditional Statements](#6-conditional-statements)
7. [Loops](#7-loops)
8. [Lists and Collections](#8-lists-and-collections)
9. [Functions](#9-functions)
10. [Dictionaries](#10-dictionaries)

---

## 1. Hello World & Basic Output

### Program 1.1: Simple Hello World
```python
# This is a comment - it doesn't execute
print("Hello, World!")
```

**Output:**
```
Hello, World!
```

**Explanation:**
- `print()` is a built-in function that displays text to the terminal
- Text is enclosed in quotes (single or double)
- Comments start with `#` and are ignored by Python

---

### Program 1.2: Multiple Print Statements
```python
print("Welcome to Python!")
print("This is my first program")
print("Learning Python is fun")
```

**Output:**
```
Welcome to Python!
This is my first program
Learning Python is fun
```

**Explanation:**
- Each `print()` statement creates a new line
- You can call `print()` multiple times

---

### Program 1.3: Print Multiple Items on One Line
```python
# Using multiple arguments in print()
print("Name:", "John", "Age:", 28)

# Using f-strings
name = "Alice"
age = 25
print(f"{name} is {age} years old")
```

**Output:**
```
Name: John Age: 28
Alice is 25 years old
```

**Explanation:**
- Separate values with commas in `print()` to display them with spaces between
- F-strings embed variables using `{variable_name}`

---

## 2. Variables and Data Types

### Program 2.1: Working with Variables
```python
# Integer
age = 28
print(f"Age: {age}")

# Float (decimal number)
height = 5.9
print(f"Height: {height}")

# String
name = "John Doe"
print(f"Name: {name}")

# Boolean (True/False)
is_student = True
print(f"Is Student: {is_student}")
```

**Output:**
```
Age: 28
Height: 5.9
Name: John Doe
Is Student: True
```

**Explanation:**
- **int**: Whole numbers (28, 100, -5)
- **float**: Decimal numbers (5.9, 3.14)
- **str**: Text (enclosed in quotes)
- **bool**: True or False values

---

### Program 2.2: Type Checking
```python
# Check the type of a variable using type()
age = 28
name = "Alice"
price = 19.99

print(type(age))        # <class 'int'>
print(type(name))       # <class 'str'>
print(type(price))      # <class 'float'>
```

**Output:**
```
<class 'int'>
<class 'str'>
<class 'float'>
```

---

### Program 2.3: Type Conversion
```python
# Convert between types
age_string = "25"
age_int = int(age_string)      # Convert string to integer
print(f"Original: {age_string} (type: {type(age_string).__name__})")
print(f"Converted: {age_int} (type: {type(age_int).__name__})")

# Convert number to string
number = 42
number_string = str(number)
print(f"Number as string: '{number_string}'")

# Convert to float
converted_float = float("3.14")
print(f"Float: {converted_float}")
```

**Output:**
```
Original: 25 (type: str)
Converted: 25 (type: int)
Number as string: '42'
Float: 3.14
```

---

## 3. User Input

### Program 3.1: Getting Input from User
```python
# Get input from user
name = input("What is your name? ")
print(f"Hello, {name}!")

age = input("How old are you? ")
# Note: input() always returns a string, even for numbers
print(f"You are {age} years old")
```

**Sample Interaction:**
```
What is your name? Alice
Hello, Alice!
How old are you? 25
You are 25 years old
```

**Explanation:**
- `input()` displays a prompt and waits for user input
- Returns the input as a string
- Always convert to appropriate type if needed

---

### Program 3.2: Collecting Multiple Inputs
```python
# Collect user information
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
age = int(input("Enter age: "))  # Convert to integer
email = input("Enter email: ")

# Display collected information
print("\n--- Your Information ---")
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Email: {email}")
```

**Sample Interaction:**
```
Enter first name: John
Enter last name: Doe
Enter age: 28
Enter email: john@example.com

--- Your Information ---
Name: John Doe
Age: 28
Email: john@example.com
```

---

## 4. Arithmetic Operations

### Program 4.1: Basic Math Operations
```python
# Arithmetic operators
a = 15
b = 4

# Addition
print(f"{a} + {b} = {a + b}")       # 15 + 4 = 19

# Subtraction
print(f"{a} - {b} = {a - b}")       # 15 - 4 = 11

# Multiplication
print(f"{a} * {b} = {a * b}")       # 15 * 4 = 60

# Division
print(f"{a} / {b} = {a / b}")       # 15 / 4 = 3.75

# Floor Division (rounds down)
print(f"{a} // {b} = {a // b}")     # 15 // 4 = 3

# Modulus (remainder)
print(f"{a} % {b} = {a % b}")       # 15 % 4 = 3

# Exponentiation (power)
print(f"{a} ** {b} = {a ** b}")     # 15 ** 4 = 50625
```

**Output:**
```
15 + 4 = 19
15 - 4 = 11
15 * 4 = 60
15 / 4 = 3.75
15 // 4 = 3
15 % 4 = 3
15 ** 4 = 50625
```

---

### Program 4.2: Calculate Average
```python
# Get numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calculate average
average = (num1 + num2 + num3) / 3

print(f"\nNumbers: {num1}, {num2}, {num3}")
print(f"Average: {average:.2f}")
```

**Sample Interaction:**
```
Enter first number: 85
Enter second number: 90
Enter third number: 95

Numbers: 85.0, 90.0, 95.0
Average: 90.00
```

**Explanation:**
- `.2f` formats the result to 2 decimal places

---

### Program 4.3: Simple Calculator
```python
# Simple calculator
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"
else:
    result = "Error: Invalid operation"

print(f"\n{num1} {operation} {num2} = {result}")
```

**Sample Interaction:**
```
Enter first number: 20
Enter operation (+, -, *, /): *
Enter second number: 5

20.0 * 5.0 = 100.0
```

---

## 5. String Operations

### Program 5.1: String Concatenation
```python
first_name = "John"
last_name = "Doe"

# Method 1: Using +
full_name1 = first_name + " " + last_name
print(f"Method 1: {full_name1}")

# Method 2: Using f-string (recommended)
full_name2 = f"{first_name} {last_name}"
print(f"Method 2: {full_name2}")

# Method 3: Using .format()
full_name3 = "{} {}".format(first_name, last_name)
print(f"Method 3: {full_name3}")
```

**Output:**
```
Method 1: John Doe
Method 2: John Doe
Method 3: John Doe
```

---

### Program 5.2: String Slicing
```python
text = "Python Programming"

# Get specific characters
print(f"First character: {text[0]}")          # P
print(f"Last character: {text[-1]}")          # g

# Slice a range
print(f"First 6 characters: {text[0:6]}")     # Python
print(f"Characters 7-18: {text[7:18]}")       # Programming
print(f"Last 3 characters: {text[-3:]}")      # ing

# Every 2nd character
print(f"Every 2nd character: {text[::2]}")    # Pto rgamn
```

**Output:**
```
First character: P
Last character: g
First 6 characters: Python
Characters 7-18: Programming
Last 3 characters: ing
Every 2nd character: Pto rgamn
```

---

### Program 5.3: String Methods
```python
text = "Hello World"

# Convert case
print(f"Uppercase: {text.upper()}")           # HELLO WORLD
print(f"Lowercase: {text.lower()}")           # hello world

# Check content
print(f"Starts with 'Hello': {text.startswith('Hello')}")    # True
print(f"Ends with 'World': {text.endswith('World')}")        # True
print(f"Contains 'World': {'World' in text}")                # True

# Find and replace
print(f"Find index of 'World': {text.find('World')}")        # 6
print(f"Replace 'World' with 'Python': {text.replace('World', 'Python')}")
# Hello Python

# Strip whitespace
padded_text = "  Hello  "
print(f"Stripped: '{padded_text.strip()}'")   # 'Hello'
```

**Output:**
```
Uppercase: HELLO WORLD
Lowercase: hello world
Starts with 'Hello': True
Ends with 'World': True
Contains 'World': True
Find index of 'World': 6
Replace 'World' with 'Python': Hello Python
Stripped: 'Hello'
```

---

## 6. Conditional Statements

### Program 6.1: If-Else Statements
```python
# Check if number is positive, negative, or zero
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("The number is zero")
```

**Sample Interaction:**
```
Enter a number: 10
10 is positive
```

---

### Program 6.2: Check Age and Grade
```python
# Simple age checker
age = int(input("Enter your age: "))

if age < 13:
    category = "Child"
elif age < 18:
    category = "Teenager"
elif age < 65:
    category = "Adult"
else:
    category = "Senior"

print(f"You are a {category}")
```

**Sample Interaction:**
```
Enter your age: 25
You are a Adult
```

---

### Program 6.3: Even or Odd Checker
```python
# Check if number is even or odd
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

**Sample Interaction:**
```
Enter a number: 7
7 is odd
```

---

### Program 6.4: Grade Calculator
```python
# Calculate letter grade based on score
score = int(input("Enter your score (0-100): "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your score: {score}")
print(f"Your grade: {grade}")
```

**Sample Interaction:**
```
Enter your score (0-100): 85
Your score: 85
Your grade: B
```

---

## 7. Loops

### Program 7.1: For Loop - Print Numbers
```python
# Print numbers 1 to 5
for i in range(1, 6):
    print(i)
```

**Output:**
```
1
2
3
4
5
```

**Explanation:**
- `range(1, 6)` generates numbers from 1 to 5 (6 is exclusive)
- `i` is the loop variable that takes each value

---

### Program 7.2: For Loop with List
```python
# Loop through a list of names
names = ["Alice", "Bob", "Charlie", "Diana"]

for name in names:
    print(f"Hello, {name}!")
```

**Output:**
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, Diana!
```

---

### Program 7.3: While Loop - Countdown
```python
# Countdown from 5 to 1
number = 5

while number > 0:
    print(number)
    number = number - 1

print("Blast off!")
```

**Output:**
```
5
4
3
2
1
Blast off!
```

**Explanation:**
- While loop continues as long as condition is True
- `number = number - 1` decreases the number each iteration

---

### Program 7.4: Multiplication Table
```python
# Print multiplication table
n = int(input("Enter a number: "))

print(f"\nMultiplication table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

**Sample Interaction:**
```
Enter a number: 5

Multiplication table of 5:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```

---

### Program 7.5: Sum Numbers Using Loop
```python
# Sum numbers from 1 to 10
total = 0

for i in range(1, 11):
    total = total + i

print(f"Sum of numbers 1 to 10: {total}")
```

**Output:**
```
Sum of numbers 1 to 10: 55
```

---

### Program 7.6: Loop with Break and Continue
```python
# Using break to exit loop
print("Numbers with break:")
for i in range(1, 6):
    if i == 3:
        break  # Exit the loop
    print(i)

print("\nNumbers with continue:")
for i in range(1, 6):
    if i == 3:
        continue  # Skip this iteration
    print(i)
```

**Output:**
```
Numbers with break:
1
2

Numbers with continue:
1
2
4
5
```

---

## 8. Lists and Collections

### Program 8.1: Creating and Accessing Lists
```python
# Create a list
numbers = [10, 20, 30, 40, 50]
fruits = ["Apple", "Banana", "Cherry"]

# Access elements by index
print(f"First number: {numbers[0]}")         # 10
print(f"Last number: {numbers[-1]}")         # 50
print(f"Second fruit: {fruits[1]}")          # Banana

# List length
print(f"Number of fruits: {len(fruits)}")    # 3
```

**Output:**
```
First number: 10
Last number: 50
Second fruit: Banana
Number of fruits: 3
```

---

### Program 8.2: List Operations
```python
# Create a list
colors = ["Red", "Green", "Blue"]

# Add elements
colors.append("Yellow")              # Add to end
colors.insert(1, "Orange")           # Add at specific position

print(f"After adding: {colors}")
# ['Red', 'Orange', 'Green', 'Blue', 'Yellow']

# Remove elements
colors.remove("Orange")              # Remove by value
print(f"After removing Orange: {colors}")

# Pop element (remove and return)
last_color = colors.pop()            # Remove last element
print(f"Removed: {last_color}")
print(f"Remaining: {colors}")
```

**Output:**
```
After adding: ['Red', 'Orange', 'Green', 'Blue', 'Yellow']
After removing Orange: ['Red', 'Green', 'Blue', 'Yellow']
Removed: Yellow
Remaining: ['Red', 'Green', 'Blue']
```

---

### Program 8.3: Loop Through List
```python
# Loop through list with index
fruits = ["Apple", "Banana", "Cherry", "Date"]

print("Using for-in loop:")
for fruit in fruits:
    print(f"  - {fruit}")

print("\nUsing enumerate (with index):")
for index, fruit in enumerate(fruits):
    print(f"  {index + 1}. {fruit}")
```

**Output:**
```
Using for-in loop:
  - Apple
  - Banana
  - Cherry
  - Date

Using enumerate (with index):
  1. Apple
  2. Banana
  3. Cherry
  4. Date
```

---

### Program 8.4: List Slicing
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get subset of list
print(f"First 3 elements: {numbers[0:3]}")   # [1, 2, 3]
print(f"Elements 3-7: {numbers[3:7]}")       # [4, 5, 6, 7]
print(f"Last 3 elements: {numbers[-3:]}")    # [8, 9, 10]
print(f"Every 2nd element: {numbers[::2]}")  # [1, 3, 5, 7, 9]
```

**Output:**
```
First 3 elements: [1, 2, 3]
Elements 3-7: [4, 5, 6, 7]
Last 3 elements: [8, 9, 10]
Every 2nd element: [1, 3, 5, 7, 9]
```

---

### Program 8.5: List Sorting and Searching
```python
numbers = [45, 23, 67, 12, 89, 34]

# Sort list
sorted_numbers = sorted(numbers)
print(f"Original: {numbers}")
print(f"Sorted: {sorted_numbers}")
print(f"Sorted descending: {sorted(numbers, reverse=True)}")

# Find element
if 67 in numbers:
    index = numbers.index(67)
    print(f"67 found at index: {index}")

# Count occurrences
mixed = [1, 2, 2, 3, 3, 3, 4]
print(f"Count of 3: {mixed.count(3)}")
```

**Output:**
```
Original: [45, 23, 67, 12, 89, 34]
Sorted: [12, 23, 34, 45, 67, 89]
Sorted descending: [89, 67, 45, 34, 23, 12]
67 found at index: 2
Count of 3: 3
```

---

## 9. Functions

### Program 9.1: Basic Function
```python
# Define a simple function
def greet():
    print("Hello! Welcome to Python")

# Call the function
greet()
```

**Output:**
```
Hello! Welcome to Python
```

---

### Program 9.2: Function with Parameters
```python
# Function with parameters
def greet(name):
    print(f"Hello, {name}!")

# Call function with arguments
greet("Alice")
greet("Bob")
greet("Charlie")
```

**Output:**
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

---

### Program 9.3: Function with Return Value
```python
# Function that returns a value
def add(a, b):
    """Add two numbers and return the result"""
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the result"""
    return a * b

# Use the returned values
result1 = add(5, 3)
result2 = multiply(4, 6)

print(f"5 + 3 = {result1}")
print(f"4 * 6 = {result2}")
```

**Output:**
```
5 + 3 = 8
4 * 6 = 24
```

---

### Program 9.4: Function with Multiple Parameters and Default Values
```python
# Function with default parameter
def introduce(name, age=25, city="Unknown"):
    """Introduce a person"""
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

# Call with different numbers of arguments
introduce("Alice")
print()
introduce("Bob", 30)
print()
introduce("Charlie", 28, "New York")
```

**Output:**
```
Name: Alice
Age: 25
City: Unknown

Name: Bob
Age: 30
City: Unknown

Name: Charlie
Age: 28
City: New York
```

---

### Program 9.5: Function to Calculate Factorial
```python
# Calculate factorial of a number
def factorial(n):
    """Calculate factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
print(f"Factorial of 5: {factorial(5)}")    # 120
print(f"Factorial of 0: {factorial(0)}")    # 1
```

**Output:**
```
Factorial of 5: 120
Factorial of 0: 1
```

**Explanation:**
- This is a recursive function (a function that calls itself)
- Factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120

---

### Program 9.6: Function with List Parameter
```python
# Function that works with lists
def find_max(numbers):
    """Find the maximum number in a list"""
    if not numbers:
        return None
    
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def calculate_average(numbers):
    """Calculate average of a list"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Use the functions
scores = [85, 92, 78, 95, 88]
print(f"Scores: {scores}")
print(f"Maximum score: {find_max(scores)}")
print(f"Average score: {calculate_average(scores):.2f}")
```

**Output:**
```
Scores: [85, 92, 78, 95, 88]
Maximum score: 95
Average score: 87.60
```

---

## 10. Dictionaries

### Program 10.1: Creating and Accessing Dictionaries
```python
# Create a dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A",
    "major": "Computer Science"
}

# Access values by key
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Grade: {student['grade']}")

# Get method (safer, returns None if key doesn't exist)
print(f"Major: {student.get('major')}")
print(f"GPA: {student.get('gpa', 'Not found')}")
```

**Output:**
```
Name: John Doe
Age: 20
Grade: A
Major: Computer Science
GPA: Not found
```

---

### Program 10.2: Modifying Dictionary
```python
# Create a dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print("Original dictionary:")
print(person)

# Add new key-value pair
person["email"] = "alice@email.com"

# Update existing value
person["age"] = 26

# Delete key-value pair
del person["city"]

print("\nModified dictionary:")
print(person)
```

**Output:**
```
Original dictionary:
{'name': 'Alice', 'age': 25, 'city': 'New York'}

Modified dictionary:
{'name': 'Alice', 'age': 26, 'email': 'alice@email.com'}
```

---

### Program 10.3: Loop Through Dictionary
```python
# Dictionary of employees
employees = {
    "E001": "John Doe",
    "E002": "Jane Smith",
    "E003": "Bob Johnson"
}

# Loop through keys
print("Employee IDs:")
for emp_id in employees:
    print(f"  {emp_id}: {employees[emp_id]}")

# Alternative: using .items()
print("\nUsing items():")
for emp_id, name in employees.items():
    print(f"  {emp_id}: {name}")

# Get only values
print("\nEmployee names:")
for name in employees.values():
    print(f"  - {name}")
```

**Output:**
```
Employee IDs:
  E001: John Doe
  E002: Jane Smith
  E003: Bob Johnson

Using items():
  E001: John Doe
  E002: Jane Smith
  E003: Bob Johnson

Employee names:
  - John Doe
  - Jane Smith
  - Bob Johnson
```

---

### Program 10.4: Nested Dictionaries
```python
# Dictionary containing dictionaries
company = {
    "name": "Tech Corp",
    "employees": {
        "E001": {"name": "John", "position": "Manager"},
        "E002": {"name": "Jane", "position": "Developer"},
        "E003": {"name": "Bob", "position": "Designer"}
    }
}

# Access nested data
print(f"Company: {company['name']}")
print(f"First employee: {company['employees']['E001']['name']}")
print(f"Position: {company['employees']['E001']['position']}")

# Loop through nested data
print("\nAll employees:")
for emp_id, info in company['employees'].items():
    print(f"  {emp_id}: {info['name']} - {info['position']}")
```

**Output:**
```
Company: Tech Corp
First employee: John
Position: Manager

All employees:
  E001: John - Manager
  E002: Jane - Developer
  E003: Bob - Designer
```

---

### Program 10.5: Dictionary Methods
```python
student_grades = {
    "John": 85,
    "Alice": 92,
    "Bob": 78,
    "Diana": 95
}

# Check if key exists
if "John" in student_grades:
    print(f"John's grade: {student_grades['John']}")

# Get all keys
print(f"All students: {list(student_grades.keys())}")

# Get all values
print(f"All grades: {list(student_grades.values())}")

# Get all items
print("\nGrades:")
for student, grade in student_grades.items():
    print(f"  {student}: {grade}")

# Get dictionary length
print(f"\nTotal students: {len(student_grades)}")
```

**Output:**
```
John's grade: 85
All students: ['John', 'Alice', 'Bob', 'Diana']
All grades: [85, 92, 78, 95]

Grades:
  John: 85
  Alice: 92
  Bob: 78
  Diana: 95

Total students: 4
```

---

## Key Concepts Summary

### Data Types
- **int**: Whole numbers
- **float**: Decimal numbers
- **str**: Text
- **bool**: True/False
- **list**: Ordered collection `[1, 2, 3]`
- **dict**: Key-value pairs `{"name": "John"}`

### Control Flow
- **if/elif/else**: Make decisions
- **for**: Loop with known iterations
- **while**: Loop while condition is true
- **break**: Exit loop early
- **continue**: Skip to next iteration

### Functions
- Reusable blocks of code
- Can take parameters
- Can return values
- Help organize code

### Common Methods
- **String**: `.upper()`, `.lower()`, `.replace()`, `.strip()`
- **List**: `.append()`, `.remove()`, `.pop()`, `.sort()`
- **Dict**: `.keys()`, `.values()`, `.items()`, `.get()`

---

## Tips for Learning

1. **Type along**: Don't just read, type the code yourself
2. **Experiment**: Modify the programs and see what happens
3. **Combine concepts**: Mix loops, functions, and lists
4. **Read error messages**: They tell you what went wrong
5. **Practice regularly**: Code every day, even for 15 minutes

---

## Next Steps

Once you master these basics, explore:
- File handling (`open()`, `read()`, `write()`)
- Exception handling (`try`, `except`)
- Object-oriented programming (classes, objects)
- Libraries (NumPy, Pandas, Requests)
- Web development (Flask, Django)
