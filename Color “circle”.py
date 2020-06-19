from math import *
#from colorsys import hsv_to_rgb
import turtle

def colorise(h, s, v):
	if s==0.0:
		return v, v, v
	i=int(h*6.0)
	f=(h*6.0) - i
	p=v*(1.0 - s)
	q=v*(1.0 - s*f)
	t=v*(1.0 - s*(1.0-f))
	v=int(255*v)
	p=int(255*p)
	q=int(255*q)
	t=int(255*t)
	i=i%6
	if i == 0:
		return v, t, p
	if i == 1:
		return q, v, p
	if i == 2:
		return p, v, t
	if i == 3:
		return p, q, v
	if i == 4:
		return t, p, v
	if i == 5:
		return v, p, q
	raise

def plot(turt, mn, mx, fx, fy, steps=200):
	for it in range(0, steps+1):
		t = (mx-mn) * it / steps + mn
		x = fx(t)
		y = fy(t)
		progress = it / steps
		h = progress+0.2
		if h > 1:
			h-=1
		s = 1.0
		dist=abs(progress-0.5)
		v = dist+0.5
		print(colorise(h,s,v))
		turt.color(colorise(h, s, v))
		turt.goto(x, y)
		turt.pendown()

turt = turtle.Turtle()
turt.penup()
turt.speed(1000)
turtle.colormode(255)

def fx(t): return 5 * (4*(1-t)+1*t) * sin(3*6.2832*t)
def fy(t): return 5 * (4*(1-t)+1*t) * cos(3*6.2832*t)
plot(turt, 1, 10, fx, fy)

turt.speed(0.2)
turt.left(90)
turt.speed(5000)
turt.penup()

turt.delay(1500)
turt.forward(390)
