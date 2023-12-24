print("none")
import tkinter as tk
from tkinter import messagebox
import datetime
def show_time():
    current_time = "Current time: " + str(datetime.datetime.now())
    messagebox.showinfo("Current Time", current_time)

root = tk.Tk()
root.title("Click me to show time")
button1 = tk.Button(root, text="qingli!", command=show_time)
button = tk.Button(root, text="time!", command=show_time)
button.pack()
button1.pack()

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

