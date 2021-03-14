#!/usr/bin/env python
# coding: utf-8

"""
Created on 2021-03-14
@author: JMC
Basic operation - mean, median and quantile.
"""

import numpy as np


def _sum(arr):
    result = 0
    for i in arr:
        result = result + i

    return result


def _median(sample):
    n = len(sample)

    # Floor division
    index = n // 2

    # With an odd number
    if n % 2:
        return sorted(sample)[index]

    # With an even number
    return sum(sorted(sample)[index - 1:index + 1]) / 2


x = np.random.randint(100, size=5)
print('Example: ', x)
# np.sort(x)

media = np.mean(x)
media_manual = _sum(x) / len(x)

print('\nMedian:', media)
print('Median manual:', media_manual)

mediana = np.median(x)
mediana_manual = _median(x)

print('\nMediana:', mediana)
print('Mediana manual:', mediana_manual)

print("\nQ1 quantile: ", np.quantile(x, .25))
print("Q2 quantile: ", np.quantile(x, .50))
print("Q3 quantile: ", np.quantile(x, .75))
print("100th quantile: ", np.quantile(x, .1))
