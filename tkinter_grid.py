# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:51:36 2023

@author: Pinal
"""

from tkinter import *
from tkinter import ttk
import mysql.connector


window=Tk()#class which creates a window
window.geometry("550x600")
window.title("Fetch")#.title 


conn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password ="pinal@123",
    database ="SCMHRD")
cursor = conn.cursor()
cursor.execute("SELECT * FROM product_master limit 0,10")
i=0 
for pro in cursor: 
    for j in range(len(pro)):
        e = Entry(window, width=50, fg='blue',background='beige') 
        e.grid(row=i, column=j) 
        e.insert(END, pro[j])
    i=i+1
window.mainloop()



