# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:12:50 2016

@author: vhrbh
"""

class Rectangle:
    
    def __init__(self,x, y, llength, wlength):
        self.llength = llength
        self.wlength = wlength
        self.centerX = x
        self.centerY = y
        
    def area(self):
        self.calc_area = self.llength *self.wlength
        return self.calc_area
        
    def perimeter(self):
        self.calc_peri = (self.llength * 2) + (self.wlength * 2)
        return self.calc_peri
        
    def display(self):
        self.rec_area = self.area()
        self.dispString = "The center of the rectangle is (" + str(self.centerX) + ", " + str(self.centerY) + ") the area is " + str(self.rec_area) + "."
        print(self.dispString)
        