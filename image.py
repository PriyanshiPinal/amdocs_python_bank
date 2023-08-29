# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:49:30 2023

@author: Pinal
"""

from tkinter import *
from PIL import ImageTk, Image


#make a window
ws = Tk()
ws.title("Login page")

#get width & height of screen


#set screensize as fullscreen and not resizable
ws.geometry("1000x1000")
ws.resizable(False, False)

# put image in a label and place label as background
imgTemp = Image.open("C:/amdocs/picture.jpg")
img2 = imgTemp.resize((height,1800))
img = ImageTk.PhotoImage(img2)

label = Label(ws,image=img)
label.pack(side='top',fill=Y,expand=True)
text = Text(ws,height=10,width=53)
text.place(x=30, y=50)

button = Button(ws,text='SEND',relief=RAISED,font=('Arial Bold', 18))
button.place(x=190, y=250)

ws.mainloop()