from tkinter import *
from tkinter import ttk


def calculate():
    try:
        m = float(mass.get())
        h = float(heigth.get())
        bmi = int(m / (h**2))
        res.set(str(bmi))
        if bmi <= 16:
            recom.set('Выраженный дефицит массы тела')
        elif 16 < bmi < 18.5:
            recom.set('Недостаточная (дефицит) масса тела')
        elif 18.5 < bmi < 25:
            recom.set('Норма')
        elif 25 < bmi < 30:
            recom.set('Избыточная масса тела (предожирение)')
        elif 30 < bmi < 35:
            recom.set('Ожирение 1 степени')
        elif 35 < bmi < 40:
            recom.set('Ожирение 2 степени')
        else:
            recom.set('Ожирение 3 степени')
    except ValueError:
        pass


WIDTH = 300
HEIGHT = 200

root = Tk()
root.title("BMI")


mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.geometry(f'{WIDTH}x{HEIGHT}')

label = Label(mainframe, bg='red', text="Mass (kg)").grid(column=1, row=1)
label = Label(mainframe, bg='red', text="Hieght (m)").grid(column=1, row=3)

mass = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=mass)
feet_entry.grid(column=1, row=2)

heigth = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=heigth)
feet_entry.grid(column=1, row=4)

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=5)

recom = StringVar()
ttk.Label(mainframe, textvariable=recom).grid(column=2, row=6)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=5, sticky=E)

root.mainloop()
