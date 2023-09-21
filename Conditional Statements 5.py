from cProfile import label
from cgitb import text
from gettext import install
from re import A
from time import sleep
import tkinter as tk
import math
import statistics
from tokenize import Number
from tabulate import tabulate
from tkinter import *
from tkinter import ttk
import random

random = random.randint(1, 100)
print(random)

root = tk.Tk()

root.title("Conditional Statements 5")

root.geometry('350x100')

guess = tk.Label(root, text = "Your Guess: ")
guess.configure(font=("Arial", 17, ""))
guess.place(x = 10, y = 20)

box = tk.Text(root, height = 1, width = 17, bg = 'white')
box.configure(font=("Arial", 15, ""))
box.place(x = 140, y = 23)

button = tk.Button(root, text = "Guess", command = lambda:login(number = box.get(1.0, tk.END)))
button.configure(font=("Arial", 12, ""))
button.place(x = 175, y = 55, anchor='n')

x = 0
def login(number):
    global x
    if x <= 1:
        if int(number) == random:
            root.destroy()
            rooot = tk.Tk()
            rooot.title("Answer")
            rooot.geometry('350x100')
            guess = tk.Label(rooot, text = "You Got It!")
            guess.configure(font=("Arial", 17, ""))
            guess.place(x = 10, y = 20)
            rooot.mainloop()
            sleep(5)
            quit()
        elif int(number) > random: 
            box.delete(1.0, tk.END)
            box.insert(tk.END, "Too High")
        elif int(number) < random: 
            box.delete(1.0, tk.END)
            box.insert(tk.END, "Too Low")
    else:
        root.destroy()
        rooot = tk.Tk()
        rooot.title("Answer")
        rooot.geometry('350x100')
        guess = tk.Label(rooot, text = "The Number Was " + str(random))
        guess.configure(font=("Arial", 17, ""))
        guess.place(x = 10, y = 20)
        rooot.mainloop()
        sleep(5)
        quit()
    x += 1



root.mainloop()