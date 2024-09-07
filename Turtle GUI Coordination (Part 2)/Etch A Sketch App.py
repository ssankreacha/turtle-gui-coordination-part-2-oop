from turtle import Turtle, Screen

"""
W = Forwards
S = Backwards
A = Counter-Clockwise
D = Clockwise

"""

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(25)
def move_backward():
    tim.backward(25)
def turn_left():
    tim.left(10)
def turn_right():
    tim.right(10)
def clear():
    tim.clear()
    tim.teleport(0, 0)
    tim.reset()

screen.listen() # Program is listening for the following
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()




