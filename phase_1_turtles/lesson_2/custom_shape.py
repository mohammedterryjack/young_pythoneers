from turtle import Screen, Turtle
from utils import set_custom_shape
from random import randint

world = Screen()
robot = Turtle()

def ninja_star(robot:Turtle) -> None:
    for _ in range(8):
        robot.forward(10)
        robot.right(47)
        robot.backward(3)

set_custom_shape(robot, ninja_star)

for _ in range(100):
    robot.forward(randint(0,10))
    robot.right(randint(-10,30))

world.exitonclick()