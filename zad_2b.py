# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 12:15:42 2023

@author: wikto
"""

import random
lista = [random.random() for x in range(5)]
print(lista)
# z listą składana
new_lista = [number * 2 for number in lista]
print(new_lista)

# z pętlą for
new_lista = []
for number in lista:
    new_lista.append(number * 2)
print(new_lista)
