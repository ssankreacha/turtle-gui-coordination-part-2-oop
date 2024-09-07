from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-75, -50, -25, 0, 25, 50, 75]
all_turtles = []

for each_turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[each_turtle])
    new_turtle.teleport(-235, y_positions[each_turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner! ")

screen.exitonclick()

