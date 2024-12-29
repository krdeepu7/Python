# Python Type Conversion, Exceptions, and Functions

## Type Conversion in Python

### Implicit Conversion
#Python automatically converts one data type to another without user intervention.

integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# Display new value and resulting data type
print("Value:", new_number)
print("Data Type:", type(new_number))

### Explicit Conversion
#Users manually convert one data type to another.

num1 = '1'
num2 = 2

# This will throw an error because 'num1' is a string
print(num1 + num2)

num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:", type(num_string))

# Explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:", type(num_string))

num_sum = num_integer + num_string

print("Sum:", num_sum)
print("Data type of num_sum:", type(num_sum))

## Exceptions

### Common Exceptions
# ZeroDivisionError: division by zero
# 10 * (1/0)

# NameError: name 'spam' is not defined
# 4 + spam*3

# TypeError: can only concatenate str (not "int") to str
# '2' + 2


### Handling Exceptions
#Use `try` and `except` blocks to handle errors gracefully.

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")


### Raising Exceptions

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # Exception type
    print(inst.args)     # Arguments stored in .args
    print(inst)          # __str__ representation
    x, y = inst.args     # Unpack args
    print('x =', x)
    print('y =', y)



try:
    raise Exception('FileError', 'The file could not be opened')
except Exception as inst:
    print(type(inst))    # Exception type
    print(inst.args)     # Arguments stored in .args
    print(inst)          # __str__ representation
    error_type, message = inst.args  # Unpack args
    print('Error Type =', error_type)
    print('Message =', message)


### Chained Exceptions

def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc


## Functions

### Basic Function Definition

def my_function():
    print("Hello from a function")

my_function()


### Function with Parameters

def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


### Arbitrary Arguments

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


### Keyword Arguments

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")


### Default Parameter Value

def my_function(country="Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


### Iterating Over Arguments

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


### Return Values

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


### Positional and Keyword-Only Arguments

def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c=7, d=8)


### Recursion

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)


## Data Structures

### Tuples
#Immutable sequences.

t = (1, 2, 3, 4)
print(t[1])  # Access by index: Output is 2
# t[1] = 5   # Error: 'tuple' object does not support item assignment


### Lists
#Mutable sequences.

l = [1, 2, 3, 4]
l.append(5)       # Adds 5 to the list
print(l)          # Output: [1, 2, 3, 4, 5]
l[1] = 10         # Modify an element
print(l)          # Output: [1, 10, 3, 4, 5]


### Sets
#Unordered collections with no duplicate elements.

s = {1, 2, 3, 4, 4}  # Duplicates are ignored
print(s)             # Output: {1, 2, 3, 4}
s.add(5)             # Adds 5 to the set
print(s)             # Output: {1, 2, 3, 4, 5}
s.remove(3)          # Removes 3 from the set
print(s)             # Output: {1, 2, 4, 5}
