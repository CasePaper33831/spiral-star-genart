'''TODO: 
make sure center of rotation is at 0,0
'''

import turtle
import colorsys

iteration = int(input("How many iterations do you want?: "))
star_points = int(input("How many points of the star do you want?: "))
foward_move = int(input("How far apart do you want the points of the star, in pixles?: "))

t = turtle.Turtle()
s = turtle.Screen()

s.screensize()
s.bgcolor('black')
t.speed(0)

n = 36
h = 0

t.goto(0, 0) 
t.pendown()

for i in range(iteration):
    c = colorsys.hsv_to_rgb(h, 1, 0.8)
    h += 1 / n
    t.color(c)
    t.left(149)
    t.forward(150) 
    t.pendown() 
    for j in range(star_points):
        t.forward(foward_move)
        t.left(150)

turtle.done()
