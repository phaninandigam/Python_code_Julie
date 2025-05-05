import random
import turtle
from turtle import Turtle, Screen

my_turtle=Turtle()
my_turtle.width(15)
my_turtle.speed('fastest')
turtle.colormode(255)

def random_colur():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)



for _ in range(5):
    for _ in range(7):
        my_turtle.pendown()
        my_turtle.color(random_colur())
        my_turtle.circle(15) #change this value to show different shapes 8 0r 12
        my_turtle.penup()
        my_turtle.forward(40)
        print(f"x co-ord value is {my_turtle.xcor()}")
        print(f"Y co-ord value is {my_turtle.ycor()}")

    my_turtle.penup()
    my_turtle.sety(my_turtle.ycor()+50)
    my_turtle.setx(0)



my_screen=Screen()
my_screen.exitonclick()

