import random
import turtle
from turtle import Turtle, Screen
bobo = Turtle()
bobo.shape("turtle")
turtle.colormode(255)
direction = 1
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spiro(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        bobo.color(random_color())
        bobo.width(2)
        bobo.circle(130)
        bobo.setheading(bobo.heading() + size_of_gap)
        bobo.speed("fastest")

draw_spiro(4)






screen = Screen()
screen.exitonclick()
