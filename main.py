import tkinter as tk
import datetime

def calculate_age():
    birth_year = int(entry.get())
    current_year = datetime.datetime.now().year
    age = current_year - birth_year
    label.config(text=f"You are {age} years old")

root = tk.Tk()
root.title("Age Calculator")

label1 = tk.Label(root, text="Please enter your birth year:")
label1.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Calculate Age", command=calculate_age)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()