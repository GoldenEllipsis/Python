import turtle,random
 
# random color
def set_color():
    color_n = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,'A', 'B', 'C', 'D', 'E', 'F']
    random_color_n = random.sample(color_n, 6)
    color = "#"
    for i in random_color_n:
        color = color + str(i)
    return color
 
def draw_snake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.pencolor(set_color())
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)
 
def main():
    turtle.setup(800,200,100,0)
     
    turtle.penup()
    turtle.setpos(-300,0)
    turtle.pendown()
     
    pythonsize = 30
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    draw_snake(40,80,5,pythonsize/2)
 
main()
