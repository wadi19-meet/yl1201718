from turtle import *
import random
import time
from ball import Ball
colormode(255)
tracer(0)
ht()
running = True
sleep = 0.0077
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2
NUMBER_OF_BALL = 5
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS =100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5


MY_BALL = Ball(5 ,10 ,2 ,3 ,10)

Balls = []

for i in range (NUMBER_OF_BALL):

	x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) ,int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS,)
	

	ball1 = Ball(x, y, dx, dy, radius)
	Balls.append(ball1)

def move_all_balls():
	for i in Balls:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def check_collision(ball1,ball2):
	if ball1 == ball2:
		return False
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.ycor()
	y2 = ball1.ycor()	
	d=math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

	if d <= (ball1.radius + ball2.radius):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball1 in Balls:
		for ball2 in Balls:
			if check_collision(ball1, ball2):
				
				x = random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y = random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				dx = random.randint(MAXIMUM_BALL_DX, MINIMUM_BALL_DX)
				dy = random.randint(MAXIMUM_BALL_DY, MINIMUM_BALL_DX)
				radius = random.randint(MAXIMUM_BALL_RADIUS, MINIMUM_BALL_RADIUS)

				while (dx == 0):
					dx = random.randint()

				while (dy == 0):
					dy = random.randint()

				if ball1.radius < ball2.radius:
					ball1.goto(x,y)
					ball1.dx = dx
					ball1.dy = dy
					ball1.radius = radius
					ball2.radius = ball2.radius +1
					ball1.shapesize(ball1.radius/10)
					ball2.shapesize(ball2.radius/10)

				if ball1.radius > ball2.radius:
					
					ball2.goto(x,y)
					ball2.dx = dx
					ball2.dy = dy
					ball2.radius = radius
					ball1.radius = ball1.radius +1
					ball2.shapesize(ball2.radius/10)
					ball1.shapesize(ball1.radius/10)


def check_myball_colllision ():
	for i in Balls :
		if check_collision (MY_BALL,i) == True :
			x = random.randint(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS , SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
			y = random.randint(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
			dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DY,)
			radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS,)

			while (dx == 0):
					dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

			while (dy == 0):
					dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)

			if MY_BALL.radius < i.radius :
				return False
			elif MY_BALL.radius > i.radius:
					
# ##############################################################
#### i have to continue this code 
######

######################################################3

				# i.goto(x,y)
				# i.dx = dx
				# i.dy = dy
				# i.radius = radius
				# MY_BALL.radius = MY_BALL.radius +1
				# i.shapesize(i.radius/10)
				# MY_BALL.shapesize(MY_BALL.radius/10)




def move_around(event):
	mouseX = event.x - SCREEN_WIDTH
	mouseY = SCREEN_HEIGHT - event.y

	turtle.getcanvas().bind("<motion>", movearound)


	ballX = MY_BALL.x
	ballY = MY_BALL.y

	distanceX = mouseX - ballx
	distanceY = mouseY - ballY 

	MY_BALL.dyv = (distanceX / (MY_BALL.radius * ACCELARATION_OF_BALL)) * MY_BALL.dx
	MY_BALL.dyv = (distanceY / (MY_BALL.radius * ACCELARATION_OF_BALL)) * MY_BALL.dy

	MY_BALL>move(SCREEN_WIDTH, SCREEN_HEIGHT)

	print(int(MY_BALL.radius))


def move_my_ball():
	global RUNNING
	MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)
	if check_myball_colllision() == False:
		RUNNING = False

	check_all_balls_collision()




mainloop()
