import turtle
import colorsys

turtle.setup(width=400, height=400) 
turtle.speed(1)     
turtle.tracer(1)    
#turtle.width(2)
turtle.bgcolor("black")

h = 0  

# Drawing loop
for i in range(50):
    
    c = colorsys.hsv_to_rgb(h, 1, 1)
    turtle.color(c)
    
    h += 0.005
    turtle.forward(i * 2)
    turtle.left(91)

turtle.done()