from turtle import *
xavier = Turtle()
xavier.speed(2)
def drawTriangle():
	for x in range(20):
		xavier.forward(30)
		xavier.left(30)
drawTriangle()
mainloop()
