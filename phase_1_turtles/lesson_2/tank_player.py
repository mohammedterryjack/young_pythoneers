from turtle import Screen, Turtle
from utils import set_custom_shape, tank_shape

turtle_world = Screen()
turtle_world.bgcolor("pink")

tank = Turtle()
set_custom_shape(tank,tank_shape)
tank.color("magenta","yellow")
tank.penup()

turtle_world.onkeypress(lambda:tank.forward(10),"Up") 
turtle_world.onkeypress(lambda:tank.backward(10),"Down") 
turtle_world.onkeypress(lambda:tank.left(10),"Left") 
turtle_world.onkeypress(lambda:tank.right(10),"Right") 

turtle_world.listen()
turtle_world.exitonclick()