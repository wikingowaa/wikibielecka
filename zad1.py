# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:33:16 2023

@author: wikto
"""

def przywitaj_się(imię, nazwisko):
    return f"Cześć {imię} {nazwisko}!"

# Pobieranie imienia i nazwiska od użytkownika
imię = input("Podaj swoje imię: ")
nazwisko = input("Podaj swoje nazwisko: ")

powitanie = przywitaj_się(imię, nazwisko)

print(powitanie)