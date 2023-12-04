# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:38:19 2023

@author: wikto
"""


def sprawdz_czy_lista_zawiera_wartosc(lista, wartosc):
    return wartosc in lista


lista_str = input("Podaj listę liczb, oddzielając je spacją: ")
lista = [int(x) for x in lista_str.split()]


wartosc = int(input("Podaj wartość, którą chcesz sprawdzić: "))

wynik = sprawdz_czy_lista_zawiera_wartosc(lista, wartosc)

if wynik:
    print("Lista zawiera podaną wartość.")
else:
    print("Lista nie zawiera podanej wartości.")
