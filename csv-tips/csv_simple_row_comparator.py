#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on segunda-feira, ‎13‎ de ‎janeiro‎ de ‎2020, ‏‎19:36:05
@author: JMC
Simple row comparator between two .csv files and saving difference
"""

with open('1.csv', 'r') as t1, open('2.csv', 'r') as t2:
    file_one = t1.readlines()
    file_two = t2.readlines()

with open('difference.csv', 'w') as outFile:
    for line in file_two:
        if line not in file_one:
            outFile.write(line)

print("Finish")
