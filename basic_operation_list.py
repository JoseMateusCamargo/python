#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on ‎segunda-feira, ‎23‎ de ‎dezembro‎ de ‎2019, ‏‎00:09:09
@author: JMC
Basic operations with list.
"""

print("\nBasic operations with list.")

list_a = [1, 2, 3, 4, 5]
print("List example:", list_a)

x = 0
total_in_arr = len(list_a)

# Operation using -> while
print("\n Loop - using while")
while x < total_in_arr:
    print(" ->", list_a[x])
    x += 1

# Operation using -> for
print("\nLoop - using for")
list_b = [1, 2, 3, 4, 5]
for item in list_b:
    print(" ->", item)

""" 
Iterating lists 
the code below does not work - just an example

list_error = [100,200,300,400]
for item in list_error:
    item += 1000
print(list_error)
"""

# Iterating lists - using range
print("\nIterating lists - using range")
list_r = [100, 200, 300, 400, 500, 600, 700, 800]
for item in range(len(list_r)):
    list_r[item] += 1000
print(list_r)

# Iterating lists - using enumerate
print("\nIterating lists - using enumerate")
list_enumerate = [100, 200, 300, 400, 500, 600, 700, 800]
for idx, item in enumerate(list_enumerate):
    list_enumerate[idx] += 1000
print(list_enumerate)
