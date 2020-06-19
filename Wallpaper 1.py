a=5
b=10
c=15
d=20
import turtle
t=turtle.Turtle()
t.speed(1000)
t.penup()
t.left(90)
t.forward(150)
t.left(90)
t.forward(150)
t.right(90)
t.pendown()

def drawcircle():
	for wildlife in range(36):
		t.forward(1)
		t.left(a)
		t.forward(1)
		t.right(b)
		t.forward(1)
		t.left(c)
		t.forward(1)
		t.right(d)
		t.forward(1)

for theloveofgod in range(4):
	for goodnesssake in range(3):
		drawcircle()
		t.right(180)
		drawcircle()
		t.penup()
		t.forward(57)
		t.pendown()
		drawcircle()
		t.right(180)
		drawcircle()
		t.penup()
		t.right(180)
		t.forward(57)
		t.pendown()
		t.right(180)
	t.penup()
	t.forward(57)
	t.left(90)
	t.pendown()
t.penup()
t.forward(100)
s=turtle.Turtle(2)
s.forward(100)
s.right(180)
s.forward(201)
s.right(180)
s.forward(100)
s.left(90)
s.forward(100)
s.right(180)
s.forward(300)