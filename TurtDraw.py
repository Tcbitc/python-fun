from turtle import *

screen_turt = Turtle(1)
screen_turt.hideturtle()

screen_turt.tracer(0,0)
screen_turt.penup()

def draw_palette():
  pose = -180
  z=1
  for color in ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'black', 'black']:
    pose += 36
    screen_turt.goto(pose,150)
    screen_turt.color(color)
    screen_turt.dot(30)
  
  # black border around white color
  screen_turt.color('white')
  screen_turt.dot(28)
  
  # dot maker button
  pose += 36
  screen_turt.goto(pose,150)
  screen_turt.color('black')
  screen_turt.dot(30)
  screen_turt.color('red')
  screen_turt.dot(20)
  screen_turt.color('black')
  screen_turt.dot(15)
  screen_turt.color('white')
  screen_turt.dot(14)

  screen_turt.update()

draw_palette()

screen = Screen()

t = Turtle()
t.pendown()

def set_color(c):
  t.pendown()
  t.color(c)
  t.update()

def draw_dot():
  t.dot(20)
  t.update()

def click(x,y):
  coord_mapping = [
    (-162, -125, 144, 166, lambda: set_color('red')),
    (-126, -89, 144, 166, lambda: set_color('orange')),
    (-90, -53, 144, 166, lambda: set_color('yellow')),
    (-54, -17, 144, 166, lambda: set_color('green')),
    (-18, 19, 144, 166, lambda: set_color('blue')),
    (18, 55, 144, 166, lambda: set_color('violet')),
    (54, 91, 144, 166, lambda: set_color('black')),
    (90, 127, 144, 166, lambda: t.penup()),
    (126, 163, 144, 166, lambda: draw_dot())
  ]
  for (xmin, xmax, ymin, ymax, f) in coord_mapping:
    if x > xmin and x < xmax and y > ymin and y < ymax:
      f()

screen.onclick(click)

def drag(x,y):
  t.goto(x, min(y, 120))
  t.update()

t.ondrag(drag)
t.update()

from tkinter import *

