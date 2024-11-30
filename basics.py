## Starting the program

# Print a simple "Hello World" message
print("Hello world")

# Variable reassignment example
age = 20  # Initially setting age to 20
age = 30  # Changing age to 30
print(age)  # Prints 30

# Example of different data types
price = 19.95  # Float
first_name = "Jack"  # String
is_online = False  # Boolean
print(is_online)  # Prints False

# Example of grouping related information
# Patient details
patient_name = 'Ram'
patient_age = 20
is_patient_new = True  # Boolean to indicate if the patient is new

# Print patient details with line breaks
print(patient_name, '\n', patient_age, '\n', is_patient_new, '\n')

# User input (commented out)
# Uncomment the following lines to accept user input
# name = input("What is your name? ")
# print("Hello " + name)

# Typecasting example
# Uncomment the following lines to calculate age
# year = int(input("Enter your birth year\n"))
# print(f"Your age is {2024 - year}")

# Demonstrating basic typecasting
int()    # Converts to integer
float()  # Converts to float
bool()   # Converts to boolean
str()    # Converts to string

# Basic Calculation
num1 = 5.7
num2 = 7
print(num1 + num2)  # Adds two numbers

# Uncomment for user-input based calculation
# num3 = float(input("Enter number1\n"))
# num4 = float(input("Enter number2\n"))
# print(num3 + num4)

# String operations
course = 'Python for Beginners'
print(course.upper())  # Converts to uppercase
print(course)          # Original string
print(course.find('y'))  # Finds the index of 'y' (1-based index)
print(course.find('for'))  # Finds the starting index of 'for'
print(course.replace('for', '4'))  # Replaces 'for' with '4'
print(course.replace('z', '4'))    # Attempt to replace non-existent character
print('Python' in course)  # Checks if 'Python' is in the string

# Arithmetic operators
print(10 + 5)  # Addition
print(10 - 5)  # Subtraction
print(10 * 5)  # Multiplication
print(10 / 3)  # Division (float)
print(10 // 3)  # Division (integer)
print(10 % 3)  # Modulus (remainder)
print(10 ** 3)  # Exponentiation

# Compound assignment
x = 10
x = x + 3  # Adds 3 to x
x += 3     # Shortcut for x = x + 3

# Operator precedence
x = 10 + 3 * 2  # Multiplication takes precedence
print(x)
x = (10 + 3) * 2  # Parentheses override precedence
print(x)

# Comparison operators
x = 3 > 2  # True
x = 3 == 2  # False
x = 3 != 2  # True

# Logical operators
price = 25
print(price > 10 and price < 30)  # True if both conditions are true
print(price > 10 or price < 30)  # True if at least one condition is true
print(not price > 20)  # Negates the condition

# If statements
num = 10
if num > 10:
    print('Number is greater than 10')
    print("Block of code")
elif num == 10:
    print("Number is equal to 10")
else:
    print("Number is smaller than 10")
print("Done")

# Currency converter
Amount = float(input("Enter an amount\n"))  # Accept amount
key = input("Currency in Dollar(D) or INR(I)\n")  # Accept currency type
if key == 'I':
    print("Amount in Dollar will be " + str(Amount / 84))  # INR to USD
elif key == 'D':
    print("Amount in rupees will be " + str(Amount * 84))  # USD to INR
else:
    print("Invalid input")

# While loop example
i = 1
while i <= 10:
    print(i * '#')  # Print '#' i times
    i += 1

# Lists (complex data type)
names = ['Ram', 'Shyam', 'John', 'Peter']
print(names)        # Prints the entire list
print(names[1])     # Access by index
print(names[-2])    # Access from end
print(names[1:3])   # Slice list from index 1 to 2

# List methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Adds 6 to the end
numbers.insert(0, -1)  # Inserts -1 at index 0
numbers.remove(3)  # Removes first occurrence of 3
# numbers.clear()  # Clears the list
print(numbers)
print(1 in numbers)  # Checks if 1 is in the list
print(len(numbers))  # Prints the length of the list

# For loop example
number = [1, 2, 3, 4, 5, 6]
for item in number:
    print(item)

# Range function
numbers = range(5, 10)
print(numbers)
for numberr in numbers:
    print(numberr)
numbers = range(5, 10, 2)  # Increment by 2
print(numbers)
for numberr in numbers:
    print(numberr)

# Tuples (immutable lists)
numbers = (1, 2, 3, 3)
# numbers[2] = 5  # Uncommenting this will cause an error as tuples are immutable
print(numbers.count(3))  # Counts occurrences of 3

print ("Done")