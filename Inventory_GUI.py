# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 06:03:27 2023

@author: Pinal
"""

from tkinter import *
import tkinter.messagebox
window=Tk()#class which creates a window
window.geometry("550x600")
window.title("Login")#.title is set to the title of your window
melabel=Label (window,text="Login For Inventory System",
               bg="White",font=("Times",30,"bold"))
melabel.place(x=200,y=0)
window.configure(background="blue")#set the back ground


textin=StringVar()
textin2=StringVar()

metext11=Entry(window,font=("Courier New",12,'bold'),
               textvar=textin,width=25,bd=5,bg='powder blue')
metext11.place(x=250,y=80)

thelabel=Label(window,text="UserName:",font="arial 20 bold")
thelabel.place(x=80,y=80)

metext13=Entry(window,font=("Courier New",12,'bold'),
               textvar=textin2,width=25,bd=5,bg='powder blue')
metext13.place(x=250,y=180)

thelabel1=Label(window,text="Email_id:",font="arial 20 bold")
thelabel1.place(x=80,y=180)




def log():
    tkinter.messagebox.askokcancel("askokcancel",
                           "do you want to continue")
def new():
    tkinter.messagebox.showinfo("showinformation", 
                                "Hello I am here to register")
    
    

butequal = Button(window, padx=42, pady=14, bd=4, bg='white', 
                  command=exec(open("C:\\amdocs\\python\\tkinter_grid.py").read()),text="Login",
                  font=("Courier New", 16, 'bold'))
butequal.place(x=225, y=540)

butequal = Button(window, padx=42, pady=14, bd=4, bg='white',
                  command=new,text="New Register",
                  font=("Courier New", 16, 'bold'))
butequal.place(x=525, y=540)
window.mainloop()

