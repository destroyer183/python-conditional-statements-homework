from cProfile import label
from cgitb import text
from gettext import install
from re import A
import tkinter as tk
import math
import statistics
from tkinter import *
from tkinter import ttk

root = tk.Tk()

root.title("Conditional Statements 1")

root.geometry('400x250')

var1 = -7
var2 = -1

varSubmit = tk.Button(root, text ="Submit", command = lambda:Submitvar(a = v11.get(1.0, tk.END), b = v21.get(1.0, tk.END)))
varSubmit.place(x=175, y=5, height = 25, width = 75)

varDefault = tk.Button(root, text ="Default", command = lambda:Defaultvar())
varDefault.place(x = 275, y = 5, height = 25, width = 75)

def Submitvar(a, b):
    global var1, var2
    var1 = float(a)
    var2 = float(b)

def Defaultvar():
    var1 = -7
    var2 = -1
    v11.delete(1.0, tk.END)
    v21.delete(1.0, tk.END)
    v11.insert(tk.END, var1)
    v21.insert(tk.END, var2)

v1 = tk.Label(root, text = "a = ")
v2 = tk.Label(root, text = "b = ")

v1.place(x = 40, y = 10)
v2.place(x = 95, y = 10)

v11 = tk.Text(root, height = 1, width = 3, bg = "white")
v21 = tk.Text(root, height = 1, width = 3, bg = "white")

v11.place(x = 80, y = 10, anchor='n')
v21.place(x = 135, y = 10, anchor='n')

v11.insert(tk.END, "-7")
v21.insert(tk.END, "-1")

def calculate1(var1, var2):
    global bool1, bool2, bool3, bool4, bool5, bool6, table1, table2, table3, table4, table5, table6
    bool1 = var1 == var2
    bool2 = var1 != var2
    bool3 = var1 > var2
    bool4 = var1 < var2
    bool5 = var1 <= var2
    bool6 = var1 >= var2
    table.delete(table1)
    table.delete(table2)
    table.delete(table3)
    table.delete(table4)
    table.delete(table5)
    table.delete(table6)
    table1 = table.insert('', 'end',text="1",values=('a == b', str(bool1)))
    table2 = table.insert('', 'end',text="2",values=('a !=b', str(bool2)))
    table3 = table.insert('', 'end',text="3",values=('a > b', str(bool3)))
    table4 = table.insert('', 'end',text="4",values=('a < b', str(bool4)))
    table5 = table.insert('', 'end',text="5",values=('a <= b', str(bool5)))
    table6 = table.insert('', 'end',text="6",values=('a >= b', str(bool6)))

s=ttk.Style()
s.theme_use('clam')

s.configure('Treeview', rowheight=20)

table = ttk.Treeview(root, column=("c1", "c2"), show='headings', height=6)
table['columns']= ('id', 'full_Name')
table.column("id",anchor=CENTER, width=120)
table.column("full_Name",anchor=CENTER, width=120)

table.heading("id",text="Boolean Expression")
table.heading("full_Name",text="Result")

table1 = table.insert('', 'end',text="1",values=('a == b', ''))
table2 = table.insert('', 'end',text="2",values=('a !=b', ''))
table3 = table.insert('', 'end',text="3",values=('a > b', ''))
table4 = table.insert('', 'end',text="4",values=('a < b', ''))
table5 = table.insert('', 'end',text="5",values=('a <= b', ''))
table6 = table.insert('', 'end',text="6",values=('a >= b', ''))

Calculate = tk.Button(root, text ="Calculate", command = lambda:calculate1(var1, var2))
Calculate.place(x = 200, y = 200, anchor='n')

table.place(x = 200, y = 45, anchor='n')
root.mainloop()