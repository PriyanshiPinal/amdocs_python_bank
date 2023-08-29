# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:42:27 2023

@author: Pinal
"""

from tkinter import*
import tkinter.messagebox
import mysql.connector
window=Tk()#class which creates a window
window.geometry("550x600")
window.title("Register")#.title is set the title of your window
melabel=Label (window,text="Registeration For Inventory System",bg="White",font=("Times",30,"bold"))
melabel.place(x=200,y=0)
window.configure(background="white")#set the back ground





def database():
    mydbconn = mysql.connector.connect(
        host ="localhost",
        user = "root",
        password ="pinal@123")
    #cursor.execute('create table info456( name Text, email Text,city Text, contact integer, passward Text )')
    mydbconn.commit()

textin=StringVar()
textin2=StringVar()
textin3=StringVar()
textin4=StringVar()
textin1=int
metext=Entry(window,font=("Courier New",12,'bold'),
             textvar=textin,width=25,bd=5,bg='powder blue')
metext.place(x=250,y=80)
thelabel=Label(window,text="cid :",font="arial 20 bold")
thelabel.place(x=80,y=80)#.grid(row=2,column=0,sticky=W)
metext1=Entry(window,font=("Courier New",12,'bold'),
              textvar=textin2,width=25,bd=5,bg='powder blue')
metext1.place(x=250,y=160)#.grid(row=5,column=4,sticky=E)
metext2=Entry(window,font=("Courier New",12,'bold'),
              textvar=textin3,width=25,bd=5,bg='powder blue')
metext2.place(x=250,y=240)#.grid(row=9,column=4,sticky=E)
metext3=Entry(window,font=("Courier New",12,'bold'),
              textvar=textin1,width=25,bd=5,bg='powder blue')
metext3.place(x=250,y=320)#.grid(row=13,column=4,sticky=E)
metext4=Entry(window,font=("Courier New",12,'bold'),
              textvar=textin4,width=25,bd=5,bg='powder blue')
metext4.place(x=250,y=400)#.grid(row=16,column=4,sticky=E)
#thelabel=Label(window,text="Name :",font="arial 20 bold")
#thelabel.place(x=80,y=80)#.grid(row=2,column=0,sticky=W)
thelabe2l=Label(window,text="Email :",font="arial 20 bold")
thelabe2l.place(x=80,y=160)#.grid(row=5,column=0,sticky=W)
thelabe3=Label(window,text="City :",font="arial 20 bold")
thelabe3.place(x=80,y=240)#.grid(row=9,column=0,sticky=W)
thelabe4=Label(window,text="Contact :",font="arial 20 bold")
thelabe4.place(x=80,y=320)#.grid(row=13,column=0,sticky=W)
thelabe5=Label(window,text="Password :",font="arial 20 bold")
thelabe5.place(x=80,y=400)#.grid(row=16,column=0,sticky=W)


def insert1():
    in1 = metext.get()
    in2 = metext1.get()
    in3 = metext2.get()
    in4 = metext3.get()
    in5 = metext4.get()

    database()
    flag = False
    flag=cursor.execute('insert into customer_master \
                        (cid,cname,city,gender,age) \
                        values(?,?,?,?,?)',(in1, in2, in3, in4, in5))


    if flag == True:
        tkinter.messagebox.showinfo("Register","data is inserted")
    conn.commit()
    conn.close()


butequal = Button(window, padx=42, pady=14, bd=4, bg='white', command=insert1,text="Register",font=("Courier New", 16, 'bold'))
butequal.place(x=225, y=540)




window.mainloop()