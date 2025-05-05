import random
import turtle
from turtle import Turtle, Screen

my_turtle=Turtle()
my_turtle.width(15)
my_turtle.speed('fast')
turtle.colormode(255)
direction=[0,90,180,270]

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

for _ in range(500):
    my_turtle.pencolor(random_colour())
    my_turtle.setheading(random.choice(direction))
    # my_turtle.right(random.choice(direction))
    my_turtle.forward(40)


my_screen=Screen()
my_screen.exitonclick()