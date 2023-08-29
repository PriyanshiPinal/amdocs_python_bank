# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:43:15 2023

@author: Pinal
"""
class department:
    def __init__(self,deptid,deptname):
        self.deptid=deptid
        self.deptname=deptname
        
class emp(department):
    __count=0 #hidden member
    def __init__(self,deptid,deptname,id,name,salary):# constructor
        self.id=id
        self.name=name
        self.salary=salary
        department.__init__(self, deptid, deptname)
        
class emp_project(emp):
    def __init__(self, deptid, deptname, id, name, salary,dur,projname):
        self.dur=dur
        self.projname=projname
        super().__init__(self, deptid, deptname, id, name, salary)
   
    def print_empdetails(self):
        print("Empid :",self.id)
        print("Empname :",self.name)
        print("Employee's department no : ",self.deptid)
        print("Employee's department :",self.deptname)
        print("Salary :",self.salary)
        print("Project name :",self.projname)
        print("Project Duration :",self.dur)
e=[]

n=int(input("How many employee details"))

for i in range(0,n):
    mid=input("Enter id :")
    mname=input("Enter employee name :")
    mdid=input("Enter dept id :")
    mdname=input("Enter dept name :")
    msal=input("Enter the salary :")
    mpname=input("Enter project name :")
    mdur=input("Enter the duration of project :")
    ei=emp_project(mdid,mdname,mid,mname,msal,mdur, mpname)
    
    e.append(ei)
    
for employee in e:
    employee.print_empdetails()
    
    
    
    