# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:30:07 2016

@author: vhrbh
"""
import math

class Circle:
    
    def __init__(self, x, y, radius):
        self.radius = radius
        self.centerX = x
        self.centerY = y
        
    def area(self):
        self.calc_area = math.pow(self.radius,2) * math.pi
        return self.calc_area
        
    def perimeter(self):
        self.circumference = 2 * self.radius * math.pi
        return self.circumference
        
    def display(self):
        self.cir_area = self.area()
        self.dispString = "The center of the rectangle is (" + str(self.centerX) + ", " + str(self.centerY) + ") the area is " + str(self.cir_area) + "."
        print(self.dispString)
        