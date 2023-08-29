# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 11:33:25 2023

@author: Pinal
"""

import mysql.connector

try:

    mydbconn = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password ="pinal@123",
    database ="SCMHRD")

# for fetching all
    mypointer = mydbconn.cursor()

    mypointer.execute("SELECT * FROM customer_master")

    myrecords = mypointer.fetchall()

    for i in myrecords:
        print(i)
        
# for inserting records in the table

    insert_query="""INSERT INTO CUSTOMER_MASTER VALUES
                    ('C100','MAHI','SURAT','F',35)"""
    mypointer3=mydbconn.cursor()
    mypointer3.execute(insert_query)
    mydbconn.commit()
    print(mypointer3.rowcount, "Record inserted successfully")
    mypointer3.close()
    
    
except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))
