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