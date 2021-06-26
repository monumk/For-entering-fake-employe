from random import *

alpha='abcdefghijklmnopqrstuvwxyz'
City=['Hyderabad','Chennai','Bangalore','Pune','Delhi','Mumbai']
digit='0123456789'
designation=['Software Engineer','Senior Software Engineer','Team Leader','Project Lead','Project Manager']

def emp_name():
    name=choice(alpha).upper()
    n=randint(2,9)
    for i in range (n):
        name=name+choice(alpha)
    return name

def emp_number():
    eno='e-'
    for i in range(4):
        eno=eno+str(choice(digit))
    return eno

def emp_sal():
    sal=uniform(10000,50000)
    return sal

def emp_city():
    city=choice(City)
    return city

def mobile():
    num=str(randint(6,9))
    for i in range(9):
        num=num+choice(digit)
    return num

def desi():
    desig=choice(designation)
    return desig

def display():
    print('Employee Name :',emp_name())
    print('Employee Number :',emp_number())
    print('Employee Salary :',emp_sal())
    print('Employee City :',emp_city())
    print('Employee Mobile No :',mobile())
    print('Employee Designation :',desi())
    
for i in range(10):    
    display()
    print('* '*30)

print('Program written by M.K. Mahor (Monu)')