from turtle import *
t = Turtle()
t.hideturtle()
st = Turtle()
st.hideturtle()
s = Screen()

coordl = -s.window_width()*(1+(1/500))
coordb = -s.window_height()*(1+(1/500))
coordr = s.window_width()*(1+(1/500))
coordt = s.window_height()*(1+(1/500))
s.setworldcoordinates(coordl,coordb,coordr,coordt)
import random
r = random.randint(1,10000)

n = 0
tx = -245

s.tracer(0,0)
st.penup()
for screen in range(10):
  st.goto(tx,220)
  st.write(n, align = 'left', font = ('Courier', 40, 'bold'))
  n = n+1
  tx = tx+50
st.goto(-245,205)
st.pendown()
st.goto(245,205)
st.goto(245,155)
st.goto(-245,155)
st.goto(-245,205)
st.penup()
st.goto(-40,160)
st.write("ok", align = 'left', font = ("Courier", 40, 'bold'))
s.update()

def numbers(x,y):
  if (y in range(220,260)):
    if (x in range(-246,-204)):
      guss = 0
    if (x in range(-196,-154)):
      guss = 1
    if (x in range(-146,-104)):
      guss = 2
    if (x in range(-96,-54)):
      guss = 3
    if (x in range(-46,-4)):
      guss = 4
    if (x in range(4,46)):
      guss = 5
    if (x in range(54,96)):
      guss = 6
    if (x in range(104,146)):
      guss = 7
    if (x in range(154,196)):
      guss = 8
    if (x in range(204,246)):
      guss = 9

      aaa = 10
      bbb = 10
      ccc = 10
      ddd = 10
      eee = 10
    if (x in range(-246,246)):
      if ((eee not in range(0,10)) and (ddd in range(0,10))):
        eee = guss
      if ((ddd not in range(0,10)) and (ccc in range(0,10))):
        ddd = guss
      if ((ccc not in range(0,10)) and (bbb in range(0,10))):
        ccc = guss
      if ((bbb not in range(0,10)) and (aaa in range(0,10))):
        bbb = guss
      if (aaa not in range(0,10)):
        aaa = guss

def ok(x,y):
  aaa = 10
  bbb = 10
  ccc = 10
  ddd = 10
  eee = 10
  trueguss = 0

  if (
    x in range(-246,246)
    and y in range(155,205)
  ):
    if aaa in range(0,10):
      aaa = aaa*1
      trueguss = aaa

    if bbb in range(0,10):
      bbb = bbb*1
      aaa = aaa*10
      trueguss = aaa+bbb

    if ccc in range(0,10):
      ccc = ccc*1
      bbb = bbb*10
      aaa = aaa*100
      trueguss = aaa+bbb+ccc

    if ddd in range(0,10):
      ddd = ddd*1
      ccc = ccc*10
      bbb = bbb*100
      aaa = aaa*1000
      trueguss = aaa+bbb+ccc+ddd

    if eee in range(0,10):
      eee = eee*1
      ddd = ddd*10
      ccc = ccc*100
      bbb = bbb*1000
      aaa = aaa*10000
      trueguss = aaa+bbb+ccc+ddd+eee

      inpu = "input:"
      win = "You win!"
      equl = "="
      smlr = "< ?"
      bgr = "> ?"
    print (inpu, trueguss)
    if trueguss<r:
      print(trueguss, smlr)
    if trueguss>r:
      print(trueguss, bgr)
    if trueguss==r:
      print(win)
      print(trueguss, equl, r)

s.onclick(ok)

