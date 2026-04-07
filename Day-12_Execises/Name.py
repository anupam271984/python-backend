import turtle
import colorsys
import time

# 1. Setup small screen
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.penup()

name = "ANUPAM"
x, y = 0, 0          # Starting position for movement
dx, dy = 2, 2        # Speed (pixels per frame)
font_size = 50

# --- PART 1: ZOOM IN ANIMATION ---
for i, char in enumerate(name):
    for size in range(1, font_size, 4):
        t.clear()
        # Draw previous letters
        curr_x = -150
        for j in range(i):
            t.goto(curr_x, 0)
            t.color(colorsys.hsv_to_rgb(j/len(name), 1, 1))
            t.write(name[j], font=("Arial", font_size, "bold"))
            curr_x += 50
        # Zoom current letter
        t.goto(curr_x, 0)
        t.color(colorsys.hsv_to_rgb(i/len(name), 1, 1))
        t.write(char, font=("Arial", size, "bold"))
        screen.update()
        time.sleep(0.01)

# --- PART 2: CONTINUOUS BOUNCING ---
try:
    while True:
        t.clear()
        
        x += dx
        y += dy

        # Boundary checks
        if x > 100 or x < -250:
            dx *= -1
        if y > 150 or y < -150:
            dy *= -1

        # Draw the whole name
        temp_x = x
        for i, char in enumerate(name):
            # Dynamic colors - change hue based on time/position
            color = colorsys.hsv_to_rgb((i/len(name) + time.time()/5) % 1, 1, 1)
            t.color(color)
            t.goto(temp_x, y)
            t.write(char, font=("Arial", font_size, "bold"))
            temp_x += 50 
        
        screen.update()
        time.sleep(0.01)

except turtle.Terminator:
    print("Animation stopped by user.")
except Exception:
    pass # Catch any remaining Tkinter errors during exit
