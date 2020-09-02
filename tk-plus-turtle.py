from random import randint
from tkinter import *
from turtle import ScrolledCanvas, RawTurtle, TurtleScreen

health = 50
damage = 10
fight = randint(10, 20)
step = 0

def up():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(90)
    turtle.forward(10)

def down():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(-90)
    turtle.forward(10)

def left():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(180)
    turtle.forward(10)

def right():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(0)
    turtle.forward(10)

def combat():
    enemy = Turtle()
    enemy.up()
    eHealth = randint(20, 100)
    eDamage = randint(10, 20)

root = Tk()
canvas = ScrolledCanvas(root)
canvas.pack(side=LEFT)
screen = TurtleScreen(canvas)
turtle = RawTurtle(canvas)
turtle.up()

w = Scale(root, from_=0, to=42)
w.pack()
w = Scale(root, from_=0, to=200, orient=HORIZONTAL)
w.pack()

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

screen.mainloop()
