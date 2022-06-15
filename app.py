
from tkinter import *
import requests
from socket import *
app=Tk()

socket=socket()
ports=[21,22,53,80,8080,3306,445]
#Fonctuon For Request in return  Result
def scan(*args):
    for port  in ports:
        result=socket.connect_ex(("162.222.226.133",port))
        if(result == 0):
            return port
    return Label(app,text=host)
   
def p(b):
    return Label(app,text=b).pack()
#CREATE label For App Name Logo
Label(app,text="Port Scanner",fg="white",background="#ff3948",width=100,height=2).pack()
#Create New lable For input Host Or Ip adress  From Users
#Create Button
Label(app,text="Please Enter Host Or Ip Adress",height=2).pack()


#Date Entry
entry=Entry(app,text="Start"
,fg="green",bg="white",width=25)
entry.pack()


lib=Label(app,width=100).pack()

i=entry.get()
btn=Button(app,
text="Start Scanning",width=12,bg="#ff7547",fg="white",command=p(i)).pack()
reslib=Label(app,text="Result Of Sacn",fg="green",width=69,height=2).pack()

Label(app,text="Port Scanner GUI\n Deveopment By Nebil Sharifi").pack()
if __name__  =="__main__":
    app.mainloop()
