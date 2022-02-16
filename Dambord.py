import tkinter as tk
root= tk.Tk()
root.geometry("635x635")
root.configure(bg="#363b42")

root.title("Dambord - ©CodeAura")
Bord = tk.Frame(root)

value = False
for i in range(10):
    if value == True:
        value = False
    else:
        value = True
    for x in range(10):
        if value == True:
            color = "black"
            value = False
        else:
            color = "white"
            value = True
        tiles = tk.Label(
            root,
            bg= color,
            padx = 30, pady = 20
        )
        tiles.grid(row = x, column = i)
Bord.place(relx = 0.5, rely = 0.5, anchor = "center")

root.mainloop()