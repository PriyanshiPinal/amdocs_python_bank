# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 09:47:55 2023

@author: Pinal
"""

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
window=Tk()#class which creates a window
window.title('Call another')


window.geometry("550x600")
window.title("Login")

def calling():
  window.destroy()
  import calendar


butequal = Button(window, padx=42, pady=14, bd=4, bg='white', 
                  command=calling,text="Call me",
                  font=("Courier New", 16, 'bold'))
butequal.place(x=20, y=50)


window.mainloop()