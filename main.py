print("none")
import tkinter as tk

def button_click():
    pass

root = tk.Tk()
root.title("My Window")

button = tk.Button(root, text="Click me!", command=button_click)
button.pack()

root.mainloop()
