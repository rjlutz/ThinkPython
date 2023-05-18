# >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
# >>> t[1:3] = ['x', 'y']
# >>> t
# ['a', 'x', 'y', 'd', 'e', 'f']

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print(t)

## what if the sizes are not matched?
# like
# t[1:3] = ['x', 'y', 'z']
# t[1:3] = ['x']
