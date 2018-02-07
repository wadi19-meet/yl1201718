from turtle import *
import random
import time
from ball import Ball

import math
colormode(255)
tracer(0)
ht()
speed(1)
RUNNING = True
sleep = 0.0077
setup (3000,3000)

# pu()
# score = clone()  
# score = 0

# score.goto(600,300)
# score.color ("red")




MY_BALL = Ball(0 ,0 ,0 ,0 ,50)
SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2
# NUMBER_OF_FOOD = 
NUMBER_OF_BALL = 3
MINIMUM_BALL_RADIUS = int(MY_BALL.radius*0.75)
MAXIMUM_BALL_RADIUS = int(MY_BALL.radius*1.5)
MINIMUM_BALL_DX = -2
MAXIMUM_BALL_DX = 2
MINIMUM_BALL_DY = -2
MAXIMUM_BALL_DY = 2
MIN_FOOD_RADIUS = 3
MAX_FOOD_RADIUS = 9
MAX_FOOD_NUMBER = 45
SCORE_SIZE = 15
SCORE_TYPE = "bold"
SCORE_COLOR = "red"

FOOD = []
Balls = []
for i in range (NUMBER_OF_BALL):

	x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) ,int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))

	while MY_BALL.distance(x,y) < MY_BALL.radius + x:		
		x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
		y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) ,int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))

	dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DY)
	radius = random.randint(MINIMUM_BALL_RADIUS, MAXIMUM_BALL_RADIUS)
	

	ball1 = Ball(x, y, dx, dy, radius)
	Balls.append(ball1)

scorewrite = clone()
scorewrite.pu()
scorewrite.goto(SCREEN_WIDTH -25, SCREEN_HEIGHT -15)
scorewrite.color(SCORE_COLOR)

ht()



def write_score():
	global scorewrite
	scorevalue = int(MY_BALL.radius)
	scorewrite.goto(SCREEN_WIDTH - 160, SCREEN_HEIGHT-30)
	scorewrite.clear()
	scorewrite.pencolor(SCORE_COLOR)
	scorewrite.write("Score: " + str(scorevalue), False, "left", font = ("Arial", SCORE_SIZE, SCORE_TYPE))







def food ():
	creatfood = random.uniform(0,0.19)

	if creatfood <0.2 and len(FOOD) < MAX_FOOD_NUMBER:
		x = random.uniform(-SCREEN_WIDTH + MAX_FOOD_RADIUS, SCREEN_WIDTH - MAX_FOOD_RADIUS)
		y = random.uniform(-SCREEN_HEIGHT + MAX_FOOD_RADIUS, SCREEN_HEIGHT - MAX_FOOD_RADIUS)
		radius = random.uniform(MIN_FOOD_RADIUS, MAX_FOOD_RADIUS)


		food = Ball(x,y,0,0,radius)
		FOOD.append(food)




def move_all_balls():
	for i in Balls:
		i.move(SCREEN_WIDTH, SCREEN_HEIGHT)

def check_collision(ball1,ball2):
	if ball1 == ball2:
		return False
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.ycor()
	y2 = ball2.ycor()	
	d=math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

	if d <= (ball1.radius + ball2.radius):
		return True
	else:
		return False

