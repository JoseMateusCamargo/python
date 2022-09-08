'''
Euclidean distance
In mathematics, the Euclidean distance between two points in Euclidean space is the length of a line segment
between the two points. It can be calculated from the Cartesian coordinates of the points using the
Pythagorean theorem, therefore occasionally being called the Pythagorean distance.
'''

from scipy.spatial import distance
import numpy as np
from math import sqrt
from math import dist

# Computes the Euclidean distance between two 1-D arrays.
# Method #1: Using distance.euclidean()
# scipy.spatial.distance.euclidean(u, v, w=None)
euclid_scipy = distance.euclidean([1, 7, 0], [5, 1, 0])
print(f'Method #1: Using distance.euclidean(): {euclid_scipy}')

# Method #2: Using linalg.norm() -----------------------------------#
a = np.array((1, 7, 0))
b = np.array((5, 1, 0))

dist_linalg = np.linalg.norm(a - b)
print(f'Method #2: Using linalg.norm(): {dist_linalg}')

# Method #3: Using square() and sum() ------------------------------#
dist_sun = np.sqrt(np.sum(np.square(a - b)))
print(f'Method #3: Using square() and sum(): {dist_sun}')

# Method #4: Using square() and dot() -------------------------------#
temp = a - b
dist_dot = np.sqrt(np.dot(temp.T, temp))
print(f'Method #4:Using square() and dot(): {dist_dot}')

# Method #5: Using dist() ------------------------------------------#
print(f'Method #5: Using dist(): {dist(a, b)}')

# Method #6: Using np.sqrt() ---------------------------------------#
point_a = (1, 7)
point_b = (5, 1)
dist_sqrt = sqrt((point_a[0] - point_b[0]) ** 2 + (point_a[1] - point_b[1]) ** 2)
print(f'Method #6: Using np.sqrt(): {dist_sqrt}')

# Example points in 3-dimensional space...
x = (1, 7, 7)
y = (5, 1, 9)
distance = sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
print("Method #6: Euclidean distance in 3-dimensional space from x to y: ", distance)

# Extra  ----------------------------------------------------------#
print('\n')
print("Enter the first point A: ")
x1, y1 = map(int, input().split())
print("Enter the second point B: ")
x2, y2 = map(int, input().split())
dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("The Euclidean Distance is " + str(dist))
