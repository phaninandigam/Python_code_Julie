from turtle import Turtle, Screen

# documentation https://docs.python.org/3/library/turtle.html


my_turtle=Turtle()
my_turtle.shape("turtle")

# draw a sqaure
for item in range(4):
    my_turtle.forward(100)
    my_turtle.left(90)

# my_turtle.done()
# draw a dashed line
for _ in range(15):
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(5)
    my_turtle.pendown()

# to draw different shapes triangle, sqaure, pentagon .....
def draw_shapes(num_sides):
    angle=360/num_sides
    for _ in range(num_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)

for shape_to_draw in range(3,11):
    draw_shapes(shape_to_draw)
#     end
screen=Screen()
screen.exitonclick()