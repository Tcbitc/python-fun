pic=int()
r=int(pic*2)
if pic in range(1,101):
	from math import *
	import turtle
	t=turtle.Turtle()
	if int(pic)+50 in range(131,151):
		for shucks in range(pic):
			for creepers in range(pic):
				x=r
				y=pic
				t.goto(x,y)
			for stutters in range(pic):
				x=pic
				y=r
				t.goto(x,y)
	if int(pic)+30 in range(111,131):
		x=1
		y=1
		for bob in range(int(pic/2)):
			for doodles in range(pic):
				x=x+1
				y=y-1
				t.goto(x,y)
			for derping in range(pic):
				x=x+1
				y=y+1
				t.goto(x,y)
		for thegorontribe in range(pic):
			for gorons in range(pic):
				x=x-1
				y=y+1
				t.goto(x,y)
			for madness in range(pic):
				x=x-1
				y=y-1
				t.goto(x,y)
	if int(pic)+10 in range(11,111):
		d=0
		for me in range(30):
			t.left(100)
			print(d+9)
			d=d+9