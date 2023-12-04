# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 11:07:01 2023

@author: wikto
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        average_marks = sum(self.marks) / len(self.marks)
        return average_marks > 50

    def __str___(self):
        return f'Czy {self.name} zdał/a? {self.is_passed()}"'


student1 = Student('Marek', [50, 50, 60, 50])
student2 = Student('Aga', [10, 10, 10])
print(student1)
print(student2)
