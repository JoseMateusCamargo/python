# Basic operations with list.

print('\nBasic operations with list.')
x = 0
list_a = [1, 2, 3, 4, 5]

print(f'List example: {list_a}')

# Operation using -> while
print("\nLoop - using while")
while x < len(list_a):
    print(f' -> {list_a[x]}')
    x += 1

# Operation using -> for
print("\nLoop - using for")
for item in list_a:
    print(" ->", item)

# Iterating lists - using range
print("\nIterating lists - using range")

for item in range(len(list_a)):
    list_a[item] += 1000

print(list_a)

# Iterating lists - using enumerate
print("\nIterating lists - using enumerate")

for idx, item in enumerate(list_a):
    list_a[idx] += 1000

print(list_a)

""" 
Iterating lists the code below does not work - just an example

list_error = [100,200,300,400]
for item in list_error:
    item += 1000

print(list_error)
"""
