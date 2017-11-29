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

# class Rectangle(Turtle):	
# 	def __init__(self,hight,weidth):
# 		Turtle.__init__(self)		
# 		self.pd()
# 		register_shape("rec",((0,0),(hight,0),(hight,weidth),(0,weidth)))
# 		self.shape("rec")

# 	def random_color(self):
# 		r = random.randint(0,256)
# 		g = random.randint(0,256)
# 		b = random.randint(0,256)
# 		self.color((r,g,b))
# rectangle2 = Rectangle(50,100)
# rectangle2.random_color()


# class Hexagon(Turtle):
# 	def __init__(self,size,speed):
# 		Turtle.__init__(self)

# 		self.ht()
# 		self.pd()

# 		begin_poly()
		
# 		ht()
# 		goto(50,0)
# 		goto(75,25)
# 		goto(50,50)
# 		goto(25,50)
# 		goto(0,25)
# 		goto(25,0)
# 		st()
# 		end_poly()
# 		hexagon1=get_poly()
# 		register_shape("hexagon",hexagon1)
# 		self.shape("hexagon")
# 		self.st()
# 		self.setheading(90)
# 	def random_color(self):
# 		r = random.randint(0,256)
# 		g = random.randint(0,256)
# 		b = random.randint(0,256)
# 		self.color((r,g,b))

# hexagon2 = Hexagon(20,7)

# hexagon2.random_color()

class Polygon(Turtle):
	def __init__(self,lines):
		Turtle.__init__(self)
		self.lines=lines

		begin_poly()
		for i in range (lines):
			self.forward(50)
			self.right(360/lines)
		end_poly()
		
		w=get_poly()	
polygon1=Polygon(6)
mainloop()	

mainloop()