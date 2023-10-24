from random import randint, choice
from tkinter import *

WIDTH = 300
HEIGHT = 200


class Ball:
    def __init__(self, color):
        self.color = color
        self.R = randint(10, 50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (10, 10)
        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R, self.x + self.R,
                                          self.y + self.R, fill=self.color)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            self.dy = -self.dy

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)


def click_handler(event):
    random_color = "#"
    for i in range(6):
        random_color += choice('0 1 2 3 4 5 6 7 8 9 A B C D E F'.split())
    ball = Ball(random_color)
    balls.append(ball)


def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)


root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
canvas = Canvas(root)
canvas.pack()
canvas.bind('<Button-1>', click_handler)
balls = [Ball("red") for i in range(5)]
tick()
root.mainloop()