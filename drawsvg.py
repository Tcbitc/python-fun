# -*- coding: utf-8 -*-
# Author: tfx2001
# License: GNU GPLv3
# Time: 2018-08-09 18:27

# Source:
# https://github.com/tfx2001/python-turtle-draw-svg/blob/master/main.py

import re
import turtle as te
from bs4 import BeautifulSoup

WriteStep = 15
Speed = 1000
Width = 600
Height = 600
Xh = 0
Yh = 0
scale = (1, 1)
first = True
K = 32


def debug(s):
    #print(s)
    pass


def Bezier(p1, p2, t):
    debug(f'Bezier({p1}, {p2}, {t})')
    return p1 * (1 - t) + p2 * t


def Bezier_2(x1, y1, x2, y2, x3, y3):
    debug(f'Bezier_2({x1}, {y1}, {x2}, {y2}, {x3}, {y3})')
    te.goto(x1, y1)
    te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(x1, x2, t / WriteStep),
                   Bezier(x2, x3, t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(y1, y2, t / WriteStep),
                   Bezier(y2, y3, t / WriteStep), t / WriteStep)
        te.goto(x, y)
    te.penup()


def Bezier_3(x1, y1, x2, y2, x3, y3, x4, y4):
    debug(f'Bezier_3({x1}, {y1}, {x2}, {y2}, {x3}, {y3, x4, y4})')
    x1 = -Width / 2 + x1
    y1 = Height / 2 - y1
    x2 = -Width / 2 + x2
    y2 = Height / 2 - y2
    x3 = -Width / 2 + x3
    y3 = Height / 2 - y3
    x4 = -Width / 2 + x4
    y4 = Height / 2 - y4
    te.goto(x1, y1)
    te.pendown()
    for t in range(0, WriteStep + 1):
        x = Bezier(Bezier(Bezier(x1, x2, t / WriteStep), Bezier(x2, x3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(x2, x3, t / WriteStep), Bezier(x3, x4, t / WriteStep), t / WriteStep), t / WriteStep)
        y = Bezier(Bezier(Bezier(y1, y2, t / WriteStep), Bezier(y2, y3, t / WriteStep), t / WriteStep),
                   Bezier(Bezier(y2, y3, t / WriteStep), Bezier(y3, y4, t / WriteStep), t / WriteStep), t / WriteStep)
        te.goto(x, y)
    te.penup()


def Moveto(x, y):
    debug(f'Moveto({x}, {y})')
    te.penup()
    te.goto(-Width / 2 + x, Height / 2 - y)
    te.pendown()


def Moveto_r(dx, dy):
    debug(f'Moveto_r({dx}, {dy})')
    te.penup()
    te.goto(te.xcor() + dx, te.ycor() - dy)
    te.pendown()


def line(x1, y1, x2, y2):
    debug(f'line({x1}, {y1}, {x2}, {y2})')
    te.penup()
    te.goto(-Width / 2 + x1, Height / 2 - y1)
    te.pendown()
    te.goto(-Width / 2 + x2, Height / 2 - y2)
    te.penup()


def Lineto_r(dx, dy):
    debug(f'Lineto_r({dx}, {dy})')
    te.pendown()
    te.goto(te.xcor() + dx, te.ycor() - dy)
    te.penup()


def Lineto(x, y):
    debug(f'Lineto({x}, {y})')
    te.pendown()
    te.goto(-Width / 2 + x, Height / 2 - y)
    te.penup()


def Curveto(x1, y1, x2, y2, x, y):
    debug(f'Curveto({x1}, {y1}, {x2}, {y2}, {x}, {y})')
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, x1, y1, x2, y2, x, y)
    global Xh
    global Yh
    Xh = x + x - x2
    Yh = y + y - y2


def Curveto_r(x1, y1, x2, y2, x, y):
    debug(f'Curveto_r({x1}, {y1}, {x2}, {y2}, {x}, {y})')
    te.penup()
    X_now = te.xcor() + Width / 2
    Y_now = Height / 2 - te.ycor()
    Bezier_3(X_now, Y_now, X_now + x1, Y_now + y1,
             X_now + x2, Y_now + y2, X_now + x, Y_now + y)
    global Xh
    global Yh
    Xh = x - x2
    Yh = y - y2


def SymmetricCurveto(x2, y2, x, y):
    debug(f'SymmetricCurveto({x2}, {y2}, {x}, {y})')
    Curveto(Xh, Yh, x2, y2, x, y)


def SymmetricCurveto_r(x2, y2, x, y):
    debug(f'SymmetricCurveto({x2}, {y2}, {x}, {y})')
    Curveto_r(Xh, Yh, x2, y2, x, y)


