#in this program i am drawing my name using turtle

import turtle

def my_name():
    nitya = turtle.Turtle()
    nitya.shape("turtle")
    nitya.left(90)
    nitya.forward(100)
    nitya.right(140)
    nitya.forward(120)

window = turtle.Screen()
window.bgcolor("red")
my_name()
window.exitonclick()
