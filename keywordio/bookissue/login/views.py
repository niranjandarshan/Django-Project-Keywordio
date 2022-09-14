from ast import Global
from django.shortcuts import render
import mysql.connector as sql




mail=''
pword=''
# Create your views here.
def loginaction(request):
    global mail,pword
    
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="niru",database="bookissue")
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
           
            if key=="email":
                mail=value
            if key=="password":
                pword=value
                
        c="select * from admin where email='{}' and password='{}'".format(mail,pword)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if(t==()):
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
        
        
    return render(request,'login_page.html')

#Login Page for students   