def transform(w_attr):
    funcs = w_attr.split(' ')
    for func in funcs:
        func_name = func[0: func.find('(')]
        if func_name == 'scale':
            global scale
            scale = (float(func[func.find('(') + 1: -1].split(',')[0]),
                     -float(func[func.find('(') + 1: -1].split(',')[1]))


def number(s):
    try:
        return float(s)
    except ValueError as err:
        return None


def readPathAttrD(w_attr):
    ulist = re.sub('  *', ' ', re.sub('([a-zA-Z])', ' \\1 ', w_attr.replace('-', ' -').replace(',', ' '))).strip().split(' ')
    for i in ulist:
        if i.isalpha(): # Command
            yield i
        else: # Number, hopefully
            num = number(i)
            if num is None:
                raise ValueError(f'Unsupported token: {i}')
            yield num


def drawSVG(filename, w_color):
    global first
    SVGFile = open(filename, 'r')
    SVG = BeautifulSoup(SVGFile.read(), 'lxml')
    Height = float(SVG.svg.attrs['height'][0: -2])
    Width = float(SVG.svg.attrs['width'][0: -2])
    transform(SVG.g.attrs['transform'])
    if first:
        te.setup(height=Height, width=Width)
        te.setworldcoordinates(-Width / 2, 300, Width -
                               Width / 2, -Height + 300)
        first = False
    te.tracer(100)
    te.pensize(1)
    te.speed(Speed)
    te.penup()
    te.color(w_color)

    for i in SVG.find_all('path'):
        attr = i.attrs['d'].replace('\n', ' ')
        f = readPathAttrD(attr)
        lastI = ''
        for i in f:
            if i == 'M':
                te.end_fill()
                Moveto(next(f) * scale[0], next(f) * scale[1])
                te.begin_fill()
            elif i == 'm':
                te.end_fill()
                Moveto_r(next(f) * scale[0], next(f) * scale[1])
                te.begin_fill()
            elif i == 'C':
                Curveto(next(f) * scale[0], next(f) * scale[1],
                        next(f) * scale[0], next(f) * scale[1],
                        next(f) * scale[0], next(f) * scale[1])
                lastI = i
            elif i == 'c':
                Curveto_r(next(f) * scale[0], next(f) * scale[1],
                          next(f) * scale[0], next(f) * scale[1],
                          next(f) * scale[0], next(f) * scale[1])
                lastI = i
            elif i == 'S':
                SymmetricCurveto(next(f) * scale[0], next(f) * scale[1],
                                 next(f) * scale[0], next(f) * scale[1])
                lastI = i
            elif i == 's':
                SymmetricCurveto_r(next(f) * scale[0], next(f) * scale[1],
                                   next(f) * scale[0], next(f) * scale[1])
                lastI = i
            elif i == 'L':
                Lineto(next(f) * scale[0], next(f) * scale[1])
            elif i == 'l':
                Lineto_r(next(f) * scale[0], next(f) * scale[1])
                lastI = i
            elif i == 'H':
                Lineto(next(f) * scale[0], te.ycor())
                lastI = i
            elif i == 'h':
                Lineto_r(next(f) * scale[0], 0)
                lastI = i
            elif i == 'V':
                Lineto(te.xcor(), next(f) * scale[1])
                lastI = i
            elif i == 'v':
                Lineto_r(0, next(f) * scale[1])
                lastI = i
            elif number(i) is None:
                raise ValueError(f'Unsupported command: {i}')
            elif lastI == 'C':
                Curveto(i * scale[0], next(f) * scale[1],
                        next(f) * scale[0], next(f) * scale[1],
                        next(f) * scale[0], next(f) * scale[1])
            elif lastI == 'c':
                Curveto_r(i * scale[0], next(f) * scale[1],
                          next(f) * scale[0], next(f) * scale[1],
                          next(f) * scale[0], next(f) * scale[1])
            elif lastI == 'S':
                SymmetricCurveto(i * scale[0], next(f) * scale[1],
                                 next(f) * scale[0], next(f) * scale[1])
            elif lastI == 's':
                SymmetricCurveto_r(i * scale[0], next(f) * scale[1],
                                   next(f) * scale[0], next(f) * scale[1])
            elif lastI == 'L':
                Lineto(i * scale[0], next(f) * scale[1])
            elif lastI == 'l':
                Lineto_r(i * scale[0], next(f) * scale[1])
            elif lastI == 'H':
                Lineto(i * scale[0], te.ycor())
            elif lastI == 'h':
                Lineto_r(i * scale[0], 0)
            elif lastI == 'V':
                Lineto(te.xcor(), i * scale[1])
            elif lastI == 'v':
                Lineto_r(0, i * scale[1])
            # TODO:
            # - Z/z to close the current path.
            # - Q/q for quadratic bezier curve.
            else:
                raise ValueError(f'Unexpected state: {lastI}')
    te.penup()
    te.hideturtle()
    te.update()
    SVGFile.close()
