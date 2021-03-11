from turtle import Screen, Turtle
turtle_world = Screen()
robot = Turtle()

turtle_world.onkeypress(lambda:robot.forward(10),"Up") 
turtle_world.listen()

turtle_world.exitonclick()