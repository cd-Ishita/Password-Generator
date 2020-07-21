from tkinter import *

window=Tk()

def kg_to_gm():
    grams = float(kg.get())*1000
    t1.insert(END,grams)

def kg_to_pounds():
    pounds = float(kg.get())*2.20462
    t2.insert(END,pounds)

def kg_to_ounces():
    ounces = float(kg.get())*35.274
    t3.insert(END,ounces)

l1 = Label(window, text="Kg")
l1.grid(row=0, column=0)

kg = StringVar()
e1 = Entry(window, textvariable=kg)
e1.grid(row=0, column=1)

b1=Button(window, text = "Convert", command = lambda:[kg_to_gm(), kg_to_pounds(), kg_to_ounces()])
b1.grid(row=0, column=2)

t1=Text(window, height=1, width=10)
t1.grid(row=1, column=0)

t2=Text(window, height=1, width=10)
t2.grid(row=1, column=1)

t3=Text(window, height=1, width=10)
t3.grid(row=1, column=2)

window.mainloop()
