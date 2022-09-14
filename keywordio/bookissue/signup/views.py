from ast import Global
from django.shortcuts import render
import mysql.connector as sql

fname=''
lname=''
gndr=''
mail=''
pword=''
# Create your views here.
def signupaction(request):
    global fname,lname,gndr,mail,pword
    
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="niru",database="bookissue")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fname=value
            if key=="last_name":
                lname=value
            if key=="sex":
                gndr=value
            if key=="email":
                mail=value
            if key=="password":
                pword=value
                
        c="insert into admin Values('{}','{}','{}','{}','{}')".format(fname,lname,gndr,mail,pword)
        cursor.execute(c)
        m.commit()
        
    return render(request,'signup_page.html')

#For Student Signup

fname=''
lname=''
gndr=''
regnum=''

# Create your views here.
def signup_student(request):
    global fname,lname,gndr,regnum
    
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="niru",database="bookissue")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fname=value
            if key=="last_name":
                lname=value
            if key=="sex":
                gndr=value
            if key=="registration_number":
                regnum=value
            
                
        c="insert into student Values('{}','{}','{}','{}')".format(fname,lname,gndr,regnum)
        cursor.execute(c)
        m.commit()
        
    return render(request,'signup_student.html')

            

