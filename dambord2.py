import tkinter as tk
root= tk.Tk()
root.geometry("300x300")
canvas = tk.Canvas(root)
canvas.pack()
root.title("Dambord")
root.configure(bg="#363b42")

color = "white"
Size = 26
width = 0
for y in range(50):
    for x in range(50):
        x1 = x*Size+width
        y1 = y*Size+width
        x2 = x1 + Size
        y2 = y1 + Size
        canvas.create_rectangle((x1, y1, x2, y2), fill=color)
        if color == 'white':
            color = 'black'
        else:    
            color = 'white'
    if color == 'white':
        color = 'black'
    else:    
        color = 'white'

root.mainloop()