import sys

# Returns the memory size of the object
dic = {'a': 677, 'b': 494848, 'c': 0, 'd': 'memory'}
print(sys.getsizeof(dic))
