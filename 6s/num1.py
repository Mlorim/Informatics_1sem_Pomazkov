from tkinter import *
from tkinter import ttk


def calculate():
    try:
        value = str(problem.get())
        res.set(eval(value))
    except ValueError:
        pass


root = Tk()
root.title("CALCULATOR")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

problem = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=problem)
feet_entry.grid(column=2, row=1, sticky=(W, E))

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=3, sticky=E)
root.mainloop()
