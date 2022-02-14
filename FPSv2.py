from tkinter import *
import tkinter as tk
import time
import random
from tkinter import messagebox

root = tk.Tk()
root.configure(bg="#363b42")
root.title("FPS Trainer V2")
root.geometry("512x512")

# Variables used for main-FPS
timer = 0
timeValue = tk.IntVar(value=0)
point = 0
seconds = 0

Buttons = ["<Button>", "<Double-Button>", "<Triple-Button>", "<W>", "<S>", "<D>", "<a>", "<space>"]
ButtonsShower = ["Left-Click", "Dubble-Click", "Tripple-Click", "W", "S", "D", "A", "Spacebar"]

ButtonRandomizer = random.choice(ButtonsShower)

def update_value():
    ButtonRandomizer = random.choice(ButtonsShower)
    button1.configure(text= "Press: " + str(ButtonRandomizer))
    
# Events for Countdown
def update_position():
    button1.place(x=random.randint(0,385), y=random.randint(75,450))    

def start_button():
    start.destroy()
    Entry.place(relx = 0.5, rely = 0.5, anchor = "center")
    Button_Confirm.place(relx = 0.814, rely = 0.65, anchor = "center")
    Title.place(relx = 0.5, rely = 0.3, anchor = "center")
    
def Entry_Input():
    global timer
    timer = timeValue.get()
    Entry.destroy()
    Title.destroy()
    Button_Confirm.destroy()
    button1.pack(ipadx = 0.5, ipady = 0.5, anchor = "center")
    count_down()

def count_down():
    global timer
    global seconds
    if timer > 0:
        timer = timer - 1
        seconds += 1
        counter.config(text="Time Left: " + str(timer))
        root.after(1000, count_down)
        counter.pack(anchor = "nw", ipadx = 0.5, ipady = 0)
        points.pack()
        points.place(relx = 1, rely = 0, anchor = "ne")
        if timer == 0:
            game_over()
def game_over():
    global timer
    if timer == 0:
        Question = messagebox.askyesno(title= "Game over!", message="You got: " + (str(point)) + " Points | Your Time: " + str((seconds)))
        if Question:
            print("<---------------->")
            print("<--GAME RESULTS-->")
            print("Your Score: " + (str(point)))
            print("Your time: " + str((seconds)))
            print("<---------------->")
            time.sleep(1)
            restart_program()
        else:    
            print("<---------------->")
            print("<--GAME RESULTS-->")
            print("Your Score: " + (str(point)))
            print("Your time: " + str((seconds)))
            print("<---------------->")
            time.sleep(2)
            root.destroy()
            exit()
def restart_program():
    Entry_Input()
        
# Events for Points and Buttons
def Keybind(event):
    Button_Pressed()
    
def ClickEvent(event):
    global point
    point = point + 1
    Button_Pressed()

def Button_Pressed():
    global point
    update_position()
    update_value()
    point = point + 1
    points.configure(text="Points: " + str(point))
    print("You got a point")

# importing GUI's for the game    
    
counter = tk.Label(
    root,
    text="Time left: " + str(timer),
    font= ('Calibri', 15, 'bold'),
    fg= "white",
    bg= "#1f1f1f", borderwidth="0",
)
points = tk.Label(
    root,
    text="Points: " + str(point),
    font= ('Calibri', 15, 'bold'),
    fg= "white",
    bg= "#1f1f1f", borderwidth="0",
)

start = tk.Button(
    root,
    text= "START TRAINING",
    font= ('Calibri', 40, 'bold'),
    fg= "white",
    bg= "#1f1f1f", borderwidth="0",
    activebackground="white",
    command=start_button,
)
start.pack()
start.place(relx = 0.5, rely = 0.5, anchor = "center")

# Coding Keybinds

button1 = tk.Button(
    root,
    text= "Press: " + str(ButtonRandomizer),
    font= ('Calibri', 20, 'bold'),
    fg= "white",
    bg= "#1f1f1f", borderwidth="0",
    activebackground="white",
    command=Button_Pressed,
)

Entry = tk.Entry(
    root,
    textvariable= timeValue,
    font= ('Calibri', 30, 'bold'),
    fg= "white",
    bg= "#1f1f1f", borderwidth="0",
)
Button_Confirm = tk.Button(
    root,
    text= "Select",
    font= ('Calibri', 20, 'bold'),
    fg= "white",
    bg= "#1f1f1f", borderwidth="0",
    command=Entry_Input
)
Title = tk.Label(
    root,
    text= "Input a Time",
    font= ('Calibri', 20, 'bold'),
    fg= "white",
    bg= "#1f1f1f", borderwidth="0",
)

# Binding Keys:
if ButtonsShower[3]:
    root.bind("w", Keybind)
if ButtonsShower[4]:
    root.bind("s", Keybind)
if ButtonsShower[6]:
    root.bind("a", Keybind)
if ButtonsShower[5]:
    root.bind("d", Keybind)
if ButtonsShower[7]:
    root.bind("<space>", Keybind)

# Binding Mouseclicks
button1.bind("<Button>", ClickEvent)
button1.bind("<Double-Button>", ClickEvent)
button1.bind("<Triple-Button>", ClickEvent)


root.mainloop()