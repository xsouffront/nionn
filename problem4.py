from turtle import *
xavier = Turtle()
xavier.speed(2)
def drawTriangle():
	for x in range(20):
		xavier.forward(30)
		xavier.left(30)
drawTriangle()
drawTriangle(5)
drawTriangle(10)
drawTriangle(15)
drawTriangle(20)
drawTriangle(25)
drawTriangle(30)
drawTriangle(35)
drawTriangle(40)

mainloop()