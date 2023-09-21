import tkinter as tk
import math
import statistics
from tabulate import tabulate
from tkinter import *
from tkinter import ttk

root = tk.Tk()

root.title("Conditional Statements 3")

root.geometry('350x100')

username = tk.Label(root, text = "Password: ")
username.configure(font=("Arial", 17, ""))
username.place(x = 20, y = 20)

box = tk.Text(root, height = 1, width = 17, bg = 'white')
box.configure(font=("Arial", 15, ""))
box.place(x = 140, y = 23)

def login(user):
    if user == "password\n" or user == "1234\n":
        box.delete(1.0, tk.END)
        box.insert(tk.END, "Weak Password")
    else:
        box.delete(1.0, tk.END)
        box.insert(tk.END, "Password Accepted")

button = tk.Button(root, text = "Login", command = lambda:login(box.get(1.0, tk.END)))
button.configure(font=("Arial", 12, ""))
button.place(x = 175, y = 55, anchor='n')

root.mainloop()