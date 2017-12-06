from turtle import *
import random
import math
class Ball(Turtle):
	def __init__(self, radius, color, speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
r = 10
R = 20
ball1 = Ball(int(r),"red",5)

ball2 = Ball(int(R),"blue",10)

# print(Ball[0][1])	
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



ball1.goto(0,0)

ball2.goto(100,0)

check_collision(ball1,ball2)
mainloop()
