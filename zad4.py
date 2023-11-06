# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:34:37 2023

@author: wikto
"""

def sprawdz_suma_wieksza_badz_rowna(a, b, c):
    suma = a + b
    return suma >= c

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

wynik = sprawdz_suma_wieksza_badz_rowna(a, b, c)

if wynik:
    print("Suma dwóch pierwszych liczb jest większa lub równa trzeciej.")
else:
    print("Suma dwóch pierwszych liczb nie jest większa lub równa trzeciej.")