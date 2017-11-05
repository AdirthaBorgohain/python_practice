import turtle


def draw_square(degree):
    jerry = turtle.Turtle()
    jerry.shape("turtle")
    jerry.speed(3)
    jerry.right(degree) #initian rotation of turtle
    for x in range(0,4):
        jerry.forward(100)
        jerry.right(90)

def cirle_from_square():
    degree=0
    while(degree<360):
        draw_square(degree)
        degree=degree+10

window = turtle.Screen()
window.bgcolor("yellow")
cirle_from_square()
window.exitonclick()
