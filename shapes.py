import turtle

shapes =  ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

i = 0
for shape in shapes:
    t = turtle.Turtle(shape)
    t.forward(i)
    i += 50

print('DONE')

input("Press enter")
