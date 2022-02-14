import tkinter as tk
import time
import random

root = tk.Tk()
root.title("Clicker V5")
root.geometry("1000x1000")
root.configure(background= "gray")
count = 0
countCheckBox = ""
BoxState = "disabled"

def autoClick():
    global countCheckBox
    CountClick = AutoclickBox.get()
    if CountClick == 1:
        if countCheckBox == "Up":
            UpF()
        elif countCheckBox == "Down":
            DownF()
        root.after(100,autoClick)

    
def DoubleClickEvent(event):
    global count, checkbutton
    if checkbutton == "Multi":
        count *= 3
    elif checkbutton == "Dev":
        count /= 3
    Number.configure(text= count)
    Autoclick.configure(state = "normal")

def Background(event):
    root.configure(bg= "Yellow")

def Color(event):
    if count > 0:
        root.configure(background= "green")
    elif count < 0:
        root.configure(background= "red")
    else:
        root.configure(background= "gray")

def UpF():
    global count, checkbutton
    count += 1
    Number.configure(text= count)
    Color("")
    checkbutton = "Multi"
    Autoclick.configure(state = "normal")
def UpB(event):
    UpF()

def DownF():
    global count, checkbutton
    count -= 1
    Number.configure(text= count)
    Color("")
    checkbutton = "Dev"
    Autoclick.configure(state = "normal")
def DownB(event):
    DownF()

def SpaceB(event):
    DoubleClickEvent("")

Up = tk.Button(
    root,
    text= "Up",
    font= ('Calibri', 40, 'bold'),
    fg= "white",
    bg= "Black",
    command= UpF
)
Up.pack()

AutoclickBox = tk.IntVar()
Autoclick = tk.Checkbutton(
    root,
    variable = AutoclickBox,
    command=autoClick,
    text="Autoclick",
    font= ('Calibri', 20, 'bold'),
    bg="white",
    state="disabled",
    onvalue = 1, 
    offvalue = 0,
)

Number = tk.Label(
    root,
    text= count,
    font= ('Calibri', 40, 'bold'),
    fg= "white",
    bg= "Black",
)
Number.pack()
Autoclick.pack()

Down = tk.Button(
    root,
    text= "Down",
    font= ('Calibri', 40, 'bold'),
    fg= "white",
    bg= "Black",
    command= DownF
)
Down.pack()

Down.pack()
Number.bind("<Enter>", Background)
Number.bind("<Leave>", Color)
Number.bind("<Double-Button>", DoubleClickEvent)
root.bind("<e>", SpaceB) 
root.bind("<Up>", UpB) and root.bind("<+>", UpB)
root.bind("<Down>", DownB) and root.bind("-", DownB)

root.mainloop()