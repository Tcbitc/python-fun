import turtle
t=turtle.Turtle()
t.speed(100)
t.color("grey")
def ocean():
	for _ in range(24):
		t.forward(8) or t.left(19)
		t.forward(2) or t.left(3) or t.forward(3) or t.left(148) or t.forward(3)
		t.right(5) or t.forward(4) or t.right(125) or t.forward(13) or t.right(25)
for x in range(6):
	ocean() or t.penup() or t.right(60) or t.forward(105) or t.pendown()
t.penup() or t.forward(200)