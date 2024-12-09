## Operator precedence
# **
# %, /, //, *
# -, +

x= 0b010
print(x)
x = 0
y =5
if x < y:                            # Truthy
    print('yes')
if y < x:                            # Falsy
    print('yes')
if x:                                # Falsy
    print('yes')
if y:                                # Truthy
    print('yes')
if x or y:                           # Truthy
    print('yes')
if x and y:                          # Falsy
    print('yes')
if 'aul' in 'grault':                # Truthy
    print('yes')
if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')


if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x


if 'f' in 'foo': print('1'); print('2'); print('3')

# 1
# 2
# 3
if 'z' in 'foo': print('1'); print('2'); print('3')


raining = False
print("Let's go to the", 'beach' if not raining else 'library')
#Let's go to the beach
raining = True
print("Let's go to the", 'beach' if not raining else 'library')
#Let's go to the libr
age = 12
s = 'minor' if age < 21 else 'adult'
s

'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'




x = y = 40
z = 1 + x if x > y else y + 2
print(z) 
#42

z = (1 + x) if x > y else (y + 2)
print(z)
#42


#Loop
#Example with List, Tuple, String, and Dictionary Iteration Using for Loops in Python

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
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
    
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),



list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])


list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])

list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")


n = 5
while n > 0:
    n -= 1
    print(n)

n = 0
while n > 0:
    n -= 1
    print(n)
a = ['foo', 'bar', 'baz']
while a:
    print(a.pop(-1))

#The Python break and continue Statements

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('Loop ended.')


n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')


n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')
4
3
2
1
0
#Loop done.

a = ['foo', 'bar', 'baz', 'qux']
s = 'corge'

i = 0
while i < len(a):
     if a[i] == s:
         # Processing for item found
         break
     i += 1
else:
     # Processing for item not found
     print(s, 'not found in list.')

#corge not found in list.


a = ['foo', 'bar', 'baz']
while True:
     if not a:
         break
     print(a.pop(-1))

# baz
# bar
# foo


a = ['foo', 'bar']
while len(a):
    print(a.pop(0))
    b = ['baz', 'qux']
    while len(b):
        print('>', b.pop(0))



n = 5
while n > 0: n -= 1; print(n)

# 4
# 3
# 2
# 1
# 0

if True: print('foo')

#foo

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)


d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

i, j = (1, 2)
print(i, j)

for i, j in [(1, 2), (3, 4), (5, 6)]:
    print(i, j)

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k, v in d.items():
   print('k =', k, ', v =', v)

for n in (0, 1, 2, 3, 4):
     print(n)

for n in x:
     print(n)


list(range(-5, 5))
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

list(range(5, -5))
[]
list(range(5, -5, -1))
[5, 4, 3, 2, 1, 0, -1, -2, -3, -4]

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')  # Will not execute
