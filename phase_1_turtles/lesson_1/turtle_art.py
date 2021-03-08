from turtle import Screen, Turtle

turtle_world = Screen()
turtle_world.bgcolor("pink")

robot = Turtle()
robot.shape("turtle")
robot.color("magenta","yellow")

for _ in range(30):
    robot.right(10)
    robot.forward(30)
    robot.left(80)
    robot.backward(20)

turtle_world.exitonclick()