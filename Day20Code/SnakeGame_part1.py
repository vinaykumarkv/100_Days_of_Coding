from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# all_turtles=[]
# x_positions = [0, -20, -40]
# for turtle_index in range(0, 3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.penup()
#     new_turtle.color("white")
#     new_turtle.goto(x=x_positions[turtle_index], y=0)
#     all_turtles.append(new_turtle)
#     print(all_turtles)
# screen.update()
#
# def move_forward():
#     all_turtles[0].forward(10)
#     all_turtles[1].forward(10)
#     all_turtles[2].forward(10)
#
#
#
#
# def move_left():
#     all_turtles[0].lt(90)
#     all_turtles[1].forward(20)
#     all_turtles[1].lt(90)
#     all_turtles[0].forward(40)
#     all_turtles[1].forward(20)
#     all_turtles[2].forward(40)
#     all_turtles[2].lt(90)
#
#
# def move_right():
#     all_turtles[0].rt(90)
#     all_turtles[1].forward(20)
#     all_turtles[1].rt(90)
#     all_turtles[0].forward(40)
#     all_turtles[1].forward(20)
#     all_turtles[2].forward(40)
#     all_turtles[2].rt(90)
#
#
# while True:
#     for i in all_turtles:
#         i.forward(20)
#         screen.listen()
#         screen.onkey(key="w", fun=move_forward)
#         screen.onkey(key="a", fun=move_left)
#         screen.onkey(key="d", fun=move_right)
#
#         if i.xcor() > 300:
#             i.hideturtle()
#             i.goto(x=-300,y=0)
#             i.speed("fastest")
#             i.showturtle()
#             i.speed(10)
#     screen.update()
#     time.sleep(0.2)

snake = Snake()
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
screen.exitonclick()