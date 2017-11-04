
import turtle

def draw_square():
    baby = turtle.Turtle() #grabs the turtle and names it chutiya
    
    baby.color("green")
    baby.shape("turtle")
    baby.speed(2)

    for i in range(0,4):
        baby.forward(100)
        baby.right(90)


def draw_circle():
    jhon = turtle.Turtle()
    jhon.shape("arrow")
    jhon.color("black")
    jhon.speed(2)

    jhon.circle(100)


def draw_triangle():
    tangy = turtle.Turtle()
    tangy.shape("turtle")
    tangy.color("yellow")
    tangy.left(180)
    for i in range(0,3):
        tangy.forward(50)
        tangy.right(120)
    
window = turtle.Screen()
window.bgcolor("red")

#drawing square
draw_square()

#drawing circle
draw_circle()

#drawing rectangle
draw_triangle()

window.exitonclick()
