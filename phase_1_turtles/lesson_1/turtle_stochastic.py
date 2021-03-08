from turtle import Screen, Turtle
from random import randint

turtle_world = Screen()
turtle_world.bgcolor("pink")

robot = Turtle()
robot.shape("turtle")
robot.color("magenta","yellow")

for _ in range(30):
    random_number = randint(0,50)
    robot.right(10)
    robot.forward(random_number)
    robot.left(80)
    robot.backward(20)

turtle_world.exitonclick()