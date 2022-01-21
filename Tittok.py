from turtle import *
import time as tm

bgcolor('black')
width(20)
colors = ['#db0f3e', '#50ebe7', '#ffffff']
position = [(0, 0),(-5, 13),(-5, 5)]
for (x,y), col in zip(position, colors):
	up()
	goto(x,y)
	down()
	color(col)
	left(180)
	circle(50, 270)
	forward(120)
	left(180)
	circle(50,90)
	
tm.sleep(20)
