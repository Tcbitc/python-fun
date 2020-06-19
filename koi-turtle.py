import turtle
from drawsvg import drawSVG

path = 'gif/koi.gif'
turtle.register_shape(path)

turtle.shape(path)
#t = turtle.Turtle(path)

drawSVG('svg/cat.svg', 'black')
#t.width(20)
#t.forward(50)

input('Press ENTER to continue')
