print("none")
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def show_time():
    current_time = "Current time: " + str(datetime.datetime.now())
    messagebox.showinfo("Current Time", current_time)

root = tk.Tk()
root.title("Click me to show time")
button1 = tk.Button(root, text="qingli!", command=show_time)
button = tk.Button(root, text="time!", command=show_time)
button.pack()
button1.pack()
current_time = datetime.datetime.now()
print("The current time is:", current_time.strftime("%H:%M:%S"))
root.mainloop()




class ClockApp(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent

        self.time = tk.StringVar()
        self.time.set(datetime.datetime.now().strftime("%H:%M:%S"))

        self.button = ttk.Button(self.parent, textvariable=self.time, takefocus=0)
        self.button.pack(side="bottom", fill="x", expand=True)

        self.pack()
        self.after(1000, self.update)  # update once per second

    def update(self):
        self.time.set(datetime.datetime.now().strftime("%H:%M:%S"))
        self.after(1000, self.update)  # update once per second


root = tk.Tk()
root.title("Clock")
root.configure(background="black")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

ClockApp(root)

root.mainloop()

import psutil

processes = psutil.process_iter(['pid', 'name'])

for process in processes:
    try:
        memory_info = process.memory_info()
        connections = process.connections()
        if connections:
            print(f"Process {process.info['name']} (PID: {process.info['pid']})")
            print(f"Memory: {memory_info}")
            print("Connections:")
            for conn in connections:
                print(f"  {conn}")
            print()
    except psutil.AccessDenied:
        pass
    except psutil.Error as err:
        print(err)

