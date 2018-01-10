import turtle
def ex1():
	length=100
	angle=145

	for i in range (5):
		turtle.forward(length)
		turtle.right(angle)
	

def ex2():
	turtle.register_shape("myname", ((50,0),(50,50),(25,75),(0,50),(0,0)))

	turtle.shape("myname")
	turtle.getshapes()
	turtle.begin_fill()
	turtle.forward(50)
	turtle.right(90)
	turtle.forward(50)
	turtle.right(30)
	turtle.forward(50)
	turtle.right(120)
	turtle.forward(50)
	turtle.right(30)
	turtle.forward(50)

	turtle.end_fill()

def  ex4():
	turtle.speed(1000)
	for i in range(360):
		turtle.penup()
		turtle.home()
		turtle.pendown()
		turtle.right(i)
		turtle.forward(200)
		turtle.right(45)
		turtle.forward(100)
		turtle.right(90)
		turtle.forward(50)
	
ex4()










turtle.mainloop()

