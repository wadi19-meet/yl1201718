from turtle import *
import random
import time
setup(1280,720)
bgpic("11.gif")
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2
Running = True
sleep = 0.0077
tracer = 0
# delay(5)
MINIMUM_BALL_DX = -3
MAXIMUM_BALL_DX = 3
MINIMUM_BALL_DY = -3
MAXIMUM_BALL_DY = 3

Balls = []
Ball1_pos = []
class Ball(Turtle):
	def __init__(self ,x , y, dx, dy, radius,color):

		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
				
		self.dx = dx
		self.dy = dy
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color ("yellow")
	def move(self , width, height):
		current_x = self.xcor()
		new_x = current_x + self.dx
		current_y = self.ycor()
		new_y = current_y + self.dy
		left_side = new_x - self.radius
		Right_side = new_x + self.radius
		top_side = new_y + self.radius
		bottom_side = new_y -self.radius
		self.goto(new_x,new_y)
		if top_side >= height:
			self.dy = -self.dy

		elif bottom_side <= -height:
			self.dy = -self.dy

		elif Right_side >= width:
			self.dx = -self.dx

		elif left_side <= -width:
			self.dx = -self.dx
dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DY)
		

Ball1 = Ball(0,0,dx,0.7,15,"color")

Balls.append(Ball1)
Ball1_pos.append(Ball1.pos())
def move_ball():
	for i in Balls:
		i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

class Block(Turtle):
	def __init__(self,x ,y ,dx ,dy, width, height,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
				
		self.dx = dx
		self.dy = dy
		self.shape("square")
		self.shapesize(width, height)
		self.color((r,g,b))

		

Block1 = Block(SCREEN_WIDTH-25,0,0,0,1,6,"red")
Block2 = Block(-SCREEN_WIDTH+25,0,0,0,1,6,"green")

UP_ARROW = "Up"
DOWN_ARROW = "Down"

Block1.right(90)
Block2.right(90)
def b1_up():
	
	Block1.forward(-5)
def b1_down():
	Block1.forward(5)
def b2_up():
	Block2.forward(-5)
def b2_down():
	Block2.forward(5)		

onkey(b1_up,"Up")
onkey(b1_down,"Down")
onkey(b2_up,"w")
onkey(b2_down,"s")

listen()

# def check_collision():
# 	if Ball1.radius() == Block1.width():
# 		Ball1_pos[Ball1.right(180)]

while Running:
	move_ball()


mainloop()