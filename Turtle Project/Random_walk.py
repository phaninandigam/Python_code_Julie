import random
from turtle import Turtle, Screen

my_turtle=Turtle()
my_turtle.width(15)
my_turtle.speed('slow')
my_colour=["green yellow","olive","magenta","medium violet red","maroon","lime green","midnight blue","blue","orange red",
           "indigo","medium violet red","gold","dark slate gray"]
direction=[0,90,180,270]

for _ in range(500):
    my_turtle.color(random.choice(my_colour))
    my_turtle.setheading(random.choice(direction))
    # my_turtle.right(random.choice(direction))
    my_turtle.forward(40)


    # my_turtle.direction(90)

my_screen=Screen()
my_screen.exitonclick()