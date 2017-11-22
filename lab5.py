# ex1
import random
from turtle import *
colormode(255)
# class Square(Turtle):	
# 	def __init__(self, size):
# 		Turtle.__init__(self)
# 		self.shapesize(size)		
# 		self.shape("square")

# 	def random_color(self):
# 		r = random.randint(0,256)
# 		g = random.randint(0,256)
# 		b = random.randint(0,256)
# 		self.color((r,g,b))
# square1 = Square(20)
# square1.random_color()

class Rectangle(Turtle):	
	def __init__(self, size , width, height):
		Turtle.__init__(self)
		self.shapesize(size)		
		self.width(width)
		self.height(height)
		self.shape("rectangle")
	def random_color(self):
		r = random.randint(0,256)
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color((r,g,b))
rectangle1 = Rectangle(10,5,6)
rectangle1.random_color()