# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:44:23 2023

@author: wikto
"""

def operacje_na_listach(lista1, lista2):

    lista_polaczona = lista1 + lista2


    lista_unikalna = list(set(lista_polaczona))


    lista_potegowana = [x ** 3 for x in lista_unikalna]

    return lista_potegowana

lista1_str = input("Podaj pierwszą listę liczb, oddzielając je spacją: ")
lista2_str = input("Podaj drugą listę liczb, oddzielając je spacją: ")

lista1 = [int(x) for x in lista1_str.split()]
lista2 = [int(x) for x in lista2_str.split()]

wynik = operacje_na_listach(lista1, lista2)

print("Wynikowa lista:", wynik)