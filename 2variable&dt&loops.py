## Operator Precedence Demonstration
# Order of precedence: 
# ** (exponentiation) > %, /, //, * > - and +

# Binary number assignment
x = 0b011  # Binary for 2
print(x)  # Output: 2

# Conditional statements with truthy and falsy values
x = 0
y = 5

# Checking conditions and their outcomes
if x < y:  # Truthy, 0 < 5
    print('yes')  # Output: yes
if y < x:  # Falsy, 5 is not < 0
    print('yes')
if x:  # Falsy, 0 is equivalent to False
    print('yes')
if y:  # Truthy, any non-zero number is True
    print('yes')  # Output: yes
if x or y:  # Truthy, y is non-zero
    print('yes')  # Output: yes
if x and y:  # Falsy, x is zero (False)
    print('yes')
if 'aul' in 'grault':  # Truthy, 'aul' is a substring of 'grault'
    print('yes')  # Output: yes
if 'quux' in ['foo', 'bar', 'baz']:  # Falsy, 'quux' is not in the list
    print('yes')

# Nested conditional statements
if 'foo' in ['foo', 'bar', 'baz']:  # Truthy
    print('Outer condition is true')  # Output: Outer condition is true

    if 10 > 20:  # Falsy
        print('Inner condition 1')  # Does not execute

    print('Between inner conditions')  # Output: Between inner conditions

    if 10 < 20:  # Truthy
        print('Inner condition 2')  # Output: Inner condition 2

    print('End of outer condition')  # Output: End of outer condition

print('After outer condition')  # Output: After outer condition

# Inline conditional statements
if 'f' in 'foo': print('1'); print('2'); print('3')  # Outputs 1, 2, 3
if 'z' in 'foo': print('1'); print('2'); print('3')  # No output

# Ternary operator usage
raining = False
print("Let's go to the", 'beach' if not raining else 'library')  # Output: Let's go to the beach
raining = True
print("Let's go to the", 'beach' if not raining else 'library')  # Output: Let's go to the library

# Another ternary example
age = 22
s = 'minor' if age < 21 else 'adult'
print(s)  # Output: minor

# Expression evaluation in ternary form
print('yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no')  # Output: no

# Complex ternary example
x = y = 40
z = 1 + x if x < y else y + 2
print(z)  # Output: 42

z = (1 + x) if x > y else (y + 2)
print(z)  # Output: 42

## Loop Demonstrations

# Iterating over various data structures
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

print("\nDictionary Iteration")
d = {'x': 123, 'y': 354}
for i in d:
    print("%s  %d" % (i, d[i]))

print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i)

# Loop with `else` block
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")  # Output after loop ends

# While loops
n = 5
while n > 0:
    n -= 1
    print(n)  # Counts down from 4 to 0

n = 0
while n > 0:
    n -= 1
    print(n)  # No output, condition is false

# Break and continue statements
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break  # Exit loop when n == 2
    print(n)
print('Loop ended.')  # Output: 4, 3; Loop ended.

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue  # Skip iteration when n == 2
    print(n)
print('Loop ended.')  # Outputs 4, 3, 1, 0; Loop ended.

# Nested loops
a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))

# For loop with conditions
for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')  # Will not execute because of break
