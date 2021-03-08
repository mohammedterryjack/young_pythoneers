from turtle import Screen, Turtle

turtle_world = Screen()
turtle_world.bgcolor("pink")

robot = Turtle()
robot.shape("turtle")
robot.color("magenta","yellow")

robot.right(30)
robot.forward(100)
robot.left(80)
robot.backward(200)

robot.circle(60)

turtle_world.exitonclick()