from tkinter import *
from tkinter import ttk


def calculate():
    try:
        value = str(color.get())
        xx = 255 - int(value[1:3], 16)
        yy = 255 - int(value[3:5], 16)
        zz = 255 - int(value[5:], 16)
        clr = '#' + hex(xx)[2:] + hex(yy)[2:] + hex(zz)[2:]
        res.set(clr)
        label.config(bg=clr)

    except ValueError:
        pass


root = Tk()
root.title("COLOR CALCULATOR")


mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

label = Label(mainframe, pady=5, text="Color (#XXXXXX)")
label.grid(column=1, row=1)
color = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=color)
feet_entry.grid(column=2, row=1, sticky=(W, E))

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=2, sticky=E)
root.mainloop()