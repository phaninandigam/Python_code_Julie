# import turtle
import random
from turtle import Turtle, Screen


my_turtle=Turtle()
my_colour=["green yellow","olive","magenta","medium violet red","maroon","lime green","midnight blue"]

for sides in range(3,11):
    angle=360/sides
    my_turtle.color(random.choice(my_colour))
    for value in range(sides):
        # my_turtle.color(random.choice(my_colour))
        # my_turtle.fillcolor(random.choice(my_colour))
        my_turtle.forward(100)
        my_turtle.right(angle)
        # my_turtle.forward(100)
        # my_turtle.right(90)


my_screen=Screen()
my_screen.exitonclick()