from turtle import *
xavier = Turtle()
xavier.speed(2)
def drawTriangle():
	for x in range(3):
		xavier.forward(100)
		xavier.left(120)
def drawWheel():
	for x in range(12):
		drawTriangle()
		xavier.left(30)
drawWheel()
mainloop()
