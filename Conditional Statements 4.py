from cProfile import label
from cgitb import text
from gettext import install
from re import A
import tkinter as tk
import math
import statistics
from tabulate import tabulate
from tkinter import *
from tkinter import ttk

root = tk.Tk()

root.title("Conditional Statements 4")

root.geometry('400x400')

mark = tk.Label(root, text = "Your Number Mark = ")
level = tk.Label(root, text = "Your Level = ")

mark.place(x = 15, y = 10)
level.place(x = 175, y = 10)

markbox = tk.Text(root, height = 1, width = 3, bg = "white")
levelbox = tk.Text(root, height = 1, width = 3, bg = "white")

markbox.place(x = 135, y = 10)
levelbox.place(x = 245, y = 10)

calbutton = tk.Button(root, text ="Calculate", command = lambda:calculate1(input = markbox.get(1.0, tk.END)))
calbutton.place(x = 290, y = 5, height = 25, width = 75)

s=ttk.Style()
s.theme_use("clam")

s.configure('Treeview', rowheight=20)

table = ttk.Treeview(root, column=("c1", "c2"), show='headings', height=14)
table['columns']= ('Number Mark', 'Level')
table.column("Number Mark",anchor=CENTER, width=100)
table.column("Level",anchor=CENTER, width=100)

table.heading("Number Mark",text="Number Mark")
table.heading("Level",text="Level")

table1 = table.insert('', 'end',text="1",values=('94+', '4+'))
table2 = table.insert('', 'end',text="2",values=('87-93', '4  '))
table3 = table.insert('', 'end',text="3",values=('80-86', '4-'))
table4 = table.insert('', 'end',text="4",values=('77-79', '3+'))
table5 = table.insert('', 'end',text="5",values=('74-76', '3  '))
table6 = table.insert('', 'end',text="6",values=('70-73', '3-'))
table7 = table.insert('', 'end',text="1",values=('67-69', '2+'))
table8 = table.insert('', 'end',text="1",values=('64-66', '2  '))
table9 = table.insert('', 'end',text="1",values=('60-63', '2-'))
table10 = table.insert('', 'end',text="1",values=('57-59', '1+'))
table11 = table.insert('', 'end',text="1",values=('54-56', '1  '))
table12 = table.insert('', 'end',text="1",values=('50-53', '1-'))
table13 = table.insert('', 'end',text="1",values=('0-49', 'R'))
table14 = table.insert('', 'end',text="1",values=('Less Than 0', 'No Mark'))

def calculate1(input):
    if str(input) >= "94":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "4+")

    elif str(input) >= "87":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "4")

    elif str(input) >= "80":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "4-")

    elif str(input) >= "77":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "3+")

    elif str(input) >= "74":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "3")

    elif str(input) >= "70":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "3-")

    elif str(input) >= "67":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "2+")

    elif str(input) >= "64":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "2")

    elif str(input) >= "60":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "2-")

    elif str(input) >= "57":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "1+")

    elif str(input) >= "54":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "1")

    elif str(input) >= "50":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "1-")

    elif str(input) >= "0":
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "R")

    else:
        levelbox.delete(1.0, tk.END)
        levelbox.insert(tk.END, "NA")

table.place(x = 200, y = 50, anchor='n')

root.mainloop()