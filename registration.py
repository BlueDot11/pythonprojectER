from cProfile import label
from cgitb import text
#from cgitb import text
#from codecs import Codec
#from logging import root
from tkinter import *
#from tkinter import font
#from tkinter.tix import COLUMN

#from importlib_metadata import entry_points
root=Tk()
root.geometry("400x700")
def getvals():
    print("Successiful")

#Heading
Label(root, text="Register", font="ar 15 bold").grid(row=0, column=3)

#Field Name
FirstName=Label(root,text="First Name", padx=8, pady=8)
MiddleName=Label(root,text="Middle Name", padx=8, pady=8)
LastName=Label(root,text="Last Name", padx=8, pady=8)
SchoolCode=Label(root,text="School Code", padx=8, pady=8)
BCNO=Label(root,text="Birth Certificate Number", padx=8, pady=8)
County=Label(root,text="Your County", padx=8, pady=8)
SubCounty=Label(root,text="Sub County", padx=8, pady=8)
DOB=Label(root,text="Date of Birth", padx=8, pady=8)
PhoneNumber=Label(root,text="Pnone Number", padx=8, pady=8)
GenderType=Label(root,text="Gender", padx=8, pady=8)
#Packing Fields
FirstName.grid(row=1, column=2)
MiddleName.grid(row=2, column=2)
LastName.grid(row=3, column=2)
SchoolCode.grid(row=4, column=2)
BCNO.grid(row=5, column=2)
County.grid(row=6, column=2)
SubCounty.grid(row=7, column=2)
DOB.grid(row=8, column=2)
PhoneNumber.grid(row=9, column=2)
GenderType.grid(row=10, column=2)

#Variables for storing data
FirstNamevalue=StringVar
MiddleNamevalue=StringVar
LastNamevalue=StringVar
SchoolCodevalue=StringVar
BCNOvalue=StringVar
Countyvalue=StringVar
SubCountyvalue=StringVar
DOBvalue=StringVar
PhoneNumbervalue=StringVar
GenderTypevalue=StringVar

checkvalue = IntVar

#Creating Entry Field
FirstNameentry = Entry(root, textvariable=FirstNamevalue)
Middlenameentry = Entry(root, textvariable=MiddleNamevalue)
LastNameentry = Entry(root, textvariable=LastNamevalue)
SchoolCodeentry = Entry(root, textvariable=SchoolCode)
BCNOentry = Entry(root, textvariable=BCNOvalue)
Countyentry = Entry(root, textvariable=Countyvalue)
SubCountyentry = Entry(root, textvariable=SubCountyvalue)
DOBentry = Entry(root, textvariable=DOBvalue)
PhoneNumberentry = Entry(root, textvariable=PhoneNumbervalue)
GenderTypeentry = Entry(root, textvariable=GenderTypevalue)

#Packing Entry Field
FirstNameentry.grid(row=1, column=3)
Middlenameentry.grid(row=2, column=3)
LastNameentry.grid(row=3, column=3)
SchoolCodeentry.grid(row=4, column=3)
BCNOentry.grid(row=5, column=3)
Countyentry.grid(row=6, column=3)
SubCountyentry.grid(row=7,column=3)
DOBentry.grid(row=8, column=3)
PhoneNumberentry.grid(row=9, column=3)
GenderTypeentry.grid(row=10, column=3)


#Creating a checkbox
checkbtn=Checkbutton(text="Remember me?",variable=checkvalue, padx=8, pady=8)
checkbtn.grid(row=11,column=3)


#submit button
Button(text="Register", command=getvals).grid(row=12, column=3, padx=8, pady=8)


root.mainloop()