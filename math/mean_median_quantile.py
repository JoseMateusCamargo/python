# Basic operation - mean, median and quantile.

import numpy as np


def _sum(arr):
    result = 0

    for i in arr:
        result = result + i

    return result


def _median(sample):
    n = len(sample)
    index = n // 2  # Floor division

    if n % 2:  # With an odd number
        return sorted(sample)[index]

    return sum(sorted(sample)[index - 1:index + 1]) / 2  # With an even number


x = np.random.randint(100, size=5)
print(f'Using example: {x}\n')
# np.sort(x)

print(f'---------- Mean examples:\n'
      f'Mean using Numpy: {np.mean(x)}\n'
      f'Mean manual function _sun: {_sum(x) / len(x)}\n')

print(f'---------- Median examples:\n'
      f'Median using Numpy: {np.median(x)}\n'
      f'Median manual function _median: {_median(x)}\n')

print(f'---------- Quantile examples:\n'
      f'Q1 quantile: {np.quantile(x, .25)}\n'
      f'Q2 quantile: {np.quantile(x, .50)}\n'
      f'Q3 quantile: {np.quantile(x, .75)}\n'
      f'100th quantile: {np.quantile(x, .1)}')
