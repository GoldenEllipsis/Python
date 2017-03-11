from turtle import *

setup(800,500,300,0)
bgcolor("black")

def set_pos(x):
    penup()
    setpos(x*120,-80)
    pendown()
    
def draw_heart():
    color('pink',"red")
    begin_fill()
    left(142)
    forward(111)
    circle(-70,180)
    left(77)
    circle(-70,180)
    forward(111)
    end_fill()

def main():
    for i in range(2):
        set_pos(i)
        draw_heart()
        left(142)
        
main()
hideturtle()
done()
