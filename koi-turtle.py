import turtle
from drawsvg import drawSVG

path = 'gif/koi.gif'
turtle.register_shape(path)

turtle.shape(path)

drawSVG('svg/cat.svg', 'black')

input('Press ENTER to continue')
