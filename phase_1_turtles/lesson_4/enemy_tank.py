from turtle import Screen, Turtle, ontimer
from utils import set_custom_shape, tank_shape, random_coordinates
from typing import Tuple
from tank_missile_controls_ai import Tank

turtle_world = Screen()

tank = Tank()
tank.register_controls_to_world(turtle_world)

enemy = Tank(("green","red"),random_coordinates())
enemy.drive_to_target(tank)

turtle_world.listen()
turtle_world.exitonclick()