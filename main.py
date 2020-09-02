
"""
from math import sin
from processing import *

X = 30
Y = 30
delay = 16
radius = 30

def setup():
    strokeWeight(10)
    frameRate(20)
    size(300,300)

def ellipseFun():
    global X, Y, radius
    background(100)
    fill(0,121,184)
    stroke(255)
    fc = environment.frameCount

    X += (mouse.x-X)/delay;
    Y += (mouse.y-Y)/delay;

    radius = radius + sin(fc / 4)

    ellipse(X,Y,radius,radius)


draw = ellipseFun 
run()

"""

import numguss
