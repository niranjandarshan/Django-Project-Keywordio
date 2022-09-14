from http.client import HTTPResponse
from django.shortcuts import render,redirect
import mysql.connector as sql


bid=''
bname=''
bauthor=''
bquantity=''
# Create your views here.
m=sql.connect(host="localhost",user="root",password="niru",database="bookissue")
cur=m.cursor()

def logout(request):
    return redirect('login.html')
def show(request):
    cur.execute("select * from bookinfo")
    data=cur.fetchall()
    return render(request,'welcome.html',{'category':data})

def show_student(request):
    cur.execute("select * from bookinfo")
    data=cur.fetchall()
    return render(request,'welcome_student.html',{'category':data})
regnum=''
# Create your views here.
def login_student(request):
    global regnum
    
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="niru",database="bookissue")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
           
            if key=="registration_number":
                regnum=value
            
                
        c="select * from student where registration_number='{}' ".format(regnum)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if(t==()):
            return render(request,'error.html')
        else:
            return redirect(show_student)
        
        
    return render(request,'login_student.html')

            



def retrieve(request):
    global bid
    
    if request.method=="POST":
        
        d=request.POST
        for key,value in d.items():
            if key=="bookid" :
                bid=value
    cur.execute("select * from bookinfo where bookid='{}'".format(bid))
    datar=cur.fetchall()
    return render(request,'retrieve.html',{'catretrieve':datar})



# Create your views here.
def create(request):
    global bid,bname,bauthor,bquantity
    
    if request.method=="POST":
        
        d=request.POST
        for key,value in d.items():
            if key=="bookid" :
                bid=value
            if key=="bookname":
                bname=value
            if key=="author":
                bauthor=value
            if key=="quantity":
                bquantity=value
            
                
        c="insert into bookinfo Values('{}','{}','{}','{}')".format(bid,bname,bauthor,bquantity)
        cur.execute(c)
        m.commit()
        
    return render(request,'create.html')



# Update your views here.
def update(request):
    global bid,bname,bauthor,bquantity
    
    if request.method=="POST":
        
        d=request.POST
        for key,value in d.items():
            if key=="bookid" :
                bid=value
            if key=="quantity":
                bquantity=value
              
        c="update bookinfo set quantity=('{0}') where bookid=('{1}')".format(bquantity,bid)
        cur.execute(c)
        m.commit()
        
    return render(request,'update.html')


    
# Delete your views here.

def delete(request):
    global bid
    
    if request.method=="POST":
        
        d=request.POST
        for key,value in d.items():
            if key=="bookid" :
                bid=value
            
              
        c="delete from bookinfo  where bookid='{}'".format(bid)
        cur.execute(c)
        m.commit()
        
    return render(request,'delete.html')



