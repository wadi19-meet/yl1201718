#problem1
print("wadi "*100)
#problem2
number1=2
print(number1)
number2=1
print(number2)
#problem3
l = [1,2,3]
sum = 0
for i in range(len(l)):
	sum = sum + l[i]
print(sum)
##problem 4
import turtle
#begin the fill
turtle.begin_fill()
turtle.goto(0,100)
turtle.goto(100,100)
turtle.goto(100,0)
turtle.goto(0,0)
turtle.end_fill()
#end the fill
turtle.pensize(20)
turtle.penup()
turtle.goto(200,200)
turtle.pendown()
radius=50
turtle.circle(radius)
turtle.penup()
turtle.goto(250,150)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(300,200)
turtle.pendown()
turtle.circle(radius)
turtle.penup()
turtle.goto(350,150)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(400,200)
turtle.pendown()
turtle.circle(radius)
turtle.mainloop()