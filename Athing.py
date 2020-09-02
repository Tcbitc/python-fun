import turtle
t=turtle.Turtle()
t.hideturtle()
x=1

def thing():
  t.tracer(0,0)
  t.dot(x)
  t.color('white')
  t.dot(x-1)
  t.color('black')
  t.update()

for athing in range(300):
  thing()
  x=x+1