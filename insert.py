# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:35:36 2023

@author: Pinal
"""

import mysql.connector

try:

    mydbconn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password ="pinal@123",
    database ="SCMHRD")


    mycursor = mydbconn.cursor()
    

    sql=('insert into Scmhrd.product_master(pid,pname,price_per_unit) values(%s,%s,%d)')
    val=('p20','olive oil',900)
    mycursor.execute(sql,val)
 
    mydbconn.commit()

except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
