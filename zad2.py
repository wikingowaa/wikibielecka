# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:23:53 2023

@author: wikto
"""

def pomnoz_dwie_liczby(a, b):
    wynik = a * b
    return wynik

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

wynik_mnozenia = pomnoz_dwie_liczby(a, b)

print("Wynik mnożenia:", wynik_mnozenia)