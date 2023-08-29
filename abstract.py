# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 15:38:52 2023

@author: Pinal
"""

from abc import ABC, abstractmethod
 
 
class shape(ABC):
 
    @abstractmethod
    def find_area(self,n1,n2):
        pass
 
 
class Rectangle(shape):
 
    # overriding abstract method
    def find_area(self,l,b):
        area = l * b
        print(area)
 
 
class  Circle(shape):
 
    # overriding abstract method
    def find_area(self,p,rad):
        area=p * pow(rad,2)
        print(area)
 
 
robj=Rectangle()
print("Rectangle Area......")

rl=float(input("Enter the length :"))
bl=float(input("Enter the breadth :"))

robj.find_area(rl,bl)

cobj=Circle()

print("Circle Area......")


radius=float(input("Enter the radius :"))

robj.find_area(3.14,bl)