def check_all_balls_collision():
	for ball1 in Balls:
		for ball2 in Balls:
			if check_collision(ball1, ball2):
				
				x = random.randint(int(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				y = random.randint(int(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) , int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				while MY_BALL.distance(x,y) < MY_BALL.radius + ball2.radius:
					x = random.randint(int(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
					y = random.randint(int(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) , int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DY)
				radius = random.randint(int(MY_BALL.radius*0.75), int(MY_BALL.radius*1.5))
				r = random.randint(0,255)
				g = random.randint(0,255)
				b = random.randint(0,255)
				new_color = (r, g, b)
				# make new color r = 
				# new_color = (r,g,b)
				while (dx == 0):
					dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

				while (dy == 0):
					dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DY)

				# if ball1.radius <= SCREEN_WIDTH:
				# 	ball1.goto(x,y)
				# 	ball1.dx = dx
				# 	ball1.dy = dy
				# 	ball1.radius = radius
				# 	ball1.shapesize(ball1.radius/10)
				# elif ball1.radius >= -SCREEN_WIDTH:
				# 	ball1.goto(x,y)
				# 	ball1.dx = dx
				# 	ball1.dy = dy
				# 	ball1.radius = radius
				# 	ball1.shapesize(ball1.radius/10)
				# elif ball1.radius <= SCREEN_HEIGHT:
				# 	ball1.dx = dx
				# 	ball1.dy = dy
				# 	ball1.radius = radius
				# 	ball1.shapesize(ball1.radius/10)
				# elif ball1.radius >= -SCREEN_HEIGHT:
				# 	ball1.dx = dx
				# 	ball1.dy = dy
				# 	ball1.radius = radius
				# 	ball1.shapesize(ball1.radius/10)





				if ball1.radius < ball2.radius:
					ball1.goto(x,y)
					ball1.dx = dx
					ball1.dy = dy
					ball1.radius = radius
					ball2.radius = ball2.radius +1
					ball1.shapesize(ball1.radius/10)
					ball2.shapesize(ball2.radius/10)
					ball1.color((r,g,b))
				if ball1.radius > ball2.radius:
					
					ball2.goto(x,y)
					ball2.dx = dx
					ball2.dy = dy
					ball2.radius = radius
					ball1.radius = ball1.radius +1
					ball2.shapesize(ball2.radius/10)
					ball1.shapesize(ball1.radius/10)
					ball2.color((r,g,b))




def check_myball_colllision ():
	for i in Balls :
		if check_collision (MY_BALL,i) == True :
			x = random.randint(int(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
			y = random.randint(int(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) , int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))

			while MY_BALL.distance(x,y) < MY_BALL.radius + i.radius:
				x = random.randint(int(- SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				y = random.randint(int(- SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) , int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
			dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
			dy = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DY)
			radius = random.randint(int(MY_BALL.radius*0.75), int(MY_BALL.radius*1.5))
			r = random.randint(0,255)
			g = random.randint(0,255)
			b = random.randint(0,255)
			new_color = (r, g, b)

			while (dx == 0):
					dx = random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)

			while (dy == 0):
					dy = random.randint(MINIMUM_BALL_DY, MAXIMUM_BALL_DY)

			if MY_BALL.radius > i.radius :
				i.goto(x,y)
				i.dx = dx
				i.dy = dy
				i.radius = radius
				MY_BALL.radius = MY_BALL.radius + i.radius / 10
				i.shapesize(i.radius/10)
				MY_BALL.shapesize(MY_BALL.radius/10)
				i.color((r,g,b))
			else:
				ht()
				goto(-180,0)
				pencolor(SCORE_COLOR)
				write("YOU LOST", False, "left", font = ("Arial",int(SCORE_SIZE*3), SCORE_TYPE) )
				time.sleep(2)
				quit()
				return False

	return True			

def eat_food():
	index = 0
	for food in FOOD:
		colliding = check_collision(MY_BALL,food) 
		if colliding == True:
			MY_BALL.radius += food.radius / 8
			MY_BALL.shapesize(MY_BALL.radius / 10)

			x = random.uniform(-SCREEN_WIDTH + MAX_FOOD_RADIUS, SCREEN_WIDTH - MAX_FOOD_RADIUS)
			y = random.uniform(-SCREEN_HEIGHT + MAX_FOOD_RADIUS, SCREEN_HEIGHT - MAX_FOOD_RADIUS)
			radius = random.uniform(MIN_FOOD_RADIUS, MAX_FOOD_RADIUS)

			food.ht()

			FOOD.pop(index)

		index += 1	



def move_around(event):

	mouseX = event.x - SCREEN_WIDTH
	mouseY = SCREEN_HEIGHT - event.y

	MY_BALL.goto(mouseX, mouseY)

getcanvas().bind("<Motion>", move_around)
getscreen().listen()



while RUNNING:
	if SCREEN_WIDTH != getcanvas().winfo_width()/2:
		SCREEN_WIDTH = getcanvas().winfo_width()/2

	elif SCREEN_HEIGHT != getcanvas().winfo_height()/2:
		SCREEN_HEIGHT = getcanvas().winfo_height()/2

	
	
	write_score()
	food()
	eat_food()
	move_all_balls()
	check_all_balls_collision()
	MY_BALL.move(SCREEN_WIDTH, SCREEN_HEIGHT)

	
	if check_myball_colllision() == False:
		RUNNING = False

	else:
		RUNNING = True

	


	if MY_BALL.radius >= 250:
		ht()
		goto(-157,0)
		pencolor(SCORE_COLOR)
		write("YOU WON", False, "left", font = ("Arial",int(SCORE_SIZE*3), SCORE_TYPE) )
		time.sleep(2)
		quit()
	

	getscreen().update()
	time.sleep(sleep)
mainloop()
