import turtle
import colorsys

iteration = int(input("How many iterations do you want?: "))
star_points = int(input("How many points of the star do you want?: "))
forward_move = int(input("How far apart do you want the points of the star, in pixels?: "))

#defining variables for later
t = turtle.Turtle()
s = turtle.Screen()
s.screensize()
s.bgcolor('black')
t.speed(0)

# n == number of colors
n = 4
# h == starting color, and it'll loop in "for i in range" later on
h = 0

# tells turtle where to go and start drawing
t.goto(0, 0)
t.pendown()


for i in range(iteration):
    # color number, vibrance, opacity
    c = colorsys.hsv_to_rgb(h, 0.5, 1)
    h += 1 / n
    t.color(c)
    # next 6 lines are for pen movement
    t.left(149)
    t.forward(150)
    t.pendown()
    for j in range(star_points):
        t.forward(forward_move)
        t.left(150)

turtle.done()
