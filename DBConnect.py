# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 06:32:53 2023

@author: Pinal
"""
# pip install mysql-connector-python
import mysql.connector

mydbconn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password ="pinal@123")

print (mydbconn)

mypointer = mydbconn.cursor()

mypointer.execute("CREATE DATABASE SmartOps")

mypointer.execute("SHOW DATABASES")

for i in mypointer:
    print(i)