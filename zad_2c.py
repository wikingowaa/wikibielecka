# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:24:01 2023

@author: wikto
"""

import random
list = [random.randint(0, 100) for x in range(10)]
print(liczba)
parzyste = []
for el in list:
    if el % 2 == 0:
        parzyste.append(el)
print(parzyste)
