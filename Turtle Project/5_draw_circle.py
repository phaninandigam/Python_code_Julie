import random
from turtle import Turtle, Screen
import turtle

my_turtle=Turtle()
my_turtle.speed("fastest")
turtle.colormode(255)

def random_colur():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

def draw_spirograph(size_of_gap):
    # for _ in range(300):
    #     my_turtle.color(random_colur())
    #     my_turtle.circle(100)
    #     my_turtle.left(5)

        # OR

    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random_colur())
        my_turtle.circle(100)
        current_heading=my_turtle.heading()
        my_turtle.setheading(current_heading + size_of_gap)


draw_spirograph(1)
my_screen= Screen()
my_screen.exitonclick()