# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:55:30 2023

@author: Pinal
"""

from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from PIL import ImageTk, Image

window=Tk()#class which creates a window
window.title('Information')
img=Image.open('C:\Amdocs\picture.jpg')
bg=ImageTk.PhotoImage(img)

window.geometry("550x600")
window.title("Login")

#.title is set to the title of your window
melabel=Label (window,text="Login For Inventory System",
               font=("Times",30,"bold"))
melabel.place(x=200,y=0)


CheckVar1 = IntVar()
CheckVar2 = StringVar()
C1 = Checkbutton(window, text = "vegetable", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(window, text = "fruits", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5,\
                 width = 20)
C1.place(x=80,y=80)

C2.place(x=260,y=80)

n=StringVar()

chkbx= ttk.Combobox(window, width=30,textvariable =n)

chkbx['values']=('Jaipur','Pune','Hyderabad','Ooty')

chkbx.place(x=600,y=200)

def chkbx_selection():
    selected_option=chkbx.get()
    tkinter.messagebox.showinfo("showinformation",selected_option)
    
butequal = Button(window, padx=42, pady=14, bd=4, bg='white', 
                  command=chkbx_selection,text="OKAY",
                  font=("Courier New", 16, 'bold'))
butequal.place(x=200, y=540)

window.mainloop()
