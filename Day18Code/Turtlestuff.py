import turtle as t
import random

tim = t.Turtle()
screen = t.Screen()
def turtlesquare(number):
    for i in range(4):
        tim.forward(100)
        tim.lt(90)


def turtledotline(number):
    for i in range(15):
        tim.forward(number)
        tim.penup()
        tim.forward(number)
        tim.pendown()


def turtleshapes():
    colors = ["red", "blue", "green", "orange", "yellow"]
    shapes = [3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(shapes)):
        tim.pencolor(random.choice(colors))
        for j in range(shapes[i]):
            tim.forward(100)
            tilt = 360 / shapes[i]
            tim.lt(tilt)


t.colormode(255)


def randomcolor():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return r, g, b


def randomwalk():
    colors = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue",
              "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
    angles = [90, 180, 270, 360]
    tim.pensize(10)
    tim.speed("fastest")
    for i in range(500):
        tim.pencolor(randomcolor())
        tim.forward(20)
        tim.setheading(random.choice(angles))

def sprialdiagram(n):
    tim.speed("fastest")
    for i in range(round(360/(n))):
        tim.circle(100)
        tim.lt(n)
        tim.pencolor(randomcolor())




tim.shape("turtle")
tim.color("blue")
# turtlesquare(100)
# turtledotline(10)
# turtleshapes()
# randomwalk()
sprialdiagram(5)

screen.exitonclick()
