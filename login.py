from cgitb import text
from logging import root
from tkinter import *

#from registration import BCNO, BCNOentry, BCNOvalue, SchoolCodeentry
root = Tk()
root.geometry("400x350")
def getval1():
    print("Data Accepted")
def getSignup():
    print("proceed to register")

#Heading
Label(root, text="Login", font="ar 15").grid(row=0, column=3)


#Field Name
StudentName=Label(root,text="Student Name", padx=8, pady=8)
School=Label(root,text="School Code", padx=8, pady=8)
BCNO1=Label(root,text="Birth Certificate Number", padx=8, pady=8)
#Packing Field Name
StudentName.grid(row=1, column=2)
School.grid(row=2,column=2)
BCNO1.grid(row=3, column=2)

#Variables
StudentNamevalue=StringVar
SchoolCodevalue=StringVar
BCNOvalue=StringVar

checkvalue = IntVar
#Creating Entry Field
StudentNameentry = Entry(root, textvariable=StudentNamevalue)
SchoolCodeentry = Entry(root,textvariable=SchoolCodevalue)
BCNOentry = Entry(root, textvariable=BCNOvalue)


#Packing Entry Field
StudentNameentry.grid(row=1, column=3)
SchoolCodeentry.grid(row=2, column=3)
BCNOentry.grid(row=3, column=3)


#login
Button(text="Login", command=getval1).grid(row=4, column=2, padx=8, pady=8)
Button(text="Sign Up",command=getSignup).grid(row=4, column=3)
root.mainloop()