import pandas as pd
from tkinter import *
from tkinter import ttk
import random as rd


films = pd.read_csv('imdb_top_250.csv')
film_genres_list = list(films['Genre'])
l = len(film_genres_list)

complex_genres = []
for film_genre in film_genres_list:
    genres = film_genre.split(' | ')
    if len(genres) > 1:
        for genre in genres:
            film_genres_list.append(genre)
        complex_genres.append(film_genre)


for genre in complex_genres:
    film_genres_list.remove(genre)

genres_set = set(film_genres_list)
films_dict = dict()
for genre in genres_set:
    films_dict[genre] = []

for i in range(l):
    genres = films['Genre'][i].split(' | ')
    for genre in genres:
        films_dict[genre].append(films['Title'][i])


def calculate():
    try:
        value = str(genre.get())
        films = films_dict[value]
        random_film = films[rd.randint(0, len(films))]
        res.set(random_film)
    except ValueError:
        pass


root = Tk()
root.title("RANDOM FILM")
root.geometry("400x500")

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

genre = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=genre)
feet_entry.grid(column=2, row=1, sticky=(W, E))

res = StringVar()
ttk.Label(mainframe, textvariable=res).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Get random film", command=calculate).grid(column=2, row=3, sticky=E)
root.mainloop()
