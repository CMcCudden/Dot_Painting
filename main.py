import colorgram
import random
from turtle import Turtle, Screen
import turtle as t

#First uncomment the code below, load your picture file into the program or provide the path to the file, and allow it
# to print the RGB numbers for the random colors.

# rgb = []
# colors = colorgram.extract('NAME/PATH TO YOUR PICTURE GOES HERE', 8)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)
# print(rgb)


dot = t.Turtle()
dot.shape('circle')
dot.hideturtle()
dot.speed('fastest')
dot.pensize(15)
DOT_SIZE = 60
screen = Screen()
screen.screensize(165, 100)
dot.penup()
dot.goto(DOT_SIZE/2 - screen.window_width()/2, screen.window_height()/2 - DOT_SIZE/2)
dot.pendown()
t.colormode(255)
colors = "TAKE THE LIST OF COLORS PRINTED FROM THE PIECE OF CODE ABOVE AND PASTE IT HERE, THEN RUN THE PROGRAM"


def draw(space, x):
    for i in range(x):
        for j in range(x):
            dot.color(random.choice(colors))
            dot.dot()
            dot.forward(space)
        dot.backward(space*x)
        dot.right(90)
        dot.forward(space)
        dot.left(90)
dot.penup()
draw(35, 18)

screen.mainloop()
