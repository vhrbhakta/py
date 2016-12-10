# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:26:31 2016

@author: vhrbh
"""

class Triangle:
    
    def __init__(self, x, y, height, base):
        self.height = height
        self.base = base
       
        self.centerX = x
        self.centerY = y
        
    def area(self):
        self.tri_area = self.height * self.base * .5
        return self.tri_area
        
    def display(self):
        self.tri_area = self.area()
        self.dispString = "The center of the rectangle is (" + str(self.centerX) + ", " + str(self.centerY) + ") the area is " + str(self.tri_area) + "."
        print(self.dispString)
        