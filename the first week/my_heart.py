from turtle import *

setup(600,400,200,0)
bgcolor("black")

def set_pos(x,rad):
    penup()
    setpos(x*rad*5,-80)
    pendown()

def draw_heart(rad):
    color('pink',"gold")
    begin_fill()
    left(135)
    forward(rad*2)
    circle(-rad,180)
    left(90)
    circle(-rad,180)
    forward(rad*2)
    end_fill()

def main():
	#定义心的大小
	rad = 10
	for i in range(3):
		set_pos(i,rad)
		draw_heart(rad)
		left(135)
         
main()
hideturtle()
done()
