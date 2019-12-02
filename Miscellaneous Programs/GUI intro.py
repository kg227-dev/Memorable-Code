#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 12:31:30 2019

@author: kushgulati
"""

from tkinter import *
 
window = Tk()
 
window.title("Welcome to Kush's first app")
 
window.geometry('350x350')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
btn = Button(window, text="Click Me")
 
btn.grid(column=5, row=5)
 
window.mainloop()