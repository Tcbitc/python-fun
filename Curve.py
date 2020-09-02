import random
rando = random.randint(1,100)

size = rando


from turtle import *
t = Turtle()
t.hideturtle()
t.color('white')
t.dot(500)
t.color('black')

ui_turtle = Turtle(1)
ui_turtle.hideturtle()

v=0
w=0
x=0
y=size
z=1

text= w
text1= 'The size is'
text2= 'The number of spins will be'
text3= 'Spins:', z
def text4(w):
  for ww in range(9):
    text= w
    ui_turtle.write(text, align="left", font=("Courier", 130, "bold"))
    w=w+1

def no(v):
  for vv in range(9):
    txt= v
    ui_turtle.write(txt, align="left", font=("Courier", 30, "bold"))
    v=v+1

print text1,size
print(' ')
print text2,rando*4

for colorchanger in range(rando*2):
  for circle in range(2):
    for _ in range(size):
      t.tracer(0,0)
      t.goto(x,y)
      t.goto(0,0)
      t.update()
      x=x+1
      y=y-1

    for a in range(size):
      t.tracer(0,0)
      t.goto(x,y)
      t.goto(0,0)
      t.update()
      x=x-1
      y=y-1

    for b in range(size):
      t.tracer(0,0)
      t.goto(x,y)
      t.goto(0,0)
      t.update()
      x=x-1
      y=y+1

    for c in range(size):
      t.tracer(0,0)
      t.goto(x,y)
      t.goto(0,0)
      t.update()
      x=x+1
      y=y+1

    ui_turtle.tracer(0,0)
    ui_turtle.penup()

    ui_turtle.color('white')
    ui_turtle.goto(23,130)
    text4(w)
    ui_turtle.color('black')

    ui_turtle.goto(-100,150)
    ui_turtle.write(text3, align="left", font=("Courier", 25, "bold"))

    ui_turtle.color('white')
    ui_turtle.goto(15,140)
    no(v)
    ui_turtle.color('black')

    ui_turtle.pendown()
    ui_turtle.update()
    t.color('white')
    z=z+1
    text3='Spins:',z
  t.color('black')
  
  