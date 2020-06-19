from math import *
from colorsys import hsv_to_rgb
import turtle

def plot(turt, mn, mx, fx, fy, steps=100):
    for it in range(0, steps+1):
        t = (mx-mn) * it / steps + mn
        x = fx(t)
        y = fy(t)
        progress = it / steps
        print(f'{t} -> ({x}, {y}) [{100 * progress}%]')
        hue = progress
        saturation = 1
        brightness = 1
        color = hsv_to_rgb(hue, saturation, brightness)
        turt.color(color)
        turt.goto(x, y)
        turt.pendown()

turt = turtle.Turtle()
turt.penup()
turt.speed(1000)

def x(t): return 10 * (4*(1-t)+1*t) * sin(3*6.2832*t)
def y(t): return 10 * (4*(1-t)+1*t) * cos(3*6.2832*t)
plot(turt, 1, 10, x, y)

# Zigzag away!
turt.penup()
turt.speed(200)
turt.left(90)
x = turt.xcor()
y = turt.ycor()
for it in range(150):
    x += 5 * cos(pi * it / 5)
    y += 5
    turt.goto(x, y)

input("Press Enter to continue...")


#--------------------------------------------------

"""
plot(-8, 8,
    lambda t: 100 * sin(13.58*t) * round(sqrt(cos(cos(7.4*t)))),
    lambda t: 100 * cos(13.58*t)**4 * sin(7.4*t)**2
)

plot(-3, -3,
    lambda t: 200 * sin(4.84 * t) / (1 + cos(4.66 * t) ** 2),
    lambda t: 200 * cos(4.66 * t) * sin(4.84 * t) ** 4
)
"""
"""
plot(0, 2 * pi,
    lambda t: 300 * cos(t),
    lambda t: 200 * sin(t),
)
"""
