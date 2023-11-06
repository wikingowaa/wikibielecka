# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:30:43 2023

@author: wikto
"""

def sprawdz_czy_parzysta(liczba):
    return liczba % 2 == 0

liczba = int(input("Podaj liczbę: "))

wynik = sprawdz_czy_parzysta(liczba)

if wynik:
    print("Liczba parzysta.")
else:
    print("Liczba nieparzysta.")