#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2021-05-18
@author: JMC
Simple way to read row in .csv
"""

import csv

file = "base_name.csv"
with open(file) as file:
    content = csv.reader(file)
    for row in content:
        print(row)
