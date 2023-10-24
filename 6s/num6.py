import matplotlib.pyplot as plt
import pandas as pd
from tkinter import *
from tkinter import ttk


def LeastSquareMethod(x, y):
    n = len(x)
    sum_xy = sum([x[i] * y[i] for i in range(0, n)])
    sum_x2 = sum([i ** 2 for i in x])
    a = (n * sum_xy - sum(x) * sum(y)) / (n * sum_x2 - (sum(x) ** 2))
    b = (sum(y) - a * sum(x)) / n
    return [a, b]


def calculate():
    try:
        value = str(file.get())
        fig = plt.figure(figsize=(16, 9))
        graf2 = fig.add_subplot()
        laba = pd.read_csv(value, delimiter=';')

        X = [int(i) for i in laba["X"]]
        Y = [int(i.replace(',', '.')) for i in laba["Y"]]
        print(X)

        graf2.plot(X, Y, '.', label='Accurate values')
        graf2.set_title('Graph', fontdict={'fontname': 'sans-serif', 'fontsize': 20})
        graf2.set_xlabel('X, cm')
        graf2.set_ylabel('Y, cm')

        coeff = LeastSquareMethod(X, Y)
        graf2.plot(X, [(x * coeff[0] + coeff[1]) for x in X], label='Approximated values', color="r")
        graf2.legend()

        print("Approximating line coefficients: a = ", coeff[0], "b = ", coeff[1])

        plt.show()

    except ValueError:
        pass


root = Tk()
root.title("CALCULATOR")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

file = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=file)
feet_entry.grid(column=2, row=1, sticky=(W, E))

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=2, row=3, sticky=E)
root.mainloop()
