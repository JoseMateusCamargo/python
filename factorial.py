#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on ‎segunda-feira, ‎23‎ de ‎março‎ de ‎2020, ‏‎15:52:59
@author: JMC
Factorial function
"""


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(10))
