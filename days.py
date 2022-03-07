import tkinter as tk
from tkinter import Tk, ttk
from tkinter import messagebox
from calendar import month, month_name
from datetime import date, datetime
import datetime as dt


root = tk.Tk()
root.title("Calculate Your Time")
root.configure(bg="#363b42")
root.geometry("512x512")

todays_date = datetime.today()
Jaar = todays_date.year
Maand = todays_date.month
Dag = todays_date.day

def CalculateDays():
    global number
    global Month
    Days = int(selected_day.get())
    Month = selected_month.get()
    Year = int(Select_year.get())
    ConvertMonthNumber = dt.datetime.strptime(Month, "%B")
    Monthnumber = ConvertMonthNumber.month
    All = dt.datetime(Year, Monthnumber, Days)
    today = datetime.today()
    difference = All - today
    number = difference.days
    MessageBoxes()

def MessageBoxes():
    global number
    if number > 0:
        if number == 1:
            messagebox.showinfo(title="Calculated", message="Dit is: " + str(number) + " dag in de toekomst.")
        else:
            messagebox.showinfo(title="Calculated", message="Dit zijn: " + str(number) + " dagen in de toekomst.")
    elif number < 0:
        if -number == 1:
            messagebox.showinfo(title="Calculated", message="Dit is: " + str(number) + " dag geleden")
        else:
            messagebox.showinfo(title="Calculated", message="Dit zijn: " + str(number) + " dagen geleden")
    else:
        messagebox.showinfo(title="Calculated", message="Dit is vandaag")



Label = tk.Label(
    root,
    text="Time",
    font= ('Calibri', 20, 'bold'),
    fg="white",
    bg="black",
)
Label.place(relx = 0.5, rely = 0.4, anchor = "center")

selected_month = tk.StringVar(value= Maand)
selected_day = tk.IntVar(value= Dag)

month_Box = ttk.Combobox(
    root, 
    textvariable=selected_month,
)
month_Box.place(relx = 0.2, rely = 0.5 , anchor = "center")
month_Box['values'] = [month_name[m] for m in range(1, 13)]
month_Box['state'] = 'readonly'

day_Box = ttk.Combobox(
    root, 
    textvariable=selected_day,
)
day_Box.place(relx = 0.5, rely = 0.5 , anchor = "center")
day_Box['values'] = [number for number in range(1, 31)]
day_Box['state'] = 'readonly'

Select_year = tk.IntVar(value = Jaar)
years = tk.Entry(
    root,
    textvariable= Select_year,
    
)
years.place(relx = 0.8, rely = 0.5 , anchor = "center")

GoButton = tk.Button(
    root,
    text= "Go",
    font= ('Calibri', 15, 'bold'),
    fg= "white",
    bg= "#1f1f1f", borderwidth="0",
    command=CalculateDays
)
GoButton.place(relx = 0.5, rely = 0.6, anchor = "center")




root.mainloop()