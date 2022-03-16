import tkinter as tk
from tkinter import Tk, ttk, messagebox
import time
from calendar import month
from datetime import date, datetime
import datetime as dt

root = tk.Tk()
root.title("DUTCH ARMY - REGISTRATION FORM")
root.geometry("512x512")

#Backend

todays_date = datetime.today()
Jaar = todays_date.year
Maand = todays_date.month
Dag = todays_date.day
#Backend
def checkRegister():
    if Age3.get() >= str(2007):
        messagebox.showwarning(title="Warning", message="This age is too young to register")
    if Name.get() == "":
        messagebox.showwarning(title="Warning", message="Please fill in a name")
    if Surname.get() == "":
        messagebox.showwarning(title="Warning", message="Please fill in a surname")
    if GenderValue.get() == "Robot":
        messagebox.showwarning(title="Warning", message="LOL you cant be a robot silly, please fill in a real gender")
    if Region.get() == "":
        messagebox.showwarning(title="Warning", message="Please fill in a region, or u live on the sea?!?")
    if Email.get() == "":
        messagebox.showwarning(title="Warning", message="Please use a valid email address")
    if Jobs.get() == "":
        messagebox.showwarning(title="Warning", message="Please select a department of the Army")
    PutInDictionary()
    
def PutInDictionary():
    global dic
    dic = {}
    
    dic["Name"] = Name.get()
    dic["Surname"] = Surname.get()
    dic["Email"] = Email.get()
    dic["Birthday"] = Age1.get() + "/" + Age2.get() + "/"  + Age3.get()
    dic["Gender"] = GenderValue.get()
    dic["Region"] = Region.get()
    dic["Job"] = Jobs.get()
    
    print(dic)
    

Regions=['North-Holland', 'South-Holland', 'Utrecht', 'Zeeland', 'Gelderland', 'Friesland', 'Groningen', 'Dhrente', 'Overijssel', 'Limburg', "Flevoland", "Noord-Brabant"]   
Job=["Royal Netherlands Navy", "Royal Netherlands Airforce", "Royal Netherlands Marechaussee", "Royal Netherlands Army"]

#Front-end
titel = tk.Label(
    root,
    text="REGISTRATION FORM",
    font= ('Franklin Gothic', 20, 'bold'),
    fg= "black"
)
titel.place(relx=0.5,rely=0.1, anchor = "center")
Subtitel = tk.Label(
    root,
    text="Ministry of Defence - Kingdom of the Netherlands",
    font= ('Franklin Gothic', 10, 'bold'),
    fg= "black"
)
Subtitel.place(relx=0.5,rely=0.14, anchor = "center")
SubmitButton = tk.Button(
    root,
    text="SUBMIT",
    font= ('Arial', 10, 'bold'),
    fg= "white",bg="#2e2e2e", borderwidth="0",
    command=checkRegister
) 
SubmitButton.place(relx=0.5,rely=0.9, anchor = "center")

NameValue = tk.StringVar(value="")
SurNameValue = tk.StringVar(value="")
AgeValue1 = tk.IntVar(value=Dag)
AgeValue2 = tk.IntVar(value=Maand)
AgeValue3 = tk.IntVar(value=Jaar)
EmailValue = tk.StringVar(value="")
RegionValue = tk.StringVar(value="")
JobValue = tk.StringVar(value="")
Name = tk.Entry(root,textvariable=NameValue,font= ('Franklin Gothic', 10, 'bold'),fg= "black",bg="#e0e0e0", borderwidth="0",)
NameText = tk.Label(root,text="Name",font= ('Arial', 10, 'italic'),fg= "black")
SurnameText = tk.Label(root,text="Surname",font= ('Arial', 10, 'italic'),fg= "black")
AgeText = tk.Label(root,text="Birthday",font= ('Arial', 10, 'italic'),fg= "black")
Surname = tk.Entry(root,textvariable=SurNameValue,font= ('Franklin Gothic', 10, 'bold'),fg= "black",bg="#e0e0e0", borderwidth="0",)
EmailText = tk.Label(root,text="Email",font= ('Arial', 10, 'italic'),fg= "black")
Email = tk.Entry(root,textvariable=EmailValue,font= ('Franklin Gothic', 10, 'bold'),fg= "black",bg="#e0e0e0", borderwidth="0",)
Region = ttk.Combobox(root,textvariable=RegionValue,font= ('Arial', 10),state ="readonly",width = 17)
RegionText = tk.Label(root,text="Region",font= ('Arial', 10, 'italic'),fg= "black")
Jobs = ttk.Combobox(root,textvariable=JobValue,font= ('Arial', 10),state ="readonly",width = 17)
JobsText = tk.Label(root,text="Job",font= ('Arial', 10, 'italic'),fg= "black")

# Birthday Selector
Age1 = ttk.Combobox(root,textvariable=AgeValue1,font= ('Arial', 10),state ="readonly",width = 4)
Age2 = ttk.Combobox(root,textvariable=AgeValue2,font= ('Arial', 10),state ="readonly",width = 4)
Age3 = ttk.Combobox(root,textvariable=AgeValue3,font= ('Arial', 10),state ="readonly",width = 4)
NameText.place(relx=0.2,rely=0.2, anchor = "center")
SurnameText.place(relx=0.2,rely=0.25, anchor = "center")
AgeText.place(relx=0.2,rely=0.3, anchor = "center")

# Gender Selector
Genders = (('Male'),('Female'),('Robot'))
GenderValue = tk.StringVar(value="")
GenderMale = tk.Radiobutton(root, text=Genders[0],value=Genders[0],variable=GenderValue,font= ('Arial', 10))
GenderFemale = tk.Radiobutton(root, text=Genders[1],value=Genders[1],variable=GenderValue,font= ('Arial', 10))
GenderRobot = tk.Radiobutton(root, text=Genders[2],value=Genders[2],variable=GenderValue,font= ('Arial', 10))
GenderText = tk.Label(root,text="Gender",font= ('Arial', 10, 'italic'),fg= "black")
GenderText.place(relx=0.2,rely=0.35, anchor = "center")

# Placing
Name.place(relx=0.4,rely=0.2, anchor = "center")
Surname.place(relx=0.4,rely=0.25, anchor = "center")
Age1.place(relx=0.31,rely=0.3, anchor = "center")
Age1['values'] = [number for number in range(1, 32)]
Age1.configure(background="#e0e0e0")
Age2.place(relx=0.41,rely=0.3, anchor = "center")
Age2['values'] = [number for number in range(1, 13)]
Age2.configure(background="#e0e0e0")
Age3.place(relx=0.51,rely=0.3, anchor = "center")
Age3.configure(background="#e0e0e0")
Age3['values'] = [number for number in range(1945, 2023)]
titel.place(relx=0.5,rely=0.1, anchor = "center")
GenderMale.place(relx=0.3,rely=0.35, anchor = "center")
GenderFemale.place(relx=0.45,rely=0.35, anchor = "center")
GenderRobot.place(relx=0.6,rely=0.35, anchor = "center")
Email.place(relx=0.4,rely=0.4, anchor = "center")
EmailText.place(relx=0.2,rely=0.4, anchor = "center")
Region.place(relx=0.4,rely=0.45, anchor = "center")
RegionText.place(relx=0.2,rely=0.45, anchor = "center")
Region['values'] = Regions
Jobs.place(relx=0.4,rely=0.5, anchor = "center")
JobsText.place(relx=0.2,rely=0.5, anchor = "center")
Jobs['values'] = Job

root.mainloop()