from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self,radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
ball1 = Ball(10, "black", 5)
ball2 = Ball(26, "blue", 3)

def check_collision(ball1,ball2):
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.ycor()
	y2 = ball1.ycor()	
	d=math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))




	if d <= (ball1.radius + ball2.radius):
		print("it collides")
	else:
		print("it is not collided")

ball1.goto(45,50)
ball2.goto(50,50)
check_collision(ball1,ball2)
mainloop()		