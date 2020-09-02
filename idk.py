from turtle import *

screen = Screen()
screenMinX = -screen.window_width()
screenMinY = -screen.window_height()
screenMaxX = screen.window_width()
screenMaxY = screen.window_height()

screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)

brush_turtle = Turtle()
brush_turtle.goto(0, 0)
brush_turtle.speed(10)

def on_screen_click(x, y):
  if y < screenMaxY - 40:
    brush_turtle.goto(x, y)
    
screen.onclick(on_screen_click)
  

class ColorPicker(Turtle):
  def __init__(self, color="red",num=0):
    Turtle.__init__(self)
    self.num = num
    self.color_name = color
    self.speed(0)
    self.shape("circle")
    self.color("black", color)
    self.penup()
    
    self.onclick(lambda x, y: self.handle_click(x, y))

  def draw(self):
    self.setx(screenMinX+110+self.num*30)
    self.sety(screenMaxY - 20)
    
  def handle_click(self, x, y):
    if self.color_name == "#F9F9F9":
      brush_turtle.penup()
      brush_turtle.color("black")
    else:
      brush_turtle.pendown()
      brush_turtle.color(self.color_name)
    