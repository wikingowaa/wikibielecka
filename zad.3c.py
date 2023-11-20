# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:58:48 2023

@author: wikto
"""

class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area 
        self.rooms = rooms 
        self.rpice = price 
        self.address = address
        
    def __str__(self):
        return f"Property: {self.area} m2, {self.rooms} rooms\n" 
               f"Price: {self.price} zl\n" 
               f"Address: {self.address}"
               
               
class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super(). __init__(area, rooms, price, address)
        self.plot = plot 
        
    def __str__(self):
        return f"House - {super().__str__()}\n" 
            f"Plot: {self.plot} m2"
            
class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super(). __init__(area, rooms, price, address) 
        self.floor = floor 
        
    def __str__(self):
        return f"Flat - {super(). __str__()}|n" 
            f"Floor: {self.floor}"